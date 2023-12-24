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
    'name': 'Real All in One Zalo - Product',
    'summary': 'Send and receive messages. Real ChatRoom. Zalo integration. Send Product, Zalo Connector',
    'description': 'Send and receive messages. Real ChatRoom. Zalo integration. Send Product, Zalo Connector',
    'version': '16.0.1',
    'author': 'G-ERP',
    'website':'erptoancau.com',
    'support': 'thanhhai41280@gmail.com',
    'images': ['static/description/banner2.gif'],
    'license': 'OPL-1',
    'application': True,
    'installable': True,
    'category': 'Sales',
    'depends': [
        'bus',
        'zalo_configuration',
        'sales_team',
        'product'
    ],
    'data': [
        'data/data.xml',
        'data/cron.xml',
        'data/zalo.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/CustomMessage.xml',
        'wizard/init_free_test.xml',
        'wizard/ScanQr.xml',
        'wizard/SimpleNewConversation.xml',
        'views/ir_attachment.xml',
        'views/template_button_views.xml',
        'views/template_list_views.xml',
        'views/default_answer_views.xml',
        'views/connector_views.xml',
        'views/conversation_views.xml',
        'views/conversation_stage_views.xml',
        'views/conversation_tags_views.xml',
        'views/message_views.xml',
        'views/res_partner.xml',
        'views/res_users_views.xml',
        'views/module_views.xml',
        'views/template_waba_views.xml',
        'views/mail_template_views.xml',
        'views/ai_config_views.xml',
        'views/ai_interface_views.xml',
        'views/ai_usage_log_views.xml',
        'views/zalo_configuration_views.xml',
        'views/zalo_message_views.xml',
        'wizard/AiInterface.xml',
        'wizard/AiInterfaceTest.xml',
        'wizard/zalo_message_wizard_views.xml',
        'reports/report_conversation_views.xml',
        'reports/report_agent_answer_time.xml',
        'views/res_config_settings_views.xml',
        'views/menu.xml',
        'reports/reports.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'zalo_connector/static/src/scss/*.scss',
            'zalo_connector/static/src/odooCore/*/*.xml',

            'zalo_connector/static/src/components/*/*.scss',
            'zalo_connector/static/src/components/*/*.xml',

            'zalo_connector/static/src/jslib/chatroom.js',
        ],
        'web.assets_backend_prod_only': [
            'zalo_connector/static/src/services/chatroomNotification.js',
            'zalo_connector/static/src/main.js',
        ],
    },
    'post_load': '',
    'currency': 'USD',
    'price': 129,
    'external_dependencies': {'python': ['phonenumbers']},

}
