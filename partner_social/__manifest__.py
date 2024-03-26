{
    'name': 'Partner Social',
    'version': '17.0',
    'depends': ['base', 'contacts'],
    'description': """This module adds social media information to contacts""",
    'author': 'Nick Settler',
    'category': 'Contacts',
    'data': [
        'data/res_partner_social_kind_data.xml',
        'security/ir.model.access.csv',
        'views/res_partner_social_kind.xml',
        'views/res_partner_social_type.xml',
        'views/res_partner_social.xml',
        'views/res_partner.xml',
        'views/res_partner_social_menu.xml',
    ]
}