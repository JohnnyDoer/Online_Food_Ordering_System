from . import views
from django.urls import path, re_path


urlpatterns = [
    path('', views.index, name='Del_index'),
    path('signup/', views.signup, name='Del_signup'),
    path('profile/', views.profile_page, name='Del_profile'),
    path('ajax/load-areas/', views.load_areas, name='Del_ajax_load_areas'),
    re_path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate, name='Del_activate'),
    path('del_orders/', views.del_orders, name='Del_orders'),
    path('edit/', views.edit_profile, name='Del_edit_profile'),
]
