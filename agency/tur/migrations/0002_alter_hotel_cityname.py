# Generated by Django 4.1.2 on 2022-10-26 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tur', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='cityName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel', to='tur.city'),
        ),
    ]
