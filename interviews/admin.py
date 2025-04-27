from django.contrib import admin
from .models import Interview, MediaAttachment


class MediaAttachmentInline(admin.TabularInline):
    model = MediaAttachment
    extra = 1


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'source', 'interviewer')
    list_filter = ('date', 'source')
    search_fields = ('title', 'original_text_ru', 'translation_en')
    inlines = [MediaAttachmentInline]


admin.site.register(MediaAttachment)
