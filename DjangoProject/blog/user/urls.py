from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

#rest
# urls.py
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    ##path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),  # This can stay as it is
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

