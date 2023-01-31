from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    CATEGORY = [
        ('TP', '팀플'),
        ('EX', '공모전'),
        ('AC', '대외활동'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=2, choices=CATEGORY)
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(blank=True, null=True, upload_to='post_photo')

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    secret = models.BooleanField(default=False)

    def __str__(self):
        return self.comment