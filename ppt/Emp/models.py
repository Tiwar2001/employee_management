from django.db import models

# Create your models here.
class emp(models.Model):
    name=models.CharField(max_length=10)
    emp_mail=models.CharField( max_length=254)
    status=models.BooleanField(default=True)
    department=models.CharField( max_length=50)
    address=models.CharField(max_length=150)
    phone_number=models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    name=models.CharField(max_length=50)
    testimonials=models.TextField()
    picture=models.ImageField(upload_to='testimonials/')    
    rating=models.IntegerField(max_length=1)
    

    def __str__(self):
        return self.name