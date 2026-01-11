from django.urls import path, include
from rest_framework import routers

from .views import (
    BookingViewset,
    ListingViewset,
    ReviewViewset,
    UserViewset,
)


router = routers.DefaultRouter()
# router.register("authi", ExampleAuthView, basename="example")// DefaultRouter only works with ViewSets
router.register("bookings", BookingViewset, basename="booking")
router.register("listing", ListingViewset, basename="listing")
router.register("reviews", ReviewViewset, basename="review")
router.register("users", UserViewset, basename="user")
urlpatterns = [
    path("", include(router.urls)),
]
