from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# brand
class Brand(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name

# car 
class Car(models.Model):
    title = models.CharField(max_length=500)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='car_images/')
    quantity = models.IntegerField()
    color = models.CharField(max_length=300)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="brand")

    def __str__(self) -> str:
        return f"{self.title} {self.price}"

# comment
class Comment(models.Model):
    name = models.CharField(max_length=500)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE,related_name="car_comment")

    def __str__(self) -> str:
        return self.name


# order
class Orders(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="car")

    def __str__(self) -> str:
        return f"{self.user.username} - {self.car.title}"
