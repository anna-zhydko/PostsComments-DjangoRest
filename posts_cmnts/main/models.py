from django.db import models


class Post(models.Model):
    title = models.CharField(verbose_name='title', max_length=255)
    link = models.CharField(verbose_name='link', max_length=255)
    creation_date = models.DateField(verbose_name='creation date')
    upvotes = models.IntegerField(verbose_name='amount of upvotes')
    author = models.CharField(verbose_name='author name', max_length=255)


class Comment(models.Model):
    author = models.CharField(verbose_name='author name', max_length=255)
    content = models.TextField(verbose_name='content')
    creation_date = models.DateField(verbose_name='creation date')
    post = models.ForeignKey(Post, verbose_name='post', on_delete=models.CASCADE)