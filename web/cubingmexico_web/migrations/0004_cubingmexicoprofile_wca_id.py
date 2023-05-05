# Generated by Django 4.1.7 on 2023-05-04 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cubingmexico_wca', '0001_initial'),
        ('cubingmexico_web', '0003_remove_cubingmexicoprofile_last_edit_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='cubingmexicoprofile',
            name='wca_id',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='cubingmexico_wca.person'),
            preserve_default=False,
        ),
    ]
