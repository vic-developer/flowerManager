from django.db import models

# Create your models here.

# class Product(models.Model):
#     id    = models.AutoField(primary_key=True)
#     name  = models.CharField(max_length = 100) 
#     info  = models.CharField(max_length = 100, default = '')
#     price = models.IntegerField(blank=True, null=True)

#     def __str__(self):
#         return self.name

class Kwiat(models.Model):
    id                  = models.AutoField(primary_key=True)
    name                = models.CharField(max_length = 100) 
    kategorie_i_kolory  = models.JSONField()
    aktywny             = models.BooleanField(default=True)
    kolejnosc           = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = "Kwiaty"  # Or your custom plural form

    def __str__(self):
        return self.name

class Kolory(models.Model):
    id                  = models.AutoField(primary_key=True)
    name                = models.CharField(max_length = 100) 
    custom_background   = models.ImageField(upload_to='tla', null=True, blank=True)
    hex_kolor           = models.CharField(max_length = 100, default = '')

    class Meta:
        verbose_name_plural = "Kolory"  # Or your custom plural form

    def __str__(self):
        return self.name

class Raport(models.Model):
    id                  = models.AutoField(primary_key=True)
    data_utworzenia     = models.DateTimeField(auto_now=True)
    wartosc             = models.JSONField()

    class Meta:
        verbose_name_plural = "Raporty"  # Or your custom plural form


class Zamowienie(models.Model):
    id                  = models.AutoField(primary_key=True)
    odbiorca            = models.CharField(max_length = 200) 
    status              = models.CharField(max_length = 200) 
    produkty            = models.JSONField()
    termin_dostarczenia = models.DateTimeField(blank=True, null=True)
    data_utworzenia     = models.DateTimeField(auto_now=True)
    zdjecie             = models.ImageField(upload_to='zamowienia', null=True, blank=True)
    notatka             = models.CharField(max_length = 5000, blank=True) 

    class Meta:
        verbose_name_plural = "Zamówienia"  # Or your custom plural form

    def __str__(self):
        return self.odbiorca