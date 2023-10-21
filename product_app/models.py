# product_app/models.py
from django.db import models

class Product(models.Model):
    ProductGroupId = models.ForeignKey('ProductGroup', on_delete=models.CASCADE)
    Name = models.TextField()
    Code = models.TextField(blank=True, null=True)
    PLU = models.IntegerField(blank=True, null=True)
    MeasurementUnit = models.TextField()
    Price = models.FloatField(default=0)
    IsTaxInclusivePrice = models.IntegerField(blank=False, default=1)
    CurrencyId = models.ForeignKey('Currency', on_delete=models.CASCADE)
    IsPriceChangeAllowed = models.IntegerField(blank=False, default=0)
    IsService = models.IntegerField(null=False, default=0)
    IsUsingDefaultQuantity  = models.IntegerField(blank=False, default=1)
    IsEnabled  = models.IntegerField(null=False, default=1)
    Description = models.TextField()
    DateCreated = models.DateTimeField(auto_now=True) # DEFAULT(DATETIME ('now','localtime'))
    DateUpdated = models.DateTimeField(auto_now=True) # DEFAULT(DATETIME ('now','localtime'))
    Cost = models.FloatField(blank=False, default=0)
    Margin = models.FloatField(blank=False, default=0)
    Image = models.BinaryField()
    Color = models.TextField(null=False, default='Transparent')
    AgeRestriction = models.IntegerField()
    LastPurchasePrice = models.IntegerField(null=False, default=0)
    Rank = models.IntegerField(null=False, default=0)
    
class ProductGroup(models.Model):
    Id = models.AutoField(primary_key=True, null=False)
    Name = models.TextField(null=False)
    ParentGroupId = models.IntegerField()
    Color = models.TextField(null=False, default='Transparent')
    Image = models.BinaryField()
    Rank = models.IntegerField(null=False, default=0)
    
class Currency(models.Model):
    Id = models.AutoField(primary_key=True, null=False)
    Name = models.TextField(null=False)
    Code = models.TextField(null=False)