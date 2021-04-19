from django.db import models

# The IT-Equipment class.
class Equipment(models.Model):
    name = models.TextField(blank=False, null=False)
    issued = models.BooleanField(default=False, blank=False, null=False)
    requests = models.IntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.name
    