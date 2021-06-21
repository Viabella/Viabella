{
    'name': 'Viabella: Product',
    'version': '1.0',
    'summary': 'Inventory',
    'author': 'Novobi, LLC',
    'website': 'https://novobi.com',
    'category': 'Inventory',
    'license': 'OPL-1',
    'depends': [
        'product', 'stock'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/sale_season_views.xml'
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
