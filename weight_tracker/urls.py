# weight_tracker/urls.py
from django.urls import path
from . import views  # Perubahan di sini

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:record_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:record_id>/edit/', views.edit, name='edit'),
    path('edit/<int:record_id>/', views.edit, name='edit'),
    path('<int:record_id>/hapus/', views.hapus_record, name='hapus'),

]
