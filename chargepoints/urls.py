from django.urls import path
from chargepoints import views

urlpatterns = [
    path('chargepoint/get/', views.chargepoint_get_list),
    path('chargepoint/get/<int:pk>/', views.chargepoint_get_single),
    path('chargepoint/post/', views.chargepoint_post_single),
    path('chargepoint/delete/<int:pk>/', views.chargepoint_delete_single),
    path('customers/get/', views.customers_get_list),
    path('customers/get/<int:pk>/', views.customers_get_single),
    path('customers/post/<int:pk>/', views.customers_post_single),
    path('customers/delete/<int:pk>/', views.customers_delete_single),
]
