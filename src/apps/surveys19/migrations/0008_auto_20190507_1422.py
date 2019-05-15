# Generated by Django 2.2 on 2019-05-07 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys19', '0007_auto_20190421_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='display',
        ),
        migrations.AddField(
            model_name='product',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys19.Product', verbose_name='Parent Product'),
        ),
    ]