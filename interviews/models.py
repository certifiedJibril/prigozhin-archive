import uuid
from django.db import models


class Interview(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField()
    date = models.DateField()
    source = models.TextField(blank=True, null=True)
    interviewer = models.TextField(blank=True, null=True)
    tags = models.JSONField(default=list, blank=True)
    original_text_ru = models.TextField()
    translation_en = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.date})"


class MediaAttachment(models.Model):
    FILE_TYPES = (
        ('pdf', 'PDF Document'),
        ('image', 'Image'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    interview = models.ForeignKey(
        Interview, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='media/')
    file_type = models.CharField(max_length=10, choices=FILE_TYPES)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file_type} for {self.interview.title}"
