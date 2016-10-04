from rest_framework.serializers import ModelSerializer
from rest_mouse.models.mouse_model import MouseModel

class MouseSerializer(ModelSerializer):
    class Meta:
        model = MouseModel
        fields = ('method', 'x', 'y')