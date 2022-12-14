# Generated by Django 2.0.1 on 2018-02-10 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0003_auto_20180210_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=7)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=5)),
                ('desconto', models.DecimalField(decimal_places=2, max_digits=5)),
                ('impostos', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pessoa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='medicamentos.Person')),
            ],
        ),
    ]
