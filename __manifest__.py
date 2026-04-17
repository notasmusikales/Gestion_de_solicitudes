{
    'name': 'Gestión de Solicitudes',
    'version': '1.0',
    'summary': 'Módulo para gestionar solicitudes internas',
    'description': """
Gestión de solicitudes con categorías, prioridades y asignaciones.
Incluye vistas en árbol, formulario y kanban, además de menús de configuración.
""",
    'author': 'Noel Gonzalez Febles',
    'depends': ['base', 'mail'],
    'data': [
        # Seguridad
        'security/ir.model.access.csv',

        # Datos iniciales (secuencias, etc.)
        'data/secuencia_data.xml',

        # Vistas primero
        'views/solicitud_tree.xml',
        'views/solicitud_form.xml',
        'views/solicitud_kanban.xml',

        # Menús y acciones al final
        'views/solicitud_menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}