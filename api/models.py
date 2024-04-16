from django.db import models

class Country(models.Model):

    Country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=3)
    description = models.TextField(max_length=50)
    logo_url = models.URLField()
    status = models.BooleanField()



    def __str__(self):
        return self.country_name
    