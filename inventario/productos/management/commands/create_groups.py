from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = 'Create initial groups and assign permissions: administradores, stock, ventas'

    def handle(self, *args, **options):
        # Administradores: all permissions
        admin_group, _ = Group.objects.get_or_create(name='administradores')
        all_perms = Permission.objects.all()
        admin_group.permissions.set(all_perms)
        admin_group.save()

        # Stock group: permisos sobre Producto y MovimientoStock
        stock_group, _ = Group.objects.get_or_create(name='stock')
        # Productos
        try:
            from productos.models import Producto, MovimientoStock
            product_ct = ContentType.objects.get_for_model(Producto)
            mov_ct = ContentType.objects.get_for_model(MovimientoStock)

            perms = Permission.objects.filter(content_type__in=[product_ct, mov_ct])
            stock_group.permissions.set(perms)
            stock_group.save()
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Warning assigning stock perms: {e}'))

        # Ventas group: permisos sobre Cliente, Venta Y permiso de lectura en Productos
        ventas_group, _ = Group.objects.get_or_create(name='ventas')
        try:
            from clientes.models import Cliente
            from ventas.models import Venta
            from productos.models import Producto
            
            cliente_ct = ContentType.objects.get_for_model(Cliente)
            venta_ct = ContentType.objects.get_for_model(Venta)
            product_ct = ContentType.objects.get_for_model(Producto)

            # Permisos sobre Cliente y Venta (todos)
            perms = Permission.objects.filter(content_type__in=[cliente_ct, venta_ct])
            
            # Agregar solo permiso de lectura (view) en Productos
            view_producto_perm = Permission.objects.filter(
                content_type=product_ct,
                codename='view_producto'
            )
            perms = perms | view_producto_perm
            
            ventas_group.permissions.set(perms)
            ventas_group.save()
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Warning assigning ventas perms: {e}'))

        self.stdout.write(self.style.SUCCESS('Groups and permissions created/updated.'))
