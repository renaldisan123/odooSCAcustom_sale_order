{
    'name': 'Custom Sale Order Fields',
    'version': '17.0.1.0.0',
    'category': 'Sales/Sales',
    'summary': 'Add Nego and Driver fields to Sale Order',
    'description': """Add Nego and Driver fields to Sales Order""",
    'author': 'SCA',
    'depends': [
        'base',
        'sale',
        'sale_management',
	'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
	'reports/sale_report_templates.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}