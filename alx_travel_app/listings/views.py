from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User, Listing, Booking, Review
from .serializers import (
    UserSerializer,
    ListingSerializer,
    BookingSerializer,
    ReviewSerializer,
)


class UserViewset(viewsets.ModelViewSet):
    "Manage property listing"

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListingViewset(viewsets.ModelViewSet):
    "Manage property listing"

    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewset(viewsets.ModelViewSet):
    "Manage booking listing"

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class ReviewViewset(viewsets.ModelViewSet):
    "Manage reviews listing"

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
