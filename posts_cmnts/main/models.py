from django.db import models


class NewsPost(models.Model):
    title = models.CharField(verbose_name='title', max_length=255)
    link = models.CharField(verbose_name='link', max_length=255)
    creation_date = models.DateField(verbose_name='creation date')
    amount_of_upvotes = models.IntegerField(verbose_name='amount of upvotes')
    author_name = models.CharField(verbose_name='author name', max_length=255)


class Comment(models.Model):
    author_name = models.CharField(verbose_name='author name', max_length=255)
    content = models.TextField(verbose_name='content')
    creation_date = models.DateField(verbose_name='creation date')
    news_post = models.ForeignKey(NewsPost, verbose_name='news_post', on_delete=models.CASCADE, related_name='comments')
    parent_comment = models.ForeignKey(
        'self', verbose_name="parent comment", on_delete=models.SET_NULL, blank=True, null=True
    )
