from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Student(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    avatar = models.ImageField(upload_to='students/', verbose_name='аватар', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name="активный")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ('last_name', 'first_name')

