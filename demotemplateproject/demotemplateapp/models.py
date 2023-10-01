from django.db import models

# Create your models here.
class django(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pictures')
    des=models.TextField()

    def __str__(self):
        return self.name
class place(models.Model):
    logo=models.ImageField(upload_to='pictures')
    image=models.ImageField(upload_to='pictures')
    head=models.TextField()
    para=models.TextField()

    def __str__(self):
        return self.head
