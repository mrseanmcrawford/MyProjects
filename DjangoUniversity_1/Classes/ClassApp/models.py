from django.db import models

class DjangoClasses(models.Model):
   course = models.CharField(max_length=60, default="", blank=True,)
   name = models.CharField(max_length=60, default="", blank=True, null=False)
   Instructor = models.CharField(max_length=60, default="", blank=True, null=False)
   Duration = models.DecimalField(max_length=300, max_digits=5, default="0.00", blank=True, decimal_places=2)

   objects = models.Manager()

   def __str__(self):
        return self.name