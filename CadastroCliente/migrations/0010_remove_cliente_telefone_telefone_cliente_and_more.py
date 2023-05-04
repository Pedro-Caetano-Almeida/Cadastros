# Generated by Django 4.2 on 2023-04-25 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroCliente', '0009_telefone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='telefone',
        ),
        migrations.AddField(
            model_name='telefone',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CadastroCliente.cliente'),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='ddd',
            field=models.CharField(max_length=2),
        ),
    ]
