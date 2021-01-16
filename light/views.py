from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView


from .models import LightSample
from .serializer import LightSerializer

# Create your views here.


class MainLight(ListAPIView):
    queryset = LightSample.objects.all()
    serializer_class = LightSerializer

class DetailsLight(RetrieveUpdateDestroyAPIView):
    queryset = LightSample.objects.all()
    serializer_class = LightSerializer
