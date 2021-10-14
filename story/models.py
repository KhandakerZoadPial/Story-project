from django.db import models
from django.contrib.auth.models import User

# ckeditor imports
from ckeditor.fields import RichTextField


# Create your models here.
class Stroy(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    story_name = models.CharField(max_length=100)
    the_story = models.TextField()
    story_picture = models.ImageField(upload_to='media/story_img', null=True, blank=True)

    def __str__(self):
        return self.story_name


class User_profile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.IntegerField(default=0) #0=None, 1=male, 2=female
    type = models.IntegerField(default=0) #0=None, 1=Father, 2=Mother, 3=Grandparents


class Question(models.Model):
    question_for = models.ForeignKey(User_profile, on_delete=models.CASCADE)
    the_question = models.TextField()
