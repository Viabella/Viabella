{
    'name': 'Viabella: Account',
    'version': '1.0',
    'summary': 'Accounting',
    'author': 'Novobi, LLC',
    'website': 'https://novobi.com',
    'category': 'Accounting',
    'license': 'OPL-1',
    'depends': [
        'account', 'sales_team', 'vb_product'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/res_partner_views.xml',
        'report/sale_season_report_views.xml'
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'auto_install': False,
    'application': False,
}
