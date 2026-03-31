
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

# Kada se BILO STA upise u bazu  -> salje se signal post_save
# Mi hocemo da uhvatimo kada se desi POST SAVE ali na USERS tabeli
    # -> post_save na USERS to znaci da je kreiran novi korisnik u tabeli users
    # -> U tom trenutku napravimo i njegov profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, user_type='driver')