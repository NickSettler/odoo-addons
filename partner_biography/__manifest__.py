{
    'name': 'Contacts Biography',
    'version': '17.0',
    'depends': ['base', 'contacts'],
    'description': """This module adds a biography to contacts""",
    'author': 'Nick Settler',
    'category': 'Contacts',
    'data': [
        'security/ir.model.access.csv',
        'data/res_partner_biography_category_data.xml',
        'data/res_partner_biography_category_type_data.xml',
        'views/res_partner_biography_category_views.xml',
        'views/res_partner_biography_category_type_views.xml',
        'views/res_partner_biography_line.xml',
        'views/res_partner.xml',
    ]
}