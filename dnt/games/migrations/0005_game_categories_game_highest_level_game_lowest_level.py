# Generated by Django 4.1.7 on 2023-03-23 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_question_rating_delete_remark'),
        ('games', '0004_alter_game_results'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='categories',
            field=models.ManyToManyField(related_name='categories', to='questions.category'),
        ),
        migrations.AddField(
            model_name='game',
            name='highest_level',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='lowest_level',
            field=models.SmallIntegerField(default=5),
            preserve_default=False,
        ),
    ]
