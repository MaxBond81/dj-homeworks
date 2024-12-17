from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="measurements")
    image = models.ImageField(blank=True, null=True)

