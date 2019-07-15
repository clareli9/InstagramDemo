from django.contrib import admin
from django.urls import path, include

from Insta.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserDetail, EditProfile, addLike

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('/', include('Insta.urls')),
    path('', PostListView.as_view(), name = 'home'),
    path('post/<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
    path('make_post/', PostCreateView.as_view(), name = 'make_post'),
    path('update_post/<int:pk>/', PostUpdateView.as_view(), name = 'update_post'),
    path('delete_post/<int:pk>/', PostDeleteView.as_view(), name = 'delete_post'),
    path('user/<int:pk>', UserDetail.as_view(), name = 'user_profile'),
    path('edit_profile/<int:pk>', EditProfile.as_view(), name = 'edit_profile'),
    path('like', addLike, name = 'like')
    #path('comment', addComment, name = 'addComment')
]