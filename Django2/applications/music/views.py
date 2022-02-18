from rest_framework import generics

from .models import Music
from .serializers import *


class MusicListView(generics.ListAPIView):

    queryset = Music.objects.all()
    serializer_class = MusicSerializer