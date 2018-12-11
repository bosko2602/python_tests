# Generated by Django 2.1.3 on 2018-12-11 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('typ', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1)),
                ('size', models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL')], max_length=4)),
                ('color', models.CharField(max_length=30, null=True)),
                ('image', models.ImageField(null=True, upload_to='static/shirtserver/images/', verbose_name='image')),
            ],
        ),
    ]
