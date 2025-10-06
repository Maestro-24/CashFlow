from django.db import models
from django.urls import reverse

class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'statuses'
        verbose_name_plural = "Статусы"

class OperationType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = False
        db_table = 'operation_types'
        verbose_name_plural = "Операции"
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    operation_type = models.ForeignKey(OperationType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        managed = False
        db_table = 'categories'
        verbose_name_plural = "Категория"

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.category})"
    
    class Meta:
        managed = False
        db_table = 'subcategories'
        verbose_name_plural = "Подкатегория"


class FinancialRecord(models.Model):
    record_date = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    operation_type = models.ForeignKey(OperationType, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.record_date} - {self.amount} - {self.category}"

    def get_absolute_url(self):
        return reverse('record_list')

    class Meta:
        managed = False
        db_table = 'finance_records'
        verbose_name_plural = "финансовый учет"
        indexes = [
            models.Index(fields=['record_date']),
            models.Index(fields=['status']),
            models.Index(fields=['operation_type']),
            models.Index(fields=['category']),
            models.Index(fields=['amount']),
        ]