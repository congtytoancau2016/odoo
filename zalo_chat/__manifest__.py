# -*- coding: utf-8 -*-
{
    'name': "Zalo Chat",
    'summary': "Zalo official account for website",
    'description': "Zalo official account for website",
    'author': 'haiduong',
    'category': 'Website',
    'website':'erptoancau.com',
    'version': '1.0',
    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],
    # always loaded
    'data': [
        'data/data.xml',
        'views/res_config_settings.xml',
        'views/template.xml',
    ],
    'price': 3,
    'currency': 'EUR',
    'installable': True,
    'images': [
		'static/description/icon.png'
	    ],
}
