from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path('', views.RecordListView.as_view(), name='record_list'),
    path('create/', views.RecordCreateView.as_view(), name='record_create'),
    path('<int:pk>/edit/', views.RecordUpdateView.as_view(), name='record_edit'),
    path('<int:pk>/delete/', views.RecordDeleteView.as_view(), name='record_delete'),
    path('references/', views.reference_management, name='reference_management'),
    
    
    path('references/status/<int:pk>/delete/', views.delete_status, name='delete_status'),
    path('references/operation-type/<int:pk>/delete/', views.delete_operation_type, name='delete_operation_type'),
    path('references/category/<int:pk>/delete/', views.delete_category, name='delete_category'),
    path('references/subcategory/<int:pk>/delete/', views.delete_subcategory, name='delete_subcategory'),

    path('references/status/<int:pk>/edit/', views.edit_status, name='edit_status'),
    path('references/operation-type/<int:pk>/edit/', views.edit_operation_type, name='edit_operation_type'),
    path('references/category/<int:pk>/edit/', views.edit_category, name='edit_category'),
    path('references/subcategory/<int:pk>/edit/', views.edit_subcategory, name='edit_subcategory'),
    
    path('ajax/get-categories/', views.get_categories_by_type, name='get_categories_by_type'),
    path('ajax/get-subcategories/', views.get_subcategories_by_category, name='get_subcategories_by_category'),
]