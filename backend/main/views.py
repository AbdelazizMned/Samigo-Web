from django.shortcuts import render
from .serializers import SliderSerializer
from .models import SliderImage
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class SliderImageApiView(APIView):
    def get(self, request, *args, **kwargs):
        images = SliderImage.objects.all()
        serializer = SliderSerializer(images, context={"request": request}, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
