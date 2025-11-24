from django.urls import path
from . import views

app_name='inventory'

urlpatterns = [
    path('', views.IndexView.as_view(),name='index'),
    path('blog-detail/<int:pk>/',
         views.InventoryDetail.as_view(),
         name='inventory_detail'),
     path('inventory/<int:pk>/delete/',
          views.InventoryDeleteView.as_view(),
          name = 'inventory_delete'),
    path('daily_necessities_list/',
         views.Daily_necessitiesView.as_view(),
         name='daily_necessities_list'),
    path('daily_goods_list/',
         views.Daily_goodsView.as_view(),
         name='daily_goods_list'),
    path('groceries/',
         views.GroceriesView.as_view(),
         name='groceries_list'),    
     path(
          'contact/',
          views.ContactView.as_view(),
          name='contact'),

    ]
