{
    'name': 'Contacts Pets',
    'version': '17.0',
    'depends': ['base', 'contacts'],
    'description': """This module adds pets to contacts""",
    'author': 'Nick Settler',
    'category': 'Contacts',
    'data': [
        'security/ir.model.access.csv',
        'data/res_partner_pet_kind_data.xml',
        'views/res_partner.xml',
        'views/res_partner_pet.xml',
        'views/res_partner_pet_color.xml',
        'views/res_partner_pet_menu.xml',
    ]
}
