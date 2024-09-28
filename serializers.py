from rest_framework import serializers
from movie_app.models import CineProfessional
class CineProfessionalSerializer (serializers.Serializer):
    id= serializers. IntegerField(read_only=True)
    name =serializers.CharField(max_length=200)
    profile = serializers.CharField()
    date_of_birth = serializers.DateField (required=False)
    class Meta:
        fields = ['id', 'name', 'profile', 'date of_birth']

    def create(self, validated_data) :
        return CineProfessional.objects.create(**validated_data)