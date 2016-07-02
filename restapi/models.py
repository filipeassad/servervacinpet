from django.db import models

class Animal(models.Model):

    nome = models.CharField(max_length=25)
    imagem = models.ImageField(upload_to='fotoanimal')
    dono = models.IntegerField()

    def publish(self):
        self.save()