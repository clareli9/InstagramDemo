from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from Insta.models import Post, InstaUser 
from Insta.forms import CustomUserCreationForm

# Create your views here.
class HelloDjango(TemplateView):
    template_name = 'home.html'

# Mixin is something like interface in Java
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts.html'
    # The reason why no need reverse, it's the use of Mixin interface
    login_url = "login"

class PostDetailView(DetailView):
    model = Post 
    template_name = "post_detail.html"

class BlogDetailView(DetailView):
    model = Post 
    template_name = "post_detail.html"

# Let the user to input information (all fields)
class PostCreateView(CreateView):
    model = Post 
    template_name = "make_post.html"
    fields = '__all__'

# Let the user to modify information (only title field)
class PostUpdateView(UpdateView):
    model = Post 
    template_name = "update_post.html"
    fields = ('title',)

class PostDeleteView(DeleteView):
    model = Post 
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')

class SignupView(CreateView):
    form_class = CustomUserCreationForm
    #form_class = UserCreationForm
    template_name = "registration/signup.html" 
    success_url = reverse_lazy('login')  





def blog_detail_view(request, primary_key):
    try:
        post = Post.objects.get(pk = primary_key)
    except Post.DoesNotExist:
        raise Http404('Post does not exist')
    return render(request, 'post_detail.html', context = {'post': post})