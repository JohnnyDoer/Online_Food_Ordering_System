from django.urls import path, include
from . import views
from django.urls import path, re_path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='Res_index'),
    path('signup/', views.signup, name='Res_signup'),
    path('profile/', views.profile_page, name='Res_profile'),
    re_path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate, name='activate'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name=
                                                                 'Restaurant/password_reset.html'),
                                                                    name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name=
                                                  'Restaurant/password_reset_done.html'),
                                                    name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name=
                                                     'Restaurant/password_reset_confirm.html'),
                                                    name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name=
                                                      'Restaurant/password_reset_complete.html'),
                                                        name='password_reset_complete'),
]
