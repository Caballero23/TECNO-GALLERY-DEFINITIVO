# Generated by Django 3.2.9 on 2021-11-23 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviles', '0004_alter_carac_moviles_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fundas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('imagen', models.ImageField(upload_to='moviles')),
                ('precio', models.CharField(max_length=50)),
                ('movil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviles.carac_moviles')),
            ],
        ),
    ]
