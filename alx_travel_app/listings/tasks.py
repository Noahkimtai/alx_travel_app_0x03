from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=30, retry_kwargs={"max_retries": 3})
def send_booking_confirmation_email(self, recipient_email, booking_id):
    """
    Send booking confirmation email asynchronously.
    Uses Django's configured email backend.
    """

    subject = "Booking Confirmation"
    message = f"Your booking (ID: {booking_id}) has been successfully created."
    from_email = settings.DEFAULT_FROM_EMAIL

    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=[recipient_email],
        fail_silently=False,
    )
