from rest_framework import serializers
from .models import Event,Mentor, event_category, location_category, level_category



class EventSerializer(serializers.ModelSerializer):
    event_type= serializers.ChoiceField(choices=event_category)
    location = serializers.ChoiceField(choices=location_category)
    start_date=serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    end_date=serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Event
        fields =['id','title', 'image', 'event_type', 'location', 'description', 'start_date', 'end_date','status', 'mentors']
        extra_kwargs = {'mentors' : {'required': False}}
        read_only_fields = ['id']
        
    def create(self, validated_data):
        return Event.objects.create(**validated_data)

# class EventSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField() #readOnly so users cant choose
#     image = serializers.URLField(default="https://shecodes.com.au/wp-content/uploads/2020/02/Purple_no_circle.svg")
#     event_type=serializers.ChoiceField(choices= event_category)
#     location=serializers.ChoiceField(choices= location_category)
#     description=serializers.CharField()
#     start_date = serializers.DateTimeField(read_only=True)
#     end_date = serializers.DateTimeField(read_only=True)
#     status= serializers.BooleanField(default=True)
    
#     def create(self, validated_data):
#         return Event.objects.create(**validated_data)
class MentorSerializer(serializers.ModelSerializer):
    level = serializers.ChoiceField(choices=level_category)
    class Meta:
        model = Mentor
        fields = ["id","first_name", "last_name", "email", "bio", "image", "skills", "level",
                   "interview", "offer", "contract_sent", "contract_return",
                  "onboarding_completed", "feedback_sent", "offboarding"]
        extra_kwargs = {'events' : {'required': False}}
        read_only_fields = ['id']


    def create(self, validated_data):          
        
        return Mentor.objects.create(**validated_data)

class EventDetailSerializer(EventSerializer):
    # mentors = MentorSerializer(many=True, read_only=True) 

    def update(self, instance, validated_data):
        instance.image = validated_data.get('image', instance.image)
        instance.event_type=validated_data.get("event_type", instance.event_type)
        instance.location=validated_data.get("location", instance.location)
        instance.description = validated_data.get('description', instance.description)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('start_date', instance.end_date)
        instance.status = validated_data.get('status', instance.status)
        instance.mentors = validated_data.get('mentors', instance.mentors)
        instance.save()
        return instance
    
class MentorDetailSerializer(MentorSerializer):
    events = EventSerializer(many=True)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.image = validated_data.get('image', instance.image)
        instance.skills = validated_data.get('skills', instance.skills)
        instance.level = validated_data.get('level', instance.level) 
        instance.interview = validated_data.get('interview', instance.interview)
        instance.offer = validated_data.get('offer', instance.offer)
        instance.contract_sent = validated_data.get('contract_sent', instance.contract_sent)
        instance.contract_return = validated_data.get('contract_return', instance.contract_return) 
        instance.onboarding_completed = validated_data.get('onboarding_completed', instance.onboarding_completed)
        instance.feedback_sent = validated_data.get('feedback_sent', instance.feedback_sent)
        instance.offboarding = validated_data.get('offboarding', instance.offboarding)
        instance.save()
        return instance
    
