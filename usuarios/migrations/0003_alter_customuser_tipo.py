# Generated by Django 4.2.4 on 2023-10-15 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='tipo',
            field=models.CharField(choices=[('VE', 'Vendedor'), ('CE', 'Corretor'), ('AD', 'Administrador')], default='vendedor', max_length=10),
        ),
    ]
