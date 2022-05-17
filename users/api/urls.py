from django.urls import path
from rest_framework.authtoken import views
from . import views as user_view
urlpatterns = [
    path('login',views.obtain_auth_token,name='login'),
    path('register',user_view.register_user,name='register'),
    path('logout',user_view.logout_view,name='logout')
]