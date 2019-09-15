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


class MatchSerializer(serializers.BaseSerializer):

    class Meta:
        model = Match
        fields = '__all__'

    def to_representation(self, obj):
        fantacyapp = [ {'fantacy_app_name': row.name, 'fantacy_app_id': row.id} for row in obj.fantacyapp.all()]
        return {
            'match_id': obj.id,
            'name': obj.name,
            'power_pics':  obj.power_pics,
            'date': obj.date,
            'sport': obj.sport.name,
            'status': obj.status,
            'team1_name': obj.team1.name,
            'team2_name': obj.team2.name,
            'team1_alias': obj.team1.alias,
            'team2_alias': obj.team2.alias,
            'team1_logo': obj.team1.logo.url,
            'team2_logo': obj.team2.logo.url,
            'fantacyapp': fantacyapp
        }


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
