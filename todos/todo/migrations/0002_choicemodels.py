# Generated by Django 3.0.7 on 2020-06-11 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('One', 'First choice'), ('Two', '2nd choice choice'), ('Three', '3rd choice')], max_length=200)),
            ],
        ),
    ]
