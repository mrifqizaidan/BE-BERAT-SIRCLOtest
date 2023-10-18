from django.db import models

class WeightRecord(models.Model):
    date = models.DateField()
    max_weight = models.DecimalField(max_digits=5, decimal_places=2)
    min_weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Berat Badan pada {self.date}"

    @property
    def differences(self):
        return self.max_weight - self.min_weight
