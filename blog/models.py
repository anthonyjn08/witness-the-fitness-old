from django.db import models
from trainers.models import Trainers
from django.utils.text import slugify

from profiles.models import UserProfile

slug = models.SlugField()

STATUS = ((0, "Draft"), (1, "Published"))


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(Trainers, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now=True)
    featured_image = models.ImageField(default="blog_placeholder")
    excerpt = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(UserProfile, related_name="post_likes", blank=True)

    def __str__(self):
        return self.title
