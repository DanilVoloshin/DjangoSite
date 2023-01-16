from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

class Table(models.Model):
    number = models.PositiveIntegerField(verbose_name="Номер стола")
    seats = models.PositiveIntegerField(verbose_name="Количество мест")
    
    
    width = models.PositiveIntegerField(verbose_name="Введите ширину стола(от 1 до 100)", validators=[MinValueValidator(1), MaxValueValidator(100)])
    length = models.PositiveIntegerField(verbose_name="Введите длину стола(от 1 до 100)", validators=[MinValueValidator(1), MaxValueValidator(100)])
    
    x = models.PositiveIntegerField(verbose_name="Введите положение стола по x(от 1 до 65)", validators=[MinValueValidator(1), MaxValueValidator(65)])
    y = models.PositiveIntegerField(verbose_name="Введите положение по y(от 1 до 100)", validators=[MinValueValidator(1), MaxValueValidator(100)])
    
    SHAPE_CHOICES = [('rectangular', 'Прямоугольный'),('oval', 'Овальный')]
    shape = models.CharField(max_length=50, choices=SHAPE_CHOICES, verbose_name="Форма стола")
    

    def __str__(self):
        return f"Стол под номером {self.number} на ({self.seats} мест)"
    
 
class Reservation(models.Model):
    name = models.CharField(max_length=22, null=True, verbose_name="Имя клиента")
    num_table = models.PositiveIntegerField(verbose_name="Номер стола")
    date = models.DateField(verbose_name="Дата заказа", default=datetime.now())
    
    def __str__(self):
        return f"Стол под номером {self.num_table} забронирован на дату: {self.date} | Имя клиента: {self.name}"