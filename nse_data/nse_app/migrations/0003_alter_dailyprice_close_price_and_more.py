# Generated by Django 4.2.9 on 2024-01-30 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nse_app', '0002_alter_dailyprice_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyprice',
            name='close_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dailyprice',
            name='high_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dailyprice',
            name='low_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dailyprice',
            name='open_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='dailyprice',
            name='turnover',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
    ]
