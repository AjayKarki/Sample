# Generated by Django 2.2.1 on 2020-01-10 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0005_newe'),
    ]

    operations = [
        migrations.CreateModel(
            name='New1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sample', models.CharField(max_length=123)),
            ],
        ),
        migrations.DeleteModel(
            name='Newe',
        ),
    ]
