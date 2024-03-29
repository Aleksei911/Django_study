# Generated by Django 4.1.5 on 2023-01-04 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device_color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Device_manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Device_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(max_length=20)),
                ('device_name', models.CharField(max_length=50)),
                ('create_date', models.DateTimeField()),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('count', models.IntegerField()),
                ('characteristic', models.CharField(max_length=255)),
                ('cargo_code', models.CharField(max_length=50)),
                ('publication', models.BooleanField()),
                ('category', models.CharField(max_length=50)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.device_color')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.device_manufacturer')),
                ('model_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.device_model')),
            ],
        ),
    ]
