from django.urls import path
from api.views import ContentTemplateListView, FantacySportListView, FeedbackCreateView, PrimeRequestCreateView, UserStoryCreateView, MatchListView, FantacyAppListView, TeamGetView, GenerateTeamsView

urlpatterns = [
    path('content/', ContentTemplateListView.as_view()),
    path('fantacy-sports/', FantacySportListView.as_view()),
    path('feedback/', FeedbackCreateView.as_view()),
    path('prime-request/', PrimeRequestCreateView.as_view()),
    path('story/', UserStoryCreateView.as_view()),
    path('match/', MatchListView.as_view()),
    path('fantacy-app/', FantacyAppListView.as_view()),
    path('team/<pk>', TeamGetView.as_view()),
    path('request-teams/', GenerateTeamsView.as_view()),
]
