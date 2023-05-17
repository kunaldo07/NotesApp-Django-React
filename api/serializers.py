from rest_framework.serializers import ModelSerializer
from .models import Note

# to convert python object into json format
class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__' # serialize all of the Note fields