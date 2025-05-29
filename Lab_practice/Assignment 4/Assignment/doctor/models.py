from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    specialty = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to='doctors/', blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    discription = models.TextField(blank=True, null=True)
    fees = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.specialty}"

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
        ordering = ['name']


 