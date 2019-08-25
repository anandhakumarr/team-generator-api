from django.contrib import admin
from api.models import ContentTemplate, Team, UserStory, TeamRequest, PrimeRequest, Match, FantacyApp, FantacySport, Feedback, Player
from django.contrib.postgres import fields
from django_json_widget.widgets import JSONEditorWidget

class TeamAdmin(admin.ModelAdmin):
    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
    }

class FantacySportAdmin(admin.ModelAdmin):
    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
    }

admin.site.register(FantacyApp)
admin.site.register(FantacySport, FantacySportAdmin)
admin.site.register(Match)
admin.site.register(Team, TeamAdmin)
admin.site.register(ContentTemplate)
admin.site.register(PrimeRequest)
admin.site.register(TeamRequest)
admin.site.register(UserStory)
admin.site.register(Feedback)
admin.site.register(Player)
