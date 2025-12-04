from django.shortcuts import render
from .models import Listing
from rest_framework .decorators import action
from rest_framework.response import Response
from .serializers import ListingSerializer
from rest_framework import viewsets, permissions, status



# Create your views here.
