# Generated by Django 2.2.1 on 2019-06-03 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20190603_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feeds',
            name='link',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='feeds',
            name='published',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='feeds',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
