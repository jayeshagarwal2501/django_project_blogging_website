from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('',views.base,name=""),
    
    path('register/',views.register_request,name="register"),

    path('login/',views.MyLoginView.as_view(),name="login"),
    
    path('profile/',views.profile,name='profile'),
   
    path('changepass/',views.MyPasswordChangeView.as_view(),name="changepass"),
   
    path('changepassdone/',views.MyPasswordChangeDoneView.as_view(),name="changepassdone"),

    path('logout/',views.MyLogoutView.as_view(),name="logout"),

    path('passreset/',views.MyPasswordResetView.as_view(),name="resetpassword"),

    path('passresetdone/',views.MyPasswordResetDoneView.as_view(),name="password_reset_done"),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'register/PasswordResetConfirmView.html'),name='password_reset_confirm'),
   
    path("reset/done/",auth_views.PasswordResetCompleteView.as_view(template_name='register/PasswordResetCompleteView.html'), name='password_reset_complete'),

    path('user/',views.detail_user,name="user_details"),

]