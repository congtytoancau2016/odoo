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
    'name': 'ChatRoom Marketing & Group with zalo Templates',
    'summary': 'Send mass message with Templates. Advanced Options. Marketing zalo group ChatRoom 2.0.',
    'description': 'Send mass zalo with Templates message Marketing. Marketing zalo group ChatRoom 2.0.',
    'version': '16.0.15',
    'author': 'G-ERP',
    'support': 'thanhhai41280@gmail.com',
    'website': 'https://erptoancau.com',
    'images': ['static/description/banner.png'],
    'license': 'OPL-1',
    'application': True,
    'installable': True,
    'category': 'Marketing/Email Marketing',
    'depends': [
        'zalo_connector',
        'mass_mailing',
        'sms',  # for sms_widget widget
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/utm_data.xml',
        'data/cron.xml',
        'views/menus.xml',
        'views/mailing_contact_views.xml',
        'views/mailing_list_views.xml',
        'views/mailing_mailing_views.xml',
        'views/mailing_trace_views.xml',
        # 'views/utm_campaign_views.xml',
        'views/res_config_settings_views.xml',
        'report/mailing_trace_report_views.xml',
        'wizards/import_records.xml',
        'wizards/mailing_sms_test_views.xml',
        'wizards/send_multi_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            '/zalo_connector_mass/static/src/css/*.css',
        ],
    },
    'currency': 'USD',
    'price': 49,
    'qweb': [
    ],
    'post_load': '',
}
