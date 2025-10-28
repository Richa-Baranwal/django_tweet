from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVarity(models.Model):

    CHAI_TYPE_CHOICES = [
        ('ML', 'MASALA'),
        ('CL', 'CLASSIC'),
        ('HL', 'HONEY'),
        ('GR', 'GINGER'),
        ('SL', 'SPECIAL'),
        ('KW', 'KASHMIRI'),
        ('KT', 'KIWI'),
        ('LT', 'LEMON'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICES, default='CL')
    description = models.TextField(default='')

    def __str__(self):
        return self.name
    

#one to many relationship
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete= models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Review of {self.chai.name} by {self.user.username}'
    
# many to many relationship
class ChaiStore(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    chai_varieties = models.ManyToManyField(ChaiVarity, related_name='stores') 

    def __str__(self):
        return self.name
    
#one to one relationship
class ChaiCert(models.Model):
    chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    expiry_date = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai.name}'
