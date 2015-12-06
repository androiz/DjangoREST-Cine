from cineREST.models import Film

from rest_framework import serializers

# Serializers define the API representation.
class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ('url', 'url_img', 'title')