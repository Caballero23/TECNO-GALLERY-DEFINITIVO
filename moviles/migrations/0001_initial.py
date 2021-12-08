# Generated by Django 3.2.9 on 2021-11-18 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='moviles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('caracteristicas', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='')),
                ('created', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'movil',
                'verbose_name_plural': 'moviles',
            },
        ),
    ]
