# Generated by Django 4.0.2 on 2022-07-13 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_actor_cinemahall_genre_movie_actors_movie_genres'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cinemahall',
            old_name='row',
            new_name='rows',
        ),
    ]
