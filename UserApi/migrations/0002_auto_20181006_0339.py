# Generated by Django 2.1.2 on 2018-10-05 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(max_length=100, unique=True)),
                ('code', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
                ('status', models.CharField(default='unused', max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
