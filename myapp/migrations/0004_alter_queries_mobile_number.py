# Generated by Django 4.1 on 2022-08-09 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_queries_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queries',
            name='mobile_number',
            field=models.IntegerField(blank=True, default=0, verbose_name='zipcode'),
        ),
    ]
