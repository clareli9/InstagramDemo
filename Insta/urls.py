from django.contrib import admin
from django.urls import path, include

from Insta.views import (PostListView, PostDetailView, PostCreateView, PostUpdateView, 
                        PostDeleteView, UserProfile, EditProfile, ExploreView, 
                        SignupView, addLike, addComment, toggleFollow)

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('/', include('Insta.urls')),
    path('', PostListView.as_view(), name = 'home'),
    path('post/<int:pk>', PostDetailView.as_view(), name = 'post'),
    path('make_post/', PostCreateView.as_view(), name = 'make_post'),
    path('update_post/<int:pk>/', PostUpdateView.as_view(), name = 'edit_post'),
    path('delete_post/<int:pk>/', PostDeleteView.as_view(), name = 'delete_post'),
    path('auth/signup', SignupView.as_view(), name='signup'),
    path('user/<int:pk>', UserProfile.as_view(), name = 'profile'),
    path('edit_profile/<int:pk>', EditProfile.as_view(), name = 'edit_profile'),
    path('like', addLike, name = 'addLike'),
    path('comment', addComment, name = 'addComment'),
    path('togglefollow', toggleFollow, name = 'togglefollow'),
    path('explore', ExploreView.as_view(), name='explore'),
]