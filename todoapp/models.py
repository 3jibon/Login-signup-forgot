from django.db import models

# Create your models here.
class Signup(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    pass1 = models.CharField(max_length=128)
    pass2 = models.CharField(max_length=128)
    agreement = models.BooleanField(default=False)

    def __str__(self):
        return self.email
    