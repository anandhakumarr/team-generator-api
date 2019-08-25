from django.db import models
from django.contrib.postgres.fields import JSONField
from PIL import Image

class ContentTemplate(models.Model):
    template_name = models.CharField(max_length=250, blank=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.template_name


class FantacyApp(models.Model):
    name = models.CharField(max_length=250, blank=False)
    CHOICES = (
        ("ACTIVE", "active"),
        ("INACTIVE", "inactive"),
    )
    status = models.CharField(max_length=10, choices=CHOICES, default='INACTIVE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class FantacySport(models.Model):
    name = models.CharField(max_length=250, blank=False)
    CHOICES = (
        ("ACTIVE", "active"),
        ("INACTIVE", "inactive"),
    )
    status = models.CharField(max_length=10, choices=CHOICES, default='INACTIVE')
    skills = models.CharField(max_length=250, blank=False)
    fantacy_rules = JSONField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=250, blank=False)
    alias = models.CharField(max_length=250, blank=False)
    logo = models.ImageField(upload_to = 'media/team/pics', default = 'media/default/team.png')
    sport = models.ForeignKey(FantacySport, on_delete=models.CASCADE)
    players_details = JSONField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.alias + ' - ' + self.name

    def save(self):
        if not self.logo:
            return
        super(Team, self).save()
        image = Image.open(self.logo)
        (width, height) = image.size
        size = ( 250, 250)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.logo.path)


class Match(models.Model):
    name = models.CharField(max_length=250, blank=False)
    power_pics = models.CharField(max_length=250)
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2')
    date = models.DateField(blank=False)
    CHOICES = (
        ("PENDING", "pending"),
        ("APPROVED", "approved"),
        ("REJECTED", "rejected"),
    )
    status = models.CharField(max_length=10, choices=CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, blank=False)
    subject = models.CharField(max_length=250, blank=False)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class PrimeRequest(models.Model):
    name = models.CharField(max_length=250, blank=False)
    email = models.EmailField(max_length=250, blank=False)
    phone = models.CharField(max_length=250, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=250, blank=False)
    sport = models.ForeignKey(FantacySport, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'media/player/pics', default = 'media/default/male.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - ' + self.sport.name

    def save(self):
        if not self.image:
            return
        super(Player, self).save()
        image = Image.open(self.image)
        (width, height) = image.size
        size = ( 250, 250)
        image = image.resize(size, Image.ANTIALIAS)
        image.save(self.image.path)

class TeamRequest(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    mustpicks = models.TextField()
    teamsgenerated = models.IntegerField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserStory(models.Model):
    title = models.CharField(max_length=250, blank=False)
    username = models.CharField(max_length=250, blank=False)
    content = models.TextField()
    storydate = models.DateField()
    STORYCHOICES = (
        ("PENDING", "pending"),
        ("APPROVED", "approved"),
        ("REJECTED", "rejected"),
    )
    status = models.CharField(max_length=10, choices=STORYCHOICES, default='PENDING')
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
