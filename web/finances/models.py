from django.db import models


class ImpBalance(models.Model):
    """Balance account model"""
    ACC_CURRENCY = (
        ('RUB', "Российский рубль"),
        ('BYN', "Белорусский Рубль")
    )
    user = models.ForeignKey("users.ImpUser", on_delete=models.CASCADE, blank=False, verbose_name="Владелец")
    name = models.CharField(max_length=100, blank=False, verbose_name="Название")
    desc = models.CharField(max_length=250, blank=True, verbose_name="Описание")
    currency = models.CharField(max_length=3, choices=ACC_CURRENCY, blank=False, verbose_name="Валюта")
    value = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, verbose_name="Остаток")

    def __str__(self):
        return f"{self.name} | {self.currency} | {self.value} | {self.user}"
