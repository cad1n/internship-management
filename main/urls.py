from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from main import settings
from django.contrib.auth import views as auth_views
from management_app.views import redirect_to_angular

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('', redirect_to_angular),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
