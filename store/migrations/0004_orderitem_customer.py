# Generated by Django 3.2.3 on 2021-05-28 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210527_2254'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.customer'),
        ),
    ]
