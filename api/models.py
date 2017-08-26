from django.db import models

class Player(models.Model):
    player_name = models.CharField(max_length=32)
    player_number = models.IntegerField()
    player_team = models.CharField(max_length=32)
    player_scoring = models.IntegerField()
    player_assist = models.IntegerField()
    player_minutes = models.IntegerField()

class GoalKeeper(models.Model):
    gk_saves = models.IntegerField()
    is_gk = models.BooleanField()

class Defender(models.Model):
    is_defender = models.BooleanField()


