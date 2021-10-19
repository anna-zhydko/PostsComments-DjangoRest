from django.urls import path, include

from . import views


urlpatterns = [
    path("news/", views.NewsPostListView.as_view()),
    path("news/new/", views.NewsPostCreateView.as_view()),
    path("news/<int:pk>/", views.NewsPostDetailView.as_view()),
    path("news/<int:pk>/update", views.NewsPostUpdateView.as_view()),
    path("comments/", views.CommentListView.as_view()),
    path("comments/new/", views.CommentCreateView.as_view()),
    path("comments/<int:pk>/", views.CommentDetailView.as_view()),
    path("comments/<int:pk>/update", views.CommentUpdateView.as_view()),
    path("upvote/", views.UpvoteView.as_view()),
]
