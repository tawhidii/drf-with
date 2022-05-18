from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views as user_view
urlpatterns = [
    # path('login',views.obtain_auth_token,name='login'),
    path('register',user_view.register_user,name='register'),
    path('logout',user_view.logout_view,name='logout'),

    # JWT
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]