# Generated by Django 4.0.2 on 2022-05-17 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('codigo', models.CharField(max_length=255, verbose_name='Código')),
                ('stock', models.IntegerField(default=0, verbose_name='Stock')),
                ('precio', models.IntegerField(default=0, verbose_name='Precio')),
                ('descripcion', models.CharField(blank=True, default='', max_length=255, verbose_name='Descripción')),
                ('img', models.ImageField(default='AliciaPage\\static\\imagenes\\default.jpg', null=True, upload_to='AliciaPage\\static\\imagenes', verbose_name='Imagen')),
                ('empresa', models.CharField(choices=[('Winnem', 'Winnem'), ('Avon', 'Avon'), ('MeryKay', 'MeryKay'), ('Millanel', 'Millanel'), ('Tupper', 'Tupper'), ('Natura', 'Natura')], default='Natura', max_length=8)),
            ],
        ),
    ]
