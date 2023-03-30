from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event, Mentor, Tech_Stack
from .serializers import EventSerializer, MentorSerializer, Tech_StackSerialiser
from django.http import Http404
from rest_framework import status, generics, permissions


# Create your views here.

class Tech_StackList(generics.ListCreateAPIView):
    queryset = Tech_Stack.objects.all()
    serializer_class = Tech_StackSerialiser
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class Tech_StackDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Tech_Stack.objects.all()
    serializer_class = Tech_StackSerialiser

# class EventList(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly] #built in django to allow only logged in
    
#     def get(self, request):
#         event = Event.objects.all().values()
#         if request.data.get("location_category"):
#             event = Event.filter(location_category=request.data.get("location_category"))
#         if request.data.get("event_category"):
#             event = Event.filter(event_category=request.data.get("event_category"))
#         serializer = EventSerializer(event, many=True) #get list of many projects not one
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = EventSerializer(data=request.data)# use the data that was given from user
#         if serializer.is_valid():#built in serializer checks info given is ok, as expected
#             serializer.save()
#             # serializer.save(owner=request.user)
#             return Response(
#                 serializer.data,
#                 status=status.HTTP_201_CREATED
#                 )
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )
# class EventDetail(APIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get_object(self, pk):
#         try:
#             event = Event.objects.get(pk=pk)
#             self.check_object_permissions(self.request, event)
#             return event
#         except Event.DoesNotExist:
#             raise Http404 #means resource does not exit, user did something wrong

class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
        
    # def create(self, request, *args, **kwargs):
    #     data = request.data

    #     new_event = Event.objects.create(
    #     title=data["title"],image=data["image"],event_type=data["event_type"],
    #     location=data["location"],description=data["description"],start_date=data["start_date"],
    #     end_date=data["end_date"])
           

    #     new_event.save()

    #     for mentor in data["mentors"]:
    #         mentor_obj = Mentor.objects.get(first_name=mentor["first_name"])
    #         new_event.mentors.add(mentor_obj)

    #     serializer = EventSerializer(new_event)

    #     return Response(serializer.data)
    
    
    # def update(self,request, *args, **kwargs):
    #     data=request.data

    #     updated_event = Event.objects.set(title=data["title"],image=data["image"],event_type=data["event_type"],
    #     location=data["location"],description=data["description"],start_date=data["start_date"],
    #     end_date=data["end_date"])

    #     updated_event.save()

    #     for mentor in data["mentors"]:
    #         mentor_obj= Mentor.objects.update(first_name=mentor["first_name"])
    #         updated_event.mentors.add(mentor_obj)

    #     serializer = EventSerializer(updated_event)
    #     return Response(serializer.data)

        
    
class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
#     def get(self, request, pk):
#         event = self.get_object(pk)
#         serializer = EventDetailSerializer(event)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         event = self.get_object(pk)
#         data = request.data
#         serializer = EventDetailSerializer(
#             instance = event,
#             data=data,
#             partial=True
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST
#         )
#             ####Added what happens if not valid like above

#     def delete(self, request, pk, format=None):
#         event = self.get_object(pk)
#         event.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
class MentorList(generics.ListCreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   
    # def create(self, request, *args, **kwargs):
    #     data = request.data

    #     new_mentor = Mentor.objects.create(
    #     first_name=data["first_name"],last_name=data["last_name"],email=data["email"],bio=data["bio"],image=data["image"],skills=data["skills"],level=data["level"],interview=data["interview"],offer=data["offer"],contract_sent=data["contract_sent"],contract_return=data["contract_return"],onboarding_completed=data["onboarding_completed"],feedback_sent=data["feedback_sent"],offboarding=data["offboarding"])
           

    #     new_mentor.save()

    #     for event in data["events"]:
    #         event_obj = Event.objects.get(event_type=event["event_type"])
    #         new_mentor.events.add(event_obj)

    #     serializer = MentorSerializer(new_mentor)

    #     return Response(serializer.data)

class MentorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    
    

        
   

   
