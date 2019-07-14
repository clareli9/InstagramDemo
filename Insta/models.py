from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField

from django.contrib.auth.models import AbstractUser

# Create your models here.
# The (database) table name is Post, which has attribute title and image
# Need the Pillow, which is Python image library
class Post(models.Model):
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
    
class InstaUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to = 'static/images/profiles',
        format = 'JPEG',
        options = {'quality': 100},
        null = True,
        blank = True,
    )