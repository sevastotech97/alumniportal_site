from django.db import models

class Programs(models.Model):
    name = models.CharField(max_length=250)
    program_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.program_logo+' - '+ self.name

class Alumni_Prof(models.Model):
    grad_year = models.DateField(blank=True, null=True)
    publication = models.DateField()
    programs = models.ForeignKey(Programs, on_delete=models.CASCADE)