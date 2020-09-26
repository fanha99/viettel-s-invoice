# © 2018 Fanha (Fanha Giang <fanha99@hotmail.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': "Viettel S-Invoice",

    'summary': """
            Viettel S-Invoice Intergration
        """,

    'description': """
        Viettel S-Invoice Intergration
    """,
    "data": [
        'view/templates.xml',
        'view/account_invoice_view.xml',
        'view/res_company.xml',
        'data/data.xml',
        'security/ir.model.access.csv'
    ],
    "license": "LGPL-3",
    "depends": ['base','account'],
    'author': "Fanha Giang",
    'category': 'API Viettel S-Invoice',
    'version': '1.1.0',
    'installable': True,
}