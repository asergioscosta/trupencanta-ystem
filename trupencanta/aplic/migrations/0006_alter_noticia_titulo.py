# Generated by Django 4.2.8 on 2023-12-17 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0005_noticia_projeto_noticia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='titulo',
            field=models.CharField(max_length=255, verbose_name='Título'),
        ),
    ]