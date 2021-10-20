from posts_cmnts.celery import app
from .models import NewsPost


@app.task
def reset_upvotes():
    news_posts = NewsPost.objects.all()
    for news_post in news_posts:
        setattr(news_post, "amount_of_upvotes", 0)
        news_post.save()

    news_posts = NewsPost.objects.all()
    for news_post in news_posts:
        print(news_post.amount_of_upvotes)

