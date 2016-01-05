from django.db import models
from django.contrib.auth.models import User

import const

IDEA_STATUS = (
        (0, 'new'),
        (1, 'discussing'),
        (2, 'prototyping'),
        (3, 'alpha'),
        (4, 'beta'),
        (5, 'release'),
        )

class ProfessionType(models.Model):

    TYPES = (
            (0, 'programmer'),
            (1, 'designer'),
            (2, 'ui/ux'),
            (3, 'marketer'),
            (4, 'sales'),
            (5, 'manager'),
            (6, 'other'),
            )

    name = models.IntegerField(choices=TYPES)

class Idea(models.Model):

    idea_status = models.IntegerField(default=0, choices=IDEA_STATUS)
    title = models.CharField(max_length=const.LINE_MAX_LENGTH)
    description = models.TextField(blank=True)

    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User)
    participants = models.ManyToManyField(User, related_name='participate')
    need_help = models.BooleanField(default=True)
    need_profession_types = models.ManyToManyField(ProfessionType, related_name='is_needed_by')

    contact_email = models.EmailField(blank=True)

class ProgressLog(models.Model):

    idea = models.ForeignKey(Idea)
    description = models.TextField(blank=True)

    from_status = models.IntegerField(choices=IDEA_STATUS)
    to_status = models.IntegerField(choices=IDEA_STATUS)

    ctime = models.DateTimeField(auto_now_add=True)
