from django.db import models


# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=11)
    content = models.TextField()
    timestamp = models.DateField()

    
    def __str__(self):
        return "Message from " + self.name + " - " + self.email




class Question(models.Model):
    ques = models.CharField(max_length=150)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    cor_option = models.CharField(max_length=5)


    def __str__(self):
        return self.ques
