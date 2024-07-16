from django.contrib import admin
from django.urls import path, include
from content.views import Main, UploadFeed
from user.views import Register, Login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', Main.as_view()),
    path('content/upload', UploadFeed.as_view()),
    path('user/register', Register.as_view()),
    path('user/login', Login.as_view())
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
