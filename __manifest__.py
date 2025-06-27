{
    'name': 'Parte de trabajo',
    'version': '16.0.1.0.0',
    'summary': 'Gestión de partes de trabajo para Odoo 16',
    'description': """
        Este modulo cubre las necesidades para una empresa que genere partes de trabajo:
        - Permite a los empleados rellenar hojas y partes de trabajo en Odoo
        - Historial y relación con obras y empleado sobre este módulo
        - Permite rellenar partes de trabajo apuntando día, hora y todo en vivo
    """,
    'category': 'Tools',
    'author': 'Nico Mesa',
    'website': 'https://github.com/nicomesa230',
    'depends': ['base','hr','obra','stock'],
    'data': [
        'security/ir.model.access.csv',
        'report/pt_report.xml',
        'report/action_pt_report.xml',
        'views/pt_tree.xml',
        'views/pt_form.xml',
        'views/ht_form.xml',
        'views/pt_kanban.xml',
        'views/pt_search.xml',
        'views/pt_menus.xml',
    ],
    'images': ['static/description/icon.png'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}