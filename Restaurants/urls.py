from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.index, name='Res_index'),
    path('signup/', views.signup, name='Res_signup'),
    path('profile/', views.profile_page, name='Res_profile'),
    path('ajax/load-areas/', views.load_areas, name='Res_ajax_load_areas'),
    re_path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate, name='Res_activate'),
    path('info/', views.restaurant, name='Res_info'),
    path('add_item/', views.add_item, name='Res_add_item'),
    path('view_orders/', views.view_orders, name='View_order'),
    path('edit/', views.edit_profile, name='Res_edit_profile'),
    path('edit_item/', views.edit_food, name='Res_edit_food'),
    path('delete_item/', views.del_item, name='Res_del_item'),

]
