from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from main import settings
# from management_app import urls as management_app_urls
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', admin.site.urls),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
