# Generated by Django 3.1.7 on 2021-04-03 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('statistikdesa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kartukeluarga',
            name='no_kk',
            field=models.CharField(max_length=16, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Penduduk',
            fields=[
                ('nik', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=100)),
                ('jenis_kelamin', models.CharField(max_length=30)),
                ('tempat_lahir', models.CharField(max_length=100)),
                ('tgl_lahir', models.DateField()),
                ('golongan_darah', models.CharField(max_length=20, null=True)),
                ('Agama', models.CharField(max_length=100)),
                ('status_perkawinan', models.CharField(max_length=100)),
                ('hubungan_keluarga', models.CharField(max_length=100)),
                ('pendidikan', models.CharField(max_length=100)),
                ('pekerjaan', models.CharField(max_length=100)),
                ('no_kk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='statistikdesa.kartukeluarga')),
            ],
        ),
    ]
