# Generated by Django 5.0.4 on 2024-05-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_category_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='payment_desc',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
