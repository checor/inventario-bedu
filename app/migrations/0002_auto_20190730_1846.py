# Generated by Django 2.2.3 on 2019-07-30 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CanastaProductos',
            new_name='ProductoCanasta',
        ),
        migrations.RemoveField(
            model_name='nota',
            name='productos',
        ),
        migrations.AddField(
            model_name='nota',
            name='canasta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Canasta'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='NotaProductos',
        ),
    ]
