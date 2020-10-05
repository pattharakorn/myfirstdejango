from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()


class Post(models.Model):
    topic = models.TextField()
    date = models.DateField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)