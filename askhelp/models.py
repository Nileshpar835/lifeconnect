from django.db import models

# Create your models here.
class HelpRequest(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    urgency=models.CharField(max_length=10, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')])
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    