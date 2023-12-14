from django.urls import path, re_path

from .views import (
    admin,
    administrar_productos,
    administrar_imagenes,
    administrar_directorio,
    usuarios,
    usuario,
    cambiar_password,
    eliminar_usuario,
    eliminar_lista,
    solicitudes_credito_distribuidor,
    solicitud_credito_distribuidor,
    solicitudes_credito_empresas,
    solicitud_credito_empresas,
    generar_clave_distribuidor,
    direcciones_email,
    generar_remitente,
    desactivar_email,
    activar_email,
    marca_categoria,
    edit_marca,
    edit_categoria,
    edit_subcategoria,
    edit_url,
    eliminar_marca,
    eliminar_categoria,
    eliminar_subcategoria,
    eliminar_url,
    equipo_renta,
    edit_equipo_renta,
    eliminar_equipo_renta,
    rentas,
    renta,
    renta_pdf,
    actividad,
    confirmar_actividad,
    actividades,
    eliminar_actividad,
    aviso_vencimiento,
    aviso_bitacoras_vencidas,
    encuestas,
    ver_encuesta,
    catalogo_vendedores,
    convertir_proyecto,
    cancelar_proyecto,
    eliminar_clientes_repetidos,
    vendedor,
    imagenes_inicio,
    admin_mundo_tecnologia,
    editar_distribuidor,
    eliminar_solicitud_trabajo,
    database_backup_compuproveedores,
    aviso_privacidad,
    avisos,
    subir_vendedores,
)

urlpatterns = [
    path('', admin, name="admin"),
    path('administrar_productos/', administrar_productos,
         name="administrar_productos"),
    path('administrar_imagenes/', administrar_imagenes,
         name="administrar_imagenes"),
    path('administrar_directorio/', administrar_directorio,
         name="administrar_directorio"),
    path('usuarios/', usuarios, name="usuarios"),
    re_path(r'^usuario/(.+)/$', usuario, name="usuario"),
    re_path(r'^cambiar_password/(\d+)/$',
            cambiar_password, name="cambiar_password"),
    re_path(r'^eliminar_usuario/(.+)/$',
            eliminar_usuario, name="eliminar_usuario"),
    re_path(r'^eliminar_lista/(\d+)/$', eliminar_lista, name="eliminar_lista"),

    # Add other paths as needed...

    re_path(r'^solicitudes_credito_distribuidores/$',
            solicitudes_credito_distribuidor, name="solicitudes_credito_distribuidor"),
    re_path(r'^solicitud_credito_distribuidor/(.+)/$',
            solicitud_credito_distribuidor, name="solicitud_credito_distribuidor"),
    re_path(r'^solicitudes_credito_empresas/$',
            solicitudes_credito_empresas, name="solicitudes_credito_empresas"),
    re_path(r'^solicitud_credito_empresas/(.+)/$',
            solicitud_credito_empresas, name="solicitud_credito_empresas"),
    re_path(r'^generar_clave_distribuidor/(.+)/$',
            generar_clave_distribuidor, name="generar_clave_distribuidor"),
    re_path(r'^direcciones_email/$', direcciones_email,
            name="direcciones_email"),
    re_path(r'^generar_remitente/$', generar_remitente,
            name="generar_remitente"),
    re_path(r'^desactivar_email/(.+)/(.+)/$',
            desactivar_email, name="desactivar_email"),
    re_path(r'^activar_email/(.+)/(.+)/$',
            activar_email, name="activar_email"),
    # Add other paths as needed...
]

urlpatterns += [
    re_path(r'^marca_categoria/$', marca_categoria, name="marca_categoria"),
    re_path(r'^edit_marca/(.+)/$', edit_marca, name="edit_marca"),
    re_path(r'^edit_categoria/(.+)/$', edit_categoria, name="edit_categoria"),
    re_path(r'^edit_subcategoria/(.+)/$',
            edit_subcategoria, name="edit_subcategoria"),
    re_path(r'^edit_url/(.+)/$', edit_url, name="edit_url"),
    re_path(r'^eliminar_marca/(.+)/$', eliminar_marca, name="eliminar_marca"),
    re_path(r'^eliminar_categoria/(.+)/$',
            eliminar_categoria, name="eliminar_categoria"),
    re_path(r'^eliminar_subcategoria/(.+)/$',
            eliminar_subcategoria, name="eliminar_subcategoria"),
    re_path(r'^eliminar_url/(.+)/$', eliminar_url, name="eliminar_url"),
    # Add other paths as needed...
]

urlpatterns += [
    re_path(r'^equipo_renta/$', equipo_renta, name="equipo_renta"),
    re_path(r'^edit_equipo_renta/(.+)/$',
            edit_equipo_renta, name="edit_equipo_renta"),
    re_path(r'^eliminar_equipo_renta/(.+)/$',
            eliminar_equipo_renta, name="eliminar_equipo_renta"),
    re_path(r'^rentas/$', rentas, name="rentas"),
    re_path(r'^renta/(.+)/$', renta, name="renta"),
    re_path(r'^renta_pdf/(.+)/$', renta_pdf, name="renta_pdf"),
    # Add other paths as needed...
]

urlpatterns += [
    re_path(r'^actividad/(\d+)/$', actividad, name="actividad"),
    re_path(r'^confirmar_actividad/(\d+)/$',
            confirmar_actividad, name="confirmar_actividad"),
    re_path(r'^actividades/$', actividades, name="actividades"),
    re_path(r'^eliminar_actividad/(\d+)/$',
            eliminar_actividad, name="eliminar_actividad"),
    # Add other paths as needed...
]

urlpatterns += [
    re_path(r'^aviso_vencimiento/$', aviso_vencimiento,
            name="aviso_vencimiento"),
    re_path(r'^aviso_bitacoras_vencidas/$', aviso_bitacoras_vencidas,
            name="aviso_bitacoras_vencidas"),
    # Add other paths as needed...
]

urlpatterns += [
    re_path(r'^encuestas/$', encuestas, name="encuestas"),
    re_path(r'^ver_encuesta/(\d+)/$', ver_encuesta, name="ver_encuesta"),
    # Add other paths as needed...
]

urlpatterns += [
    re_path(r'^catalogo_vendedores/$', catalogo_vendedores,
            name="catalogo_vendedores"),
    re_path(r'^convertir_proyecto/(.*)/$',
            convertir_proyecto, name="convertir_proyecto"),
    re_path(r'^cancelar_proyecto/(.*)/$',
            cancelar_proyecto, name="cancelar_proyecto"),
    # Add other paths as needed...
]

urlpatterns += [
    re_path(r'^eliminar_clientes_repetidos/$',
            eliminar_clientes_repetidos, name="eliminar_clientes_repetidos"),
    re_path(r'^vendedor/(.*)/$', vendedor, name="admin-vendedor"),
    re_path(r'^imagenes_inicio/$', imagenes_inicio,
            name="admin-imagenes_inicio"),
    re_path(r'^mundo_tecnologia/$', admin_mundo_tecnologia,
            name="admin_mundo_tecnologia"),
    re_path(r'^editar_distribuidor/(.*)/$', editar_distribuidor,
            {"distribuidor": True}, name="admin_editar_distribuidor"),
    re_path(r'^editar_empresa/(.*)/$', editar_distribuidor,
            {"distribuidor": False}, name="admin_editar_empresa"),
    re_path(r'^eliminar_solicitud_trabajo/(\d+)/$',
            eliminar_solicitud_trabajo, name="eliminar_solicitud_trabajo"),
    re_path(r'^database_backup_compuproveedores/$',
            database_backup_compuproveedores, name="database_backup_compuproveedores"),
    re_path(r'^aviso_privacidad/$', aviso_privacidad,
            name="admin-aviso_privacidad"),
    re_path(r'^avisos/$', avisos, name="admin-avisos"),
    re_path(r'^subir_vendedores/$', subir_vendedores,
            name="admin-subir_vendedores"),
    # Add other paths as needed...
]
