from rest_framework import serializers

class FeatureSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    status = serializers.BooleanField(default=True)
    
    from rest_framework import serializers

class InfoSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=200)
    status = serializers.BooleanField()