
from django.db import models
from django.db.models import Q


class Music(models.Model):
    song = models.TextField()  # blank=False
    singer = models.TextField()  # blank=False
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    # setting auto_now or auto_now_add to True will cause the field to have editable=False and blank=True set.
    last_modify_date = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        db_table = "music"


