# -*- coding: utf-8 -*-
{
    'name': 'Viettel S-Invoice Connector',
    'version': '1.0',
    'category': 'Accounting',
    "license": "OPL-1",
    'description': """
        Tích hợp đồng bộ hoá đơn điện tử Viettel S-Invoice
    """,
    'author': 'G-ERP',
    'depends': [
        'base',
        'web',
        'account'
    ],
    'data': [
        # 'security/',
        'security/ir.model.access.csv',
        'security/ir_access_model.xml',
        # 'data/',
        'data/viettel_invoice_payment_type_data.xml',
        # 'view/',
        'views/res_company_view.xml',
        'views/res_partner_view.xml',
        'views/account_move_view.xml',
        'views/viettel_invoice_journal_view.xml',
        'wizard/show_message_wizard_view.xml',
        'wizard/invoice_info_adjust_wizard_view.xml',
        'wizard/viettel_invoice_cancel_wizard_view.xml',
    ],

    'test': [],
    'demo': [],
    'images': ['static/description/banner.png'],
    'installable': True,
    'active': False,
    'currency': 'USD',
    'price': 200,
    'application': True,
}
