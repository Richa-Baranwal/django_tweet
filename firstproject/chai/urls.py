from django.urls import path
from . import views

urlpatterns = [
    # localhost:8000/chai/
    path('', views.myapp, name = 'myapp'),
    # localhost:8000/chai/order/
    path('order/', views.order, name='order'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
    path('chai_stores/', views.chai_store_view, name='chai_stores'),
]