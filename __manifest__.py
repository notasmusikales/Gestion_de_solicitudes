{
    'name': 'Gestión de Solicitudes',
    'version': '1.0.0',
    'category': 'Services',
    'summary': 'Módulo para gestionar solicitudes internas (IT, RRHH, Compras)',
    'description': """
        Módulo personalizado para la gestión de solicitudes internas de la empresa.
        Permite registrar y dar seguimiento a solicitudes de:
        - IT: Soporte técnico, Hardware, Software
        - RRHH: Vacaciones, Permisos, Capacitaciones
        - Compras: Suministros, Equipos, Servicios
    """,
    'author': 'Empresa',
    'website': '',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/secuencia_data.xml',
        'views/solicitud_menu.xml',
        'views/solicitud_tree.xml',
        'views/solicitud_form.xml',
        'views/solicitud_kanban.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}