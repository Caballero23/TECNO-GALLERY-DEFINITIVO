# Generated by Django 3.2.9 on 2021-11-19 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviles', '0002_auto_20211119_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carac_moviles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('ram', models.CharField(max_length=50)),
                ('tamaño', models.CharField(max_length=50)),
                ('capacidad', models.CharField(max_length=50)),
                ('mpx_camara', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='moviles')),
                ('precio', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Carac_moviles',
            },
        ),
        migrations.DeleteModel(
            name='moviles',
        ),
    ]