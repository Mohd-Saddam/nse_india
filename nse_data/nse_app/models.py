from django.db import models

class Index(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class DailyPrice(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True, blank=True)
    open_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    high_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    low_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    close_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    shares_traded = models.IntegerField(null=True)
    turnover = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.index.name} - {self.date}"
