# admin.py

from django.contrib import admin
from .models import Category, Musteri, Restoran, RestoranDetay, Urun, Siparis, SiparisDetay



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'urun']

@admin.register(Musteri)
class MusteriAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'telefon', 'adres']

@admin.register(Restoran)
class RestoranAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'adres', 'telefon']

@admin.register(RestoranDetay)
class RestoranDetayAdmin(admin.ModelAdmin):
    list_display = ['restoran_name', 'adres', 'telefon', 'acilis_saati', 'kapanis_saati', 'puan', 'resim']

@admin.register(Urun)
class UrunAdmin(admin.ModelAdmin):
    list_display = ['urun_id', 'name', 'image', 'price', 'description']

@admin.register(Siparis)
class SiparisAdmin(admin.ModelAdmin):
    list_display = ['mus_id', 'siparis_tarihi', 'teslim_tarihi', 'tutar', 'durum']

@admin.register(SiparisDetay)
class SiparisDetayAdmin(admin.ModelAdmin):
    list_display = ['siparis', 'miktar', 'fiyat', 'toplam_tutar']
