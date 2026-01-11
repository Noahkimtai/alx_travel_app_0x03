from django.db import models
from django.utils import timezone
import uuid


class User(models.Model):
    """Represent a user in the property listing app"""

    ROLE_CHOICES = [
        ("guest", "Guest"),
        ("host", "Host"),
        ("admin", "Admin"),
    ]

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, db_index=True)
    password_hash = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Listing(models.Model):
    """Property listing"""

    class ListingStatus(models.TextChoices):
        AVAILABLE = "Available", "Available"
        OCCUPIED = "Occupied", "Occupied"

    listing_id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    description = models.TextField()
    location = models.CharField(max_length=200)
    price = models.FloatField()
    status = models.CharField(
        max_length=20, choices=ListingStatus.choices, default=ListingStatus.AVAILABLE
    )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.location} - {self.status}"


class Booking(models.Model):
    """Booking for a listing"""

    class BookingStatus(models.TextChoices):
        PENDING = "Pending", "Pending"
        CONFIRMED = "Confirmed", "Confirmed"
        CANCELLED = "Cancelled", "Cancelled"

    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="bookings"
    )
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings"
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(
        max_length=20, choices=BookingStatus.choices, default=BookingStatus.PENDING
    )
    total_price = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.customer} booking for {self.listing}"


class Review(models.Model):
    """Review of a listing"""

    class RatingChoices(models.IntegerChoices):
        ONE = 1, "1"
        TWO = 2, "2"
        THREE = 3, "3"
        FOUR = 4, "4"
        FIVE = 5, "5"

    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name="reviews"
    )
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    comment = models.TextField(blank=True, null=True)
    rating = models.IntegerField(choices=RatingChoices.choices)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review by {self.reviewer} on {self.listing}"
