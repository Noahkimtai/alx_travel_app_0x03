import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from listings.models import User, Listing, Booking, Review


class Command(BaseCommand):
    help = "Seed the database with sample data for testing"

    def handle(self, *args, **options):
        self.stdout.write("Seeding database...")

        # --- USERS ---
        users = []
        roles = ["guest", "host", "admin"]
        for i in range(5):
            user = User.objects.create(
                first_name=f"User{i}",
                last_name=f"Test{i}",
                email=f"user{i}@example.com",
                password_hash="hashed_password",
                phone_number=f"+100000000{i}",
                role=random.choice(roles),
            )
            users.append(user)
        self.stdout.write(f"Created {len(users)} users")

        # --- LISTINGS ---
        listings = []
        for i in range(5):
            listing = Listing.objects.create(
                host=random.choice(users),
                description=f"Listing description {i}",
                location=f"City {i}",
                price=random.randint(50, 500),
                status=random.choice(
                    [Listing.ListingStatus.AVAILABLE, Listing.ListingStatus.OCCUPIED]
                ),
            )
            listings.append(listing)
        self.stdout.write(f"Created {len(listings)} listings")

        # --- BOOKINGS ---
        bookings = []
        for i in range(5):
            listing = random.choice(listings)
            customer = random.choice(users)
            booking = Booking.objects.create(
                listing=listing,
                customer=customer,
                start_date=timezone.now(),
                end_date=timezone.now() + timezone.timedelta(days=random.randint(1, 7)),
                status=random.choice(
                    [Booking.BookingStatus.PENDING, Booking.BookingStatus.CONFIRMED]
                ),
                total_price=listing.price * random.randint(1, 7),
            )
            bookings.append(booking)
        self.stdout.write(f"Created {len(bookings)} bookings")

        # --- REVIEWS ---
        reviews = []
        for i in range(5):
            review = Review.objects.create(
                listing=random.choice(listings),
                reviewer=random.choice(users),
                comment=f"This is review {i}",
                rating=random.randint(1, 5),
            )
            reviews.append(review)
        self.stdout.write(f"Created {len(reviews)} reviews")

        self.stdout.write(self.style.SUCCESS("Seeding complete!"))
