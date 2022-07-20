from django.urls import path
from django.conf.urls.static import static
from app_users.views import RegisterView, AuthLoginView, AuthLogoutView, MainView, ProfileUserView, EditProfileView
from djtesting import settings


urlpatterns = [
    path('', MainView.as_view(), name='main_url'),
    path('register/', RegisterView.as_view(), name='register_url'),
    path('login/', AuthLoginView.as_view(), name='login_url'),
    path('logout/', AuthLogoutView.as_view(), name='logout_url'),
    path('profile/', ProfileUserView.as_view(), name='profile_url'),
    path('profile/edit/<int:user_id>', EditProfileView.as_view(), name='edit_url'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
