# Generated by Django 4.1 on 2022-11-24 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homestoreapp', '0008_alter_buying_paymwnt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buying',
            name='status',
            field=models.CharField(default='awaiting', max_length=255),
        ),
    ]
