{
    'name': 'Viabella: Sales',
    'version': '1.0',
    'summary': 'Sales',
    'author': 'Novobi, LLC',
    'website': 'https://novobi.com',
    'category': 'Sales',
    'license': 'OPL-1',
    'depends': [
        'sale', 'vb_product'
    ],
    'data': [
        'views/sale_order_views.xml'
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
