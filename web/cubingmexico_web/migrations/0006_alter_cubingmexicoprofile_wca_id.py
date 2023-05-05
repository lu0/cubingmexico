# Generated by Django 4.1.7 on 2023-05-04 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cubingmexico_wca', '0001_initial'),
        ('cubingmexico_web', '0005_alter_cubingmexicoprofile_wca_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cubingmexicoprofile',
            name='wca_id',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='cubingmexico_wca.person'),
        ),
    ]