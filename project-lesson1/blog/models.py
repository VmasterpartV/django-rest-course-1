from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    PRIVATE = 'PRIVATE'
    PUBLIC = 'PUBLIC'
    TYPE_CHOICES = [
        (PRIVATE, 'Privado'),
        (PUBLIC, 'Público'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(default=PRIVATE, choices=TYPE_CHOICES, max_length=10, blank=True, null=True)
    picture = models.ImageField(upload_to='pictures', blank=True, null=True)

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    message = models.TextField()

    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user