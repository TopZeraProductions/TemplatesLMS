# Generated by Django 2.1.2 on 2018-10-30 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProfessorDAL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=20, null=True, verbose_name='cidade')),
                ('uf', models.CharField(max_length=2, null=True, verbose_name='uf')),
                ('cep', models.CharField(max_length=8, null=True, verbose_name='cep')),
                ('endereco', models.CharField(max_length=50, null=True, verbose_name='endereco')),
                ('rg', models.CharField(max_length=20, null=True, verbose_name='rg')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
            ],
            options={
                'verbose_name': 'nome',
                'verbose_name_plural': 'nomes',
                'ordering': ['criado_em'],
            },
        ),
    ]
