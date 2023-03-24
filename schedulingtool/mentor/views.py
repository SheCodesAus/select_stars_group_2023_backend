from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Event, Mentor
from .serializers import EventSerializer,EventDetailSerializer, MentorSerializer, MentorDetailSerializer
from django.http import Http404
from rest_framework import status, generics, permissions
# from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly

# Create your views here.
class EventList(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly] #built in django to allow only logged in
    
    def get(self, request):
        event = Event.objects.all().values()
        if request.data.get("location_category"):
            event = Event.filter(location_category=request.data.get("location_category"))
        if request.data.get("event_category"):
            event = Event.filter(event_category=request.data.get("event_category"))
        serializer = EventSerializer(event, many=True) #get list of many projects not one
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)# use the data that was given from user
        if serializer.is_valid():#built in serializer checks info given is ok, as expected
            serializer.save()
            # serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
class EventDetail(APIView):
    # permission_classes = [
    #     permissions.IsAuthenticatedOrReadOnly,
    #     IsOwnerOrReadOnly
    # ]

    def get_object(self, pk):
        try:
            # return Project.objects.get(pk=pk) #passing the input in as an attribute
            event = Event.objects.get(pk=pk)
            self.check_object_permissions(self.request, event)
            return event
        except Event.DoesNotExist:
            raise Http404 #means resource does not exit, user did something wrong
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = EventDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        event = self.get_object(pk)
        data = request.data
        serializer = EventDetailSerializer(
            instance = event,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
            ####Added what happens if not valid like above

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class MentorList(generics.ListCreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    # permission_classes = [                            
    #     permissions.IsAuthenticatedOrReadOnly
    # ]
    # def perform_create(self, serializer):
    #     serializer.save(supporter=self.request.user)

class MentorDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [                            
    #     permissions.IsAuthenticatedOrReadOnly,
    #     IsSupporterOrReadOnly
    # ]
    queryset = Mentor.objects.all()
    serializer_class = MentorDetailSerializer
