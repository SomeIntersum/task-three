from django.urls import path

from travels.views import home, user_detail, travel_detail, my_travels, create_travel

urlpatterns = [
    path('', home, name='home'),
    path('user/<int:user_id>/', user_detail, name='user_detail'),
    path('travel/<int:travel_id>/', travel_detail, name='travel_detail'),
    path('my-travels/', my_travels, name='my_travels'),
    path('create-travel/', create_travel, name='create_travel'),
]
