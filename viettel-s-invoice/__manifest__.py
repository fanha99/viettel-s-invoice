{
    'name': "Viettel S-Invoice",

    'summary': """
            Viettel S-Invoice Intergration
        """,

    'description': """
        Viettel S-Invoice Intergration
    """,
    "data": [
        'view/account_invoice_view.xml',
        'view/res_company.xml',
        'data/data.xml',
        'security/ir.model.access.csv'
    ],
    "license": "LGPL-3",
    "depends": ['base','account'],
    'author': "Fanha Giang",
    'category': 'API Viettel S-Invoice',
    'version': '1.0.1',
    'installable': True,
}