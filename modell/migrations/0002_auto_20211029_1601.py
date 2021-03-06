# Generated by Django 3.2.8 on 2021-10-29 11:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('modell', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='modell.user'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modell.posts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modell.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_content', models.CharField(default='', max_length=500)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modell.posts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modell.user')),
            ],
        ),
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('bio_id', models.AutoField(primary_key=True, serialize=False)),
                ('bio_email', models.EmailField(default='', max_length=75)),
                ('bio_password', models.CharField(default='', max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modell.user')),
            ],
        ),
    ]
