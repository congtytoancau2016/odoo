# -*- coding: utf-8 -*-
# =====================================================================================
# License: OPL-1 (Odoo Proprietary License v1.0)
#
# By using or downloading this module, you agree not to make modifications that
# affect sending messages through erptoancau.com or avoiding contract a Plan with erptoancau.com.
# Support our work and allow us to keep improving this module and the service!
#
# Al utilizar o descargar este módulo, usted se compromete a no realizar modificaciones que
# afecten el envío de mensajes a través de erptoancau.com o a evitar contratar un Plan con erptoancau.com.
# Apoya nuestro trabajo y permite que sigamos mejorando este módulo y el servicio!
# =====================================================================================

{
    'name': 'ChatRoom Sale extra, Invoice. Real All in One',
    'summary': 'Send and receive messages. Real ChatRoom. Zalo integration. Send Product, Zalo Connector',
    'description': 'Send and receive messages. Real ChatRoom. Zalo integration. Send Product, Zalo Connector',
    'version': '16.0.1',
    'author': 'G-ERP',
    'support': 'thanhhai41280@gmail.com',
    'images': ['static/description/banner.png'],
    'website': 'https://erptoancau.com',
    'license': 'OPL-1',
    'application': True,
    'installable': True,
    'category': 'Discuss/Sales/CRM',
    'depends': [
        'zalo_connector',
        'sale_management',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizard/SelectConversation.xml',
        'views/sale_order_views.xml',
        'views/res_partner_view.xml',
        'views/acrux_chat_conversation_views.xml',
        'reports/reports.xml',
    ],
    'currency': 'USD',
    'price': 49,
    'assets': {
        'web.assets_backend': [
            'zalo_connector_sale/static/src/components/*/*.scss',
            'zalo_connector_sale/static/src/components/*/*.xml',
            'zalo_connector_sale/static/src/jslib/chatroom.js',
        ],
    },
}
