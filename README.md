Тестовое задание
В проекте Django есть 2 приложения (apps) - spend и revenue

файл models.py в Spend имеет следующий вид:

```python 
class SpendStatistic(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    spend = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    impressions = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
    conversion = models.IntegerField(default=0)
```

файл models.py в Revenue имеет следующий вид:

```python 
class RevenueStatistic(models.Model):
    name = models.CharField(max_length=255)
    spend = models.ForeignKey('spend.SpendStatistic', on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    revenue = models.DecimalField(max_digits=9, decimal_places=2, default=0)
```

## Задача.

Написать файл views.py в revenue. Реализовать эндпоинт в котором мы получаем queryset модели RevenueStatistic с делением по дням (date) и названием (name), с агрегированными суммами значений revenue и связанными значениями spend, impressions, clicks, conversion из модели SpendStatistic.

Написать файл views.py в spend. Реализовать эндпоинт в котором мы получаем queryset модели SpendStatistic с делением по дням (date) и имени (name), с агрегированными суммами значений spend, impressions, clicks, conversion и связанными значениями revenue из модели RevenueStatistic.

Использовать средства Django Rest Framework.
serializers.py писать необязательно.
Выполненное задание выложить на GitHub и переслать ссылку.
Уточняющие вопросы из тестового задания сюда - @developer_for