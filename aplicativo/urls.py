from django.urls import path
from aplicativo import views

app_name = 'aplicativo'

urlpatterns = [
    path('', views.ProdutoMenu.as_view(), name='menu'),
    path('list', views.ProdutoList.as_view(), name='list'),
    path('create/', views.ProdutoCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.ProdutoUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.ProdutoDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.ProdutoDelete.as_view(), name='delete'),
]
