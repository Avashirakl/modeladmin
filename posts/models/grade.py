from django.db import models

from utils.models import AbstractUUID, AbstractTimeTrackable, AbstractCreatedByTrackable


class Grade(AbstractUUID, AbstractTimeTrackable, AbstractCreatedByTrackable, models.Model):
    is_liked = models.BooleanField(default=True)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, related_name="grades", blank=True,  null=True)

