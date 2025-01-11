from django.db import models

# Create your models here.
class Student(models.Model):
      name=models.CharField(max_length=100)
      college=models.CharField(max_length=50)
      Age=models.CharField(max_length=10)
      is_active=models.BooleanField(default=False)

      def __str__(self):
        return self.name