# Generated by Django 4.0.3 on 2022-07-02 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_commande'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='total',
            field=models.CharField(default='500', max_length=200),
            preserve_default=False,
        ),
    ]
