from django.contrib import admin
from django.urls import path
from todoapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.login,name="login"),
    path("signup",views.signup,name="signup"),
    path("recovery",views.recovery,name="recovery"),
    path("terms",views.terms,name="terms"),
    path("home",views.home,name="home"),
    path("logout",views.logout,name="logout"),
    
    # password reset
    path('password_reset',auth_views.PasswordResetView.as_view(template_name='recovery.html'),name='password_reset'),

    path('password_reset_done',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
    name='password_reset_confirm'),

    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),

]