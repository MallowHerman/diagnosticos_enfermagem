from django.urls import path
from .  import views

urlpatterns = [
    path('', views.DiagnosesListView.as_view(), name='diagnoses-list'),
    path('detail/<int:pk>/', views.DiagnosesDetailView.as_view(), name='diagnoses-detail')
]