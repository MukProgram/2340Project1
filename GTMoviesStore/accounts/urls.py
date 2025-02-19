from django.urls import path
from accounts.views import PasswordResetView
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('signup/', views.signup, name='accounts.signup'),
    path('login/', views.login, name='accounts.login'),
    path('logout/', views.logout, name='accounts.logout'),
    path('orders/', views.orders, name='accounts.orders'),
    path('reset_password/', views.PasswordResetView.as_view(), name ='reset_password'),
     path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name ='password_reset_done'),
     path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name ='password_reset_confirm'),
     path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name ='password_reset_complete'),
]