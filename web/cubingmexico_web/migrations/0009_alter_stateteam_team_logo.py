# Generated by Django 4.1.7 on 2023-05-04 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cubingmexico_web', '0008_cubingmexicoprofile_is_state_team_leader_stateteam_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stateteam',
            name='team_logo',
            field=models.ImageField(blank=True, null=True, upload_to='img/team_logos/'),
        ),
    ]
