# Generated by Django 4.1 on 2022-09-02 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homestoreapp', '0002_rename_price_products_decription_products_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
