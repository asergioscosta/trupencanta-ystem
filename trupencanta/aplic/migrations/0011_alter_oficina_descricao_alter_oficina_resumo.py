# Generated by Django 4.2.8 on 2023-12-23 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0010_alter_oficina_dia_aulas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficina',
            name='descricao',
            field=models.TextField(help_text='Insira uma descrição detalhada aqui.\nPule linhas conforme necessário.', verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='oficina',
            name='resumo',
            field=models.CharField(max_length=155, verbose_name='Resumo'),
        ),
    ]