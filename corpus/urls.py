from django.contrib import admin
from django.urls import path, include  # 👈 include was missing

urlpatterns = [
    path('admin/', admin.site.urls),
    # 👈 this line activates your app’s routes!
    path('', include('interviews.urls')),
]
