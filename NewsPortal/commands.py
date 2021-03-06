from NewsPaper.models import *
user1 = User.objects.create(username='pten4uk', first_name='Nikita')
user2 = User.objects.create(username='den4uk', first_name='Denis')
Author.objects.create(polzovatel=user1)
Author.objects.create(polzovatel=user2)
Category.objects.create(name='категория1')
Category.objects.create(name='категория2')
Category.objects.create(name='категория3')
Category.objects.create(name='категория4')
Post.objects.create(author=Author.objects.get(polzovatel=User.objects.get(username='pten4uk')), _class='A', head='head', text='text')
Post.objects.create(author=Author.objects.get(polzovatel=User.objects.get(username='den4uk')), _class='A', head='head2', text='text2')
Post.objects.create(author=Author.objects.get(polzovatel=User.objects.get(username='pten4uk')), _class='N', head='head', text='text')
p1 = Post.objects.get(pk=1)
p2 = Post.objects.get(pk=2)
p3 = Post.objects.get(pk=3)
cat1 = Category.objects.get(name='категория1')
cat2 = Category.objects.get(name='категория2')
p1.category.add(cat1)
p1.category.add(cat2)
p2.category.add(cat1)
p2.category.add(cat2)
p3.category.add(cat1)
p3.category.add(cat2)
Comment.objects.create(polzovatel=User.objects.get(username='pten4uk'), post=p1, text='классный коммент1')
Comment.objects.create(polzovatel=User.objects.get(username='pten4uk'), post=p1, text='классный коммент2')
Comment.objects.create(polzovatel=User.objects.get(username='den4uk'), post=p2, text='классный коммент2')
Comment.objects.create(polzovatel=User.objects.get(username='den4uk'), post=p3, text='классный коммент2')
p1.like()
p1.like()
p2.like()
p2.like()
p3.dislike()
com1 = Comment.objects.get(pk=1)
com2 = Comment.objects.get(pk=2)
com1.dislike()
com2.like()
Author.objects.get(polzovatel=User.objects.get(username='pten4uk')).update_rating()
Author.objects.get(polzovatel=User.objects.get(username='den4uk')).update_rating()
Author.objects.all().order_by('-rating').values('polzovatel', 'rating')[0]
post = Post.objects.all().order_by('-rating')[0]
print(post.datetime, post.author.polzovatel.username, post.rating, post.text, post.preview())
post.comment_set.values('datetime', 'user__username', 'rating', 'text')