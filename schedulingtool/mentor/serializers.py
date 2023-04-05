from rest_framework import serializers
from .models import Event,Mentor, event_category, location_category, level_category, Tech_Stack, Onboarding
from user.serializers import CustomUserSerializer
        


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

class Tech_StackSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Tech_Stack
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    event_type= serializers.ChoiceField(choices=event_category)
    location = serializers.ChoiceField(choices=location_category)
    start_date=serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    end_date=serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Event
        fields =['id','title', 'image', 'event_type', 'location', 'description', 'start_date', 'end_date','status', 'mentors', 'event_tech_stack']
        extra_kwargs = {'mentors' : {'required': False}, 'event_tech_stack' : {'required': False}, 'tech_mentor' : {'required': False} }
        read_only_fields = ['id']


class OnboardingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onboarding
        fields = '__all__'
        extra_kwargs = {'interview':{'required': False}, 'offer':{'required': False}, 
                        'contract_sent':{'required': False}, 'contract_return':{'required': False}, 
                        'onboarding_completed':{'required': False}, 'feedback':{'required': False}, 
                        'offboarding':{'required': False}, 'event':{'required': False}, 'mentor':{'required': False}}
        # fields = ['id', 'interview', 'offer', 'contract_sent', 'contract_return', 'onboarding_completed', 'feedback', 'offboarding']
        read_only_fields = ['id']


    
class MentorSerializer(serializers.ModelSerializer):
    level = serializers.ChoiceField(choices=level_category)
    events = OnboardingSerializer(many=True, source="onboardings", read_only=True)
    onboarding = OnboardingSerializer(many=True, read_only=True) 
    
    # interview_user = CustomUserSerializer(many=True, read_only=True)

    class Meta:
        model = Mentor
        # fields = '__all__'
        fields = ["id","first_name", "last_name", "email", "bio", "image", "mentor_tech_stack", "level", "location", "can_travel", 'onboarding', 'events']
        extra_kwargs = { 'events_tech' : {'required':False}, 'mentor_tech_stack' : {'required': False}}
        read_only_fields = ['id', 'onboarding', 'events']

    
