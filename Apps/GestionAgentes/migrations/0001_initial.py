# Generated by Django 2.1.1 on 2018-09-14 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50)),
                ('vSNMP', models.CharField(max_length=50)),
                ('puerto', models.PositiveSmallIntegerField()),
                ('comunidad', models.CharField(max_length=50)),
            ],
        ),
    ]
