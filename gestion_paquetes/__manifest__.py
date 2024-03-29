# -*- coding: utf-8 -*-
{
    'name': "gestion_paquetes",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['web','website', 'base', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_move_view_form.xml',
        'views/search_package.xml',
        'views/website_menu.xml',
        'views/custom_invoice_template.xml',
        'views/invoice_package_view.xml',
        'views/product_template_form_view.xml',
        'views/package_kanban_view.xml',
        'data/location_data.xml'

    ],
    'demo': [
        'demo/demo.xml',
    ],
}
