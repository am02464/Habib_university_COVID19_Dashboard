from django.db import models

province_choices = [("SINDH", "Sindh"), ("PUNJAB", "Punjab")]

# Create your models here.
class Daily_Cases(models.Model):
    province = models.CharField(choices=province_choices, max_length=20)
    date = models.DateField( auto_now=False, auto_now_add=False)
    total_suspected = models.IntegerField(default=0)
    total_tested = models.IntegerField(default=0)
    total_tested_positive = models.IntegerField(default=0)
    total_tested_negative = models.IntegerField(default=0)
    total_admitted = models.IntegerField(default=0)
    total_discharged = models.IntegerField(default=0)
    total_died = models.IntegerField(default=0)


    class Meta:
        verbose_name = "Daily Cases"
        verbose_name_plural = "Daily Cases"
        unique_together = ("date", "province")
        

    def __str__(self):
        return f"Record of {self.province} on {self.date}"


