from rest_framework import serializers
from api.models import ContentTemplate, Team, UserStory, TeamRequest, PrimeRequest, Match, Feedback, FantacySport, FantacyApp
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from django.contrib.postgres.fields import JSONField

class ContentTemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentTemplate
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = '__all__'


class FantacyAppSerializer(serializers.ModelSerializer):

    class Meta:
        model = FantacyApp
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = '__all__'


class FantacySportSerializer(serializers.ModelSerializer):

    class Meta:
        model = FantacySport
        fields = '__all__'

class UserStoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserStory
        fields = '__all__'

class PrimeRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = PrimeRequest
        fields = '__all__'

class GenerateTeamSerializer(serializers.Serializer):
    players = serializers.JSONField()
