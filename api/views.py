from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from api.serializers import ContentTemplateSerializer, UserStoriesSerializer, PrimeRequestSerializer, FantacySportSerializer, FeedbackSerializer, MatchSerializer, FantacyAppSerializer, TeamSerializer, GenerateTeamSerializer
from api.models import ContentTemplate, Team, UserStory, TeamRequest, PrimeRequest, Match, Feedback, FantacySport, FantacyApp
import datetime
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from api.rules import generate_teams

class ContentTemplateListView(ListAPIView):

    serializer_class = ContentTemplateSerializer
    queryset = ContentTemplate.objects.all()


class TeamGetView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class MatchListView(ListAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = MatchSerializer
    queryset = Match.objects.filter(date__gte=datetime.date.today())


class FantacyAppListView(ListAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = FantacyAppSerializer
    queryset = FantacyApp.objects.filter(status="active")


class FantacySportListView(ListAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = FantacySportSerializer
    queryset = FantacySport.objects.filter(status="active")


class FeedbackCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = FeedbackSerializer


class PrimeRequestCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = PrimeRequestSerializer


class UserStoryCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = UserStoriesSerializer


class GenerateTeamsView(CreateAPIView):
    permission_classes = [IsAuthenticated]

    serializer_class = GenerateTeamSerializer

    def create(self, validated_data):
        return generate_teams(validated_data.data)
