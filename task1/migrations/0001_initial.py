# Generated by Django 4.0.2 on 2022-02-17 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=200, null=True)),
                ('producttype', models.CharField(choices=[('Digital', 'Digital'), ('Physical', 'Physical')], max_length=200, null=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, default='default.png', null=True, upload_to='')),
            ],
        ),
    ]
