from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from events.models import Event
from django.contrib.auth import get_user_model

 
User = get_user_model()

@receiver(post_save, sender=User)
def send_activation_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Welcome!',
            'Thanks for signing up!',
            'adnnn336@gmail.com',
            [instance.email],
            fail_silently=False,
        )
        print(f"Welcome email sent to {instance.email}")

@receiver(m2m_changed, sender=Event.participants.through)
def send_rsvp_email(sender, instance, action, pk_set, **kwargs):
    if action == 'post_add':
        for user_id in pk_set:
            user = User.objects.get(id=user_id)
            send_mail(
                subject=f"RSVP Confirmation for {instance.title}",
                message=f"Hello {user.username},\n\nYou have successfully RSVP'd to {instance.title}.",
                from_email='admin@example.com',
                recipient_list=[user.email],
            )
