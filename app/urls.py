from django.urls import path
from.views import HomeView, DetailView, AddPostView, UpdatePostView, DeletePostView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/', views.api, name='api'),
    path('detail/<int:pk>', DetailView.as_view(), name='detail'),
    path('create/', AddPostView.as_view(), name='create'),
    path('update/<int:pk>', UpdatePostView.as_view(), name='update'),
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete'),
]
