from rest_framework.routers import DefaultRouter
from django.urls import path,re_path,include
from . import views
from .views import *
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

userSignup=UserViewSet.as_view({
    'get':'list',
    'post':'create'
})
userDetail=UserViewSet.as_view({
    'get':'retrieve'
})


router = DefaultRouter()

router.register(r'Profile', ProfileViewSet)
router.register(r'User', UserViewSet)


urlpatterns =[
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/signup/', userSignup, name='user_signup'),
    # path('users/<int:pk>/', userDetail, name='user-detail'),
    path('api/v1/', include(router.urls)),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

] 