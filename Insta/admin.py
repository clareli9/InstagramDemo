from django.contrib import admin
from Insta.models import Post, InstaUser, Comment, Like, UserConnection

class CommentInline(admin.StackedInline):
    model = Comment

class LikeInline(admin.StackedInline):
    model = Like

class FollowingInline(admin.StackedInline):
    model = UserConnection
    fk_name = 'creator'

class FollowerInline(admin.StackedInline):
    model = UserConnection
    fk_name = 'following'

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
        LikeInline,
    ]

class UserAdmin(admin.ModelAdmin):
    inlines = [
        FollowerInline,
        FollowingInline,
    ]

# Register your models here.
admin.site.register(Post)
admin.site.register(InstaUser)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(UserConnection)