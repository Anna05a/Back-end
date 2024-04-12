# Generated by Django 5.0.4 on 2024-04-10 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_remove_customuser_cards'),
        ('main', '0008_remove_card_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='cards',
            field=models.ManyToManyField(blank=True, to='main.card'),
        ),
    ]
