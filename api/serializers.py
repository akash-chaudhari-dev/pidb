from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    html_file = serializers.FileField(required=False, allow_null=True)
    
    class Meta:
        model = Item
        fields = '__all__'
    
    def validate_html_file(self, value):
        if value is not None:
            if not value.name.endswith('.html'):
                raise serializers.ValidationError("Only .html files are allowed.")
        return value
