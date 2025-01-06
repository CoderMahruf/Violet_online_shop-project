# Generated by Django 5.0.6 on 2025-01-06 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('discount', models.PositiveIntegerField(help_text='discount in parcentage')),
                ('active', models.BooleanField(default=True)),
                ('active_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
