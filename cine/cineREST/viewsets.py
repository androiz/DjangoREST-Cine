from cineREST.serializers import FilmSerializer
from cineREST.models import Film

from rest_framework import viewsets

# ViewSets define the view behavior.


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer