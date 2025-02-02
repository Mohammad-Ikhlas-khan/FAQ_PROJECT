from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import FAQ

@receiver(post_save, sender=FAQ)
def clear_faq_cache(sender, **kwargs):
    for lang in ['en', 'hi', 'bn']:
        cache.delete(f'faqs_{lang}')