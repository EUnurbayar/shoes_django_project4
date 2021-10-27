from rest_framework import generics
from .models import Shoe
from .serializers import ShoeSerializer
# Create your views here.

class ShoeList(generics.ListCreateAPIView):
    queryset = Shoe.objects.all()
    serializers_class = ShoeSerializer

class ShoeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shoe.objects.all()
    serializers_class = ShoeSerializer