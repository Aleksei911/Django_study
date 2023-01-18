from django.db import models


# Create your models here.
class Device(models.Model):
    serial_number = models.CharField(max_length=20)
    device_name = models.CharField(max_length=50)
    model_name = models.ForeignKey('Device_model', on_delete=models.CASCADE)
    create_date = models.DateTimeField()
    added_date = models.DateTimeField(auto_now_add=True)
    color = models.ForeignKey('Device_color', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    count = models.IntegerField()
    characteristic = models.CharField(max_length=255)
    cargo_code = models.CharField(max_length=50)
    publication = models.BooleanField()
    manufacturer = models.ForeignKey('Device_manufacturer', on_delete=models.CASCADE)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.device_name


class Device_model(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Device_color(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Device_manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
