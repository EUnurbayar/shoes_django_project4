from rest_framework import serializers
from .models import Shoe

class ShoeSerializer(serializers.HyperlinkedModelSerializer):
    # shoe_url = serializers.ModelSerializer.serializer_url_field(view_name="shoe_detail")

    class Meta:
        model = Shoe
        fields = '__all__'
        
        # fields = ("id", "type", "styling", "image", "details", "description", "brand_name", "brand_url")