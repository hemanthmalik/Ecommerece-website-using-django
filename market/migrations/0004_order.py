# Generated by Django 2.2.1 on 2019-08-05 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=100)),
                ('address1', models.CharField(default='', max_length=500)),
                ('address2', models.CharField(default='', max_length=500)),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('zip', models.CharField(default='', max_length=50)),
                ('itemsJson', models.CharField(default='', max_length=2000)),
            ],
        ),
    ]
