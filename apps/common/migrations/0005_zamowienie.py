# Generated by Django 4.2.6 on 2023-11-21 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_kwiat_kolejnosc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zamowienie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('odbiorca', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('produkty', models.JSONField()),
                ('termin_dostarczenia', models.DateTimeField(blank=True, null=True)),
                ('data_utworzenia', models.DateTimeField(auto_now=True)),
                ('zdjecie', models.ImageField(blank=True, null=True, upload_to='zamowienia')),
                ('notatka', models.CharField(blank=True, max_length=5000)),
            ],
        ),
    ]
