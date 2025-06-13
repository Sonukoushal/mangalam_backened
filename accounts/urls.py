from django.urls import path
from .views import SignupView,LoginView,LogoutView,PromoteSuperuser
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("signup/",SignupView.as_view()),
    path("login/",LoginView.as_view()),
    path("logout/",LogoutView.as_view()),
    path("make-superuser/<int:user_id>/", PromoteSuperuser.as_view()),
    path('api-token-auth/',obtain_auth_token)
]

 