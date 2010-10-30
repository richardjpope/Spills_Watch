from django.db import models

class Company(models.Model):

    name = models.CharField(max_length = 100, null=False, blank=False)

    def __unicode__(self):
        return self.name

class Incident(models.Model):

        title = models.CharField(max_length = 100, null=True, blank=True)
        description = models.TextField(max_length = 300, null=True, blank=True)
        action_taken = models.TextField(max_length = 300, null=True, blank=True)        
        incident_date = models.DateTimeField(null=True, blank=True)                        
        reported_date = models.DateTimeField(null=True, blank=True)        
        location = models.CharField(max_length = 100, null=False, blank=False)        
        lat = models.FloatField(null=True, blank=True, verbose_name='Latitude of incident', help_text="as a decimal number")
        lng = models.FloatField(null=True, blank=True, verbose_name='Longitude of incident', help_text="as a decimal number")
        medium = models.CharField(max_length = 100, null=False, blank=False)        
        fatality_count = models.IntegerField(null=True, blank=True,)
        injury_count = models.IntegerField(null=True, blank=True,)
        hospitalised_count = models.IntegerField(null=True, blank=True,)
        company = models.ForeignKey(Company, null=True, blank=True,)        