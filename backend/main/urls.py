from django.urls import path
from .views import SliderImageApiView

urlpatterns = [path("images/", SliderImageApiView.as_view())]
