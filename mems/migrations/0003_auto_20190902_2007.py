# Generated by Django 2.2.4 on 2019-09-02 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mems', '0002_auto_20190831_0145'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='purchaseOrder',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='category',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='department',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='manufacturer',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='serialNumber',
            field=models.CharField(default='', max_length=20),
        ),
    ]
