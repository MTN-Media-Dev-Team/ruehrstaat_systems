from django.db import models

from rest_framework_api_key.models import AbstractAPIKey

from carriers.models import Carrier

# Create your models here.


class ApiKey(AbstractAPIKey):
    hasReadAccessTo = models.ManyToManyField(Carrier, blank=True, default=None, related_name="hasReadAccessTo")
    hasReadAccessToAll = models.BooleanField(default=False, null=False, blank=False)
    # field to indicate if key can only be used for specific carrier ids from Carrier model -> ids, default is None which means all carriers
    hasWriteAccessTo = models.ManyToManyField(Carrier, blank=True, default=None, related_name="hasWriteAccessTo")
    hasWriteAccessToAll = models.BooleanField(default=False, null=False, blank=False)


