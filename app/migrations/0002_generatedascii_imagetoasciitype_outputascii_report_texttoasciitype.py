# Generated by Django 3.1 on 2020-08-29 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneratedASCII',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferred_output_method', models.CharField(max_length=128)),
                ('url_code', models.CharField(max_length=7, unique=True)),
                ('is_hidden', models.BooleanField(default=False)),
                ('date_shared', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TextToASCIIType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_text', models.TextField(max_length=256)),
                ('generated_ascii', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='text_to_ascii_type', to='app.generatedascii')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=512)),
                ('date_reported', models.DateTimeField(auto_now=True)),
                ('generated_ascii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='app.generatedascii')),
            ],
        ),
        migrations.CreateModel(
            name='OutputASCII',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method_name', models.CharField(max_length=128)),
                ('ascii_txt', models.TextField()),
                ('generated_ascii', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outputs', to='app.generatedascii')),
            ],
        ),
        migrations.CreateModel(
            name='ImageToASCIIType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_image', models.ImageField(upload_to='input_images')),
                ('generated_ascii', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='image_to_ascii_type', to='app.generatedascii')),
            ],
        ),
    ]
