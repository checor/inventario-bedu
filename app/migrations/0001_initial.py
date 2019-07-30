# Generated by Django 2.2.3 on 2019-07-30 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=64)),
                ('rfc', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NotaProductos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('nota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Nota')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='nota',
            name='productos',
            field=models.ManyToManyField(through='app.NotaProductos', to='app.Producto'),
        ),
        migrations.CreateModel(
            name='CanastaProductos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('canasta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Canasta')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Producto')),
            ],
        ),
        migrations.AddField(
            model_name='canasta',
            name='cliente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Cliente'),
        ),
        migrations.AddField(
            model_name='canasta',
            name='productos',
            field=models.ManyToManyField(through='app.CanastaProductos', to='app.Producto'),
        ),
    ]