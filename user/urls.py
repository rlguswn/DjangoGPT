from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # User 기능 url
    # # 회원가입 /user/register/
    path('register/', views.UserRegister.as_view(), name='register'),
    # # 로그인 /user/login/
    path('login/', views.UserLogin.as_view(), name='login'),
    # # 로그아웃 /user/logout/
    path('logout/', views.UserLogout.as_view(), name='logout'),
    #
    # # Profile 기능 url
    # # 프로필 /profile/
    # path('profile/<str:user>/', views.ProfileDetail.as_view(), name='p-detail'),
    # # 프로필 /profile/update/
    # path('profile/<str:user>/update/', views.ProfileUpdate.as_view(), name='p-update')
]
