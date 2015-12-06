from serializers import *
from rest_framework import viewsets


# ViewSets define the view behavior.
class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer