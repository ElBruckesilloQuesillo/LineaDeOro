# Generated by Django 4.2.2 on 2023-08-17 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id_destino', models.IntegerField(primary_key=True, serialize=False)),
                ('ciudad_destino', models.CharField(max_length=50)),
                ('hora_llegada', models.TimeField()),
            ],
        ),
    ]
