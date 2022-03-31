from django.db import models

from utils.models import AbstractUUID, AbstractTimeTrackable, AbstractCreatedByTrackable

STATUS = [('1', "Odin"),
          ('2', "Dva"),
          ('3', "Tri")]


class Post(AbstractUUID, AbstractTimeTrackable, AbstractCreatedByTrackable, models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=128, blank=True, null=True)
    status = models.CharField(choices=STATUS, default='1', max_length=2, null=True)

    class Meta:
        verbose_name = "Post"

    @property
    def likes(self):
        return self.grades.filter(is_liked=True).count()

    @property
    def dislikes(self):
        return self.grades.filter(is_liked=False).count()
