from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('proiecte/', views.ProjectListView.as_view(), name='project_list'),
    path('proiecte/<slug:slug>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('rezumat/', views.ResumeView.as_view(), name='resume'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]

