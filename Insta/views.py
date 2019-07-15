from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from Insta.models import Post, InstaUser, Like, Comment 
from Insta.forms import CustomUserCreationForm

from annoying.decorators import ajax_request

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

# The view for insta users profile
class UserDetail(DetailView):
    model = InstaUser
    template_name = "user_profile.html"

class EditProfile(UpdateView):
    model = InstaUser
    template_name = "edit_profile.html"
    fields = ('username', 'profile_pic')

@ajax_request
def toggleFollow(request):
    current_user = InstaUser.objects.get(pk=request.user.pk)
    follow_user_pk = request.POST.get('follow_user_pk')
    follow_user = InstaUser.objects.get(pk=follow_user_pk)

    try:
        if current_user != follow_user:
            if request.POST.get('type') == 'follow':
                connection = UserConnection(creator=current_user, following=follow_user)
                connection.save()
            elif request.POST.get('type') == 'unfollow':
                UserConnection.objects.filter(creator=current_user, following=follow_user).delete()
            result = 1
        else:
            result = 0
    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'type': request.POST.get('type'),
        'follow_user_pk': follow_user_pk
    }

@ajax_request
def addLike(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    try:
        # It's about how to add data to Django database 
        like = Like(post=post, user=request.user)
        like.save()
        result = 1
    except Exception as e:
        # One user can not like the post twice
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }


@ajax_request
def addComment(request):
    comment_text = request.POST.get('comment_text')
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    commenter_info = {}

    try:
        comment = Comment(comment=comment_text, user=request.user, post=post)
        comment.save()

        username = request.user.username

        commenter_info = {
            'username': username,
            'comment_text': comment_text
        }

        result = 1
    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'post_pk': post_pk,
        'commenter_info': commenter_info
    }





def blog_detail_view(request, primary_key):
    try:
        post = Post.objects.get(pk = primary_key)
    except Post.DoesNotExist:
        raise Http404('Post does not exist')
    return render(request, 'post_detail.html', context = {'post': post})