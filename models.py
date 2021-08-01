from django.db import models
from django.contrib.auth.models import AbstractUser


class Author:
    user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self, rating):
        pass



class Category:
    name = models.CharField(max_length=32, unique=True)


class Post:
    article = 'A'
    news = 'N'
    CLASSES = [
        (article, 'Статья'),
        (news, 'Новость')
    ]
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    _class = models.CharField(max_length=1, choices=CLASSES)
    datetime = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through='PostCategory')
    head = models.CharField(max_length=256)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1

    def preview(self):
        return self.text[:124] + '...'


class PostCategory:
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment:
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(AbstractUser, on_delete=models.CASCADE)
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1

    def dislike(self):
        self.rating -= 1
