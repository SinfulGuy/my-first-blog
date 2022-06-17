from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    dislikes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


@receiver(post_save, sender=Post)
def create_user(sender, instance=None, created=False, **kwargs):
    if created:
        send_mail(f'New post available by {instance.author}',
                  f'title: {instance.title} \ntext: {instance.text}',
                  settings.EMAIL_HOST_USER,
                  [settings.RECIPIENT_ADDRESS]
                  )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
