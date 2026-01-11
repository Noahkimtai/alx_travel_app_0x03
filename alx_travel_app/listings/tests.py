from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from models import User, Listing, Booking, Review

# Create your tests here.
class ListingsTest(TestCase):

    def test_something(self):
        self.assertEqual(True)


class ListingTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('listing')
        self.listing_instance = Listing.objects.create()
        

    def test_get_listings_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

    def test_create_list_item(self):
        data = {}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
