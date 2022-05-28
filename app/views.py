from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, ApiSerializer
import requests

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #ordering = [id]

class DetailView(DetailView):
    model = Post
    template_name = 'detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create.html'

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ApiViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = ApiSerializer

def api(request):
    
    response=requests.get('https://jsonplaceholder.typicode.com/posts').json()

    return render(request, 'api.html', {'response': response})