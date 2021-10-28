from rest_framework import serializers
from .models import Shoe

class ShoeSerializer(serializers.HyperlinkedModelSerializer):
    shoe_url = serializers.ModelSerializer.serializer_url_field(view_name="shoe_detail")

    class Meta:
        model = Shoe
        fields = ("id", "type", "styling", "details", "description", "brand_name", "brand_url", "shoe_url", "photo")