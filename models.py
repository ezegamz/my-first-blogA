from django.db import models
from django.utils import timezone

class Post(models.Model):
    autor=models.ForeignKey('auth.user', on_delete=models.CASCADE)
    titulo=models.CharField(max_length=200)
    texto=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True, null=True)

    def Publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

