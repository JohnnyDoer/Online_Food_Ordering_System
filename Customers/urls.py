from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('', views.index, name='Cus_index'),
    path('signup/', views.signup, name='Cus_signup'),
    path('login/', views.loginform, name='Cus_login'),
    path('profile/', views.profile_page, name='Cus_profile'),
    path('ajax/load-areas/', views.load_areas, name='Cus_ajax_load_areas'),
    path('logout/', views.user_logout, name='logout'),
    path('categories/', views.categories, name='Cus_categories'),
    path('res_area/', views.restaurants, name='res_area'),
    re_path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate, name='Cus_activate'),
    path('res_info/', views.res_info, name='Cus_resinfo'),
    path('add_address/', views.add_address, name='add_address'),
    path('add_to_cart/', views.add_to_cart, name='Cus_add_cart'),
    path('cart/', views.cart, name='Cus_cart'),
    path('delete/', views.delete, name='Cus_delete'),
    path('Receipt/', views.receipt, name='Cus_receipt'),
    path('edit/', views.edit_profile, name='Cus_edit_profile'),
    path('your_profile/', views.show_profile, name='Cus_show_profile'),
    path('search/', include('haystack.urls')),
]
