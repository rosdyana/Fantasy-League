from django.db import models

class Match(models.Model):
    match_id = models.IntegerField(max_length=32,
                                   default='')
    home_team = models.CharField(max_length=32)
    away_team = models.CharField(max_length=32)
    home_goal = models.IntegerField()
    away_goal = models.IntegerField()

    def __int__(self):
        return "%d" % self.match_id

class Player(models.Model):
    player_name = models.CharField(max_length=32, default='')
    player_number = models.IntegerField()
    player_team = models.CharField(max_length=32)
    player_scoring = models.IntegerField()
    player_assist = models.IntegerField()
    player_minutes = models.IntegerField()
    match_id = models.ForeignKey(Match.__name__,
                                 default='')

class GoalKeeper(models.Model):
    player_name = models.ForeignKey(Player.__name__,
                                    default='')
    gk_saves = models.IntegerField()
    is_gk = models.BooleanField()

    def __str__(self):
        return "%d %d" % (self.gk_saves, self.is_gk)

class Defender(models.Model):
    player_name = models.ForeignKey(Player.__name__,
                                    default='')
    is_defender = models.BooleanField()

    def __str__(self):
        return '%d' % self.is_defender

class Midfielder(models.Model):
    player_name = models.ForeignKey(Player.__name__,
                                    default='')
    is_midfielder = models.BooleanField()

    def __str__(self):
        return '%d' % self.is_midfielder

class Attacker(models.Model):
    player_name = models.ForeignKey(Player.__name__,
                                    default='')
    is_attacker = models.BooleanField()

    def __str__(self):
        return '%d' % self.is_attacker


