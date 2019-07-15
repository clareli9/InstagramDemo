from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField
from django.contrib.auth.models import AbstractUser


class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to = 'static/images/profiles',
        format = 'JPEG',
        options = {'quality': 100},
        null = True,
        blank = True,
    )

    def get_followings(self):
        followings = UserConnection.objects.filter(creator = self)
        return followings
    
    def get_followers(self):
        followers = UserConnection.objects.filter(following = self)
        return followers

    def is_followed_by(self, user):
        followers = UserConnection.objects.filter(following = self)
        return followers.filter(creator = user)

    def get_absolute_url(self):
        # After update user profile
        return reverse("user_profile", args = [str(self.id)])

    def __str__(self):
        return self.username


# Profile and Friends
class UserConnection(models.Model):
    # A follows B, A is creator, B is following
    creator = models.ForeignKey(InstaUser,
                                on_delete = models.CASCADE,
                                related_name = 'creators')
    following = models.ForeignKey(InstaUser,
                                on_delete = models.CASCADE,
                                related_name = 'followings')
    def __str__(self):
        return self.creator.username + ' follows ' + self.following.username

# Create your models here.
# The (database) table name is Post, which has attribute title and image
# Need the Pillow, which is Python image library
class Post(models.Model):
    author = models.ForeignKey(InstaUser,
                                on_delete = models.CASCADE,
                                related_name = 'insta_posts',
                                blank = True,
                                null = True)
    title = models.TextField(blank = True, null = True)
    # The images are uploaded to file folders, not database
    # Since most databases do not support the format of JPEG, GIF... 
    # May need the complicated way to do serialization
    # Another way is to store inside the application, but takes a lot of memory
    # The optimal way is to upload to CPN, like AWS
    image = ProcessedImageField(
        upload_to = 'static/images/posts',
        format = 'JPEG',
        options = {'quality': 100},
        blank = True,
        null = True,
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # After create one model (like: user press the submit button), need to go to this url
        return reverse("post_detail", args = [str(self.id)])

    def get_like_count(self):
        return self.likes.count()

    def get_comment_count(self):
        return self.comments.count()
    

class Comment(models.Model):
    # The post type is Post.
    # on_delete: If the post has been deleted, comment also should be deleted
    # related_name: used to database query
    post = models.ForeignKey(Post, 
                            on_delete = models.CASCADE, 
                            related_name = 'comments')
    # Who send comments
    user = models.ForeignKey(InstaUser,
                            on_delete = models.CASCADE,
                            related_name = 'comments')
    # The content of comments
    comment = models.CharField(max_length = 140)
    # Record the current time when someone post comments, could not be modified
    posted_on = models.DateTimeField(auto_now_add = True,
                                    editable = False)

    def __str__(self):
        return self.comment 
    
class Like(models.Model):
    post = models.ForeignKey(Post, 
                            on_delete = models.CASCADE, 
                            related_name = 'likes')

    user = models.ForeignKey(InstaUser,
                            on_delete = models.CASCADE,
                            related_name = 'likes')
    class Meta:
        unique_together = ("post", "user")
    
    def __str__(self):
        return 'Like: ' + self.user.username + ' likes ' + self.post.title     

