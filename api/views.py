from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from api.serializers import ContentTemplateSerializer, UserStoriesSerializer, PrimeRequestSerializer, FantacySportSerializer, FeedbackSerializer, MatchSerializer, FantacyAppSerializer, TeamSerializer, GenerateTeamSerializer
from api.models import ContentTemplate, Team, UserStory, TeamRequest, PrimeRequest, Match, Feedback, FantacySport, FantacyApp
import datetime
from django.http import JsonResponse

class ContentTemplateListView(ListAPIView):

    serializer_class = ContentTemplateSerializer
    queryset = ContentTemplate.objects.all()


class TeamGetView(RetrieveAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class MatchListView(ListAPIView):
    serializer_class = MatchSerializer
    queryset = Match.objects.filter(status="APPROVED",date__gte=datetime.date.today())


class FantacyAppListView(ListAPIView):
    serializer_class = FantacyAppSerializer
    queryset = FantacyApp.objects.filter(status="ACTIVE")


class FantacySportListView(ListAPIView):

    serializer_class = FantacySportSerializer
    queryset = FantacySport.objects.filter(status="ACTIVE")


class FeedbackCreateView(CreateAPIView):
    serializer_class = FeedbackSerializer


class PrimeRequestCreateView(CreateAPIView):
    serializer_class = PrimeRequestSerializer


class UserStoryCreateView(CreateAPIView):
    serializer_class = UserStoriesSerializer


class GenerateTeamsView(CreateAPIView):
    serializer_class = GenerateTeamSerializer

    def create(self, validated_data):
        print(validated_data.data['players'])
        return JsonResponse({'foo': 'bar'})
