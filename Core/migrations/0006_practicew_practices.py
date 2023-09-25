# Generated by Django 4.2.5 on 2023-09-25 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_alter_speaking_type_alter_writing_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='PracticeW',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('solution', models.TextField(default='')),
                ('user', models.IntegerField(default=0)),
                ('problem', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Core.writing')),
            ],
        ),
        migrations.CreateModel(
            name='PracticeS',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('solution', models.TextField(default='')),
                ('user', models.IntegerField(default=0)),
                ('problem', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Core.speaking')),
            ],
        ),
    ]
