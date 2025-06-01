"""View module for handling requests about event gamers"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import EventGamer, Gamer, Event


class EventGamerView(ViewSet):
    """Level up event gamer view"""

    def list(self, request):
        """Handle GET requests to get all event gamers

            Returns:
                Response -- JSON serialized list of event gamers
            """
        event_gamers = EventGamer.objects.all()
        serializer = EventGamerSerializer(event_gamers, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST requests for events

        Returns -- JSON serialized event instance
        """
        event = Event.objects.get(pk=request.data["event"])
        gamer = Gamer.objects.get(pk=request.data["gamer"])

        event = Event.objects.create(
            description=request.data["description"],
            date=request.data["date"],
            time=request.data["time"],
            event=event,
            gamer=gamer
        )
        serializer = EventSerializer(event)
        return Response(serializer.data)


class EventGamerSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = EventGamer
        fields = ('id', 'gamer', 'event')
