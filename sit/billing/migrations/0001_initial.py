# Generated by Django 5.0.3 on 2025-01-16 20:48

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_insumo_producto'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('numero_factura', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_finalizacion', models.DateTimeField(blank=True, null=True)),
                ('fecha_entrega', models.DateTimeField(blank=True, null=True)),
                ('valor_venta', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coste_insumos', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('coste_servicio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('adelanto', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('valor_envio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('observaciones', models.TextField(blank=True, max_length=1000, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
                ('usuario_responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleProductos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalleProducto', to='billing.factura')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleInsumos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insumo', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalleFactura', to='billing.factura')),
            ],
        ),
    ]
