from rest_framework import serializers
from .models import Event, event_category, location_category



class EventSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField() #readOnly so users cant choose
    image = serializers.URLField(default="https://shecodes.com.au/wp-content/uploads/2020/02/Purple_no_circle.svg")
    event_type=serializers.ChoiceField(choices= event_category)
    location=serializers.ChoiceField(choices= location_category)
    description=serializers.CharField()
    start_date = serializers.DateTimeField(read_only=True)
    end_date = serializers.DateTimeField(read_only=True)
    status= serializers.BooleanField(default=True)
    
    def create(self, validated_data):
        return Event.objects.create(**validated_data)

class EventDetailSerializer(EventSerializer):
    # mentor = MentorSerializers(many=True, read_only=True) 

    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.event_type=validated_data.get("event_type", instance.event_type)
        instance.location=validated_data.get("location", instance.location)
        instance.description = validated_data.get('description', instance.description)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance