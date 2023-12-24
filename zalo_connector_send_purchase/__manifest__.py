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
    'name': 'ChatRoom SEND Purchase Order and Templates. Zalo.',
    'summary': 'Send messages from Purchase Order with Templates.',
    'description': 'Send Purchase Orders. Real All in One. Send and receive messages. Real ChatRoom. Zalo integration. Zalo Connector. apichat.io. GupShup. Chat-Api. ChatApi. Drag and Drop.',
    'version': '16.0.1',
    'author': 'G-ERP',
    'support': 'thanhhai41280@gmail.com',
    'website': 'https://erptoancau.com',
    'license': 'OPL-1',
    'application': True,
    'installable': True,
    'auto_install': True,
    'category': 'Discuss',
    'images': ['static/description/banner.png'],
    'depends': [
        'zalo_connector_template_base',
        'purchase',
    ],
    'currency': 'USD',
    'price': 19,
    'data': [
        'data/data.xml',
        'views/res_config_settings_views.xml',
        'views/form_views.xml',
    ],
    'assets': {
    },
}
