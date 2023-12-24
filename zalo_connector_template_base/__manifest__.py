# -*- coding: utf-8 -*-
# =====================================================================================
# License: OPL-1 (Odoo Proprietary License v1.0)
#
# By using or downloading this module, you agree not to make modifications that
# affect sending messages through erptoancau.com or avoiding contract a Plan with erptoancau.com.
# Support our work and allow us to keep improving this module and the service!
#
# =====================================================================================
{
    'name': 'ChatRoom SEND BASE',
    'summary': 'Base module for others. Messages and Templates.',
    'description': 'Base module for others. Zalo Messages and Templates.',
    'version': '16.0.5',
    'author': 'G-ERP',
    'support': 'thanhhai41280@gmail.com',
    'website': 'https://erptoancau.com',
    'license': 'OPL-1',
    'application': True,
    'installable': True,
    'auto_install': True,
    'category': 'Discuss',
    'depends': [
        'zalo_connector',
    ],
    'images': ['static/description/banner.png'],
    'currency': 'USD',
    'price': 39,
    'data': [
        'security/ir.model.access.csv',
        'wizard/MessageWizard.xml',
        'views/form_views.xml',
    ],
    'qweb': [
    ],
}
