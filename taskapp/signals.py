from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Snippet

@receiver(post_save, sender=Snippet)
def get_sender_email_from_settings(sender, **kwargs):
    print("in receiver")
    obj=kwargs['instance']
    if not obj.title:
        obj.title='Default Title'
