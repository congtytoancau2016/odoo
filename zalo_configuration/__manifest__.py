# -*- coding: utf-8 -*-
{
    'name': "Zalo Configuration",
    'summary': "Zalo Configuration",
    'description': "Zalo Configuration",
    'author': "G-ERP",
    'website':'erptoancau.com',
    # for the full list
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'contacts',
    ],
    'currency': 'USD',
    'price': 30,
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/zalo_configuration_views.xml',
    ],
}
