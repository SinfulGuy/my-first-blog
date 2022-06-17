from django.core.mail import send_mail
from django.conf import settings
from .models import Post
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=Post)
def create_user(sender, instance=None, created=False, **kwargs):
    if created:
        send_mail('A cool subject', 'A stunning message', settings.EMAIL_HOST_USER, [settings.RECIPIENT_ADDRESS])
