from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import SliderImage


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderImage
        fields = "__all__"

        def get_photo_url(self, obj):
            request = self.context.get("request")
            photo_url = obj.fingerprint.url
            return request.build_absolute_uri(photo_url)
