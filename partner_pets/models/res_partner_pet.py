from odoo import models, fields, api


class PartnerPet(models.Model):
    _description = "Pet"
    _name = "res.partner.pet"
    _inherit = ['avatar.mixin']
    _order = "name"

    name = fields.Char(string="Name", required=True)
    id_number = fields.Char(string="ID Number", required=True, help="ID number of the pet as in the passport")
    breed_id = fields.Many2one('res.partner.pet.breed', string="Breed", required=True, store=True)
    kind_id = fields.Many2one('res.partner.pet.kind', string="Kind", readonly=True,
                              related='breed_id.kind_id', store=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ],
        string='Gender',
        required=True
    )
    birthdate = fields.Date(string="Birthdate")
    age = fields.Integer(string="Age", compute='_compute_age', store=True)
    color_ids = fields.Many2many('res.partner.pet.color', string="Colors")
    owner_id = fields.Many2one('res.partner', string="Owner", required=True)
    note = fields.Text(string="Note")

    _sql_constraints = [
        ('birthdate_must_be_past', 'CHECK(birthdate <= NOW())', 'Birthdate must be in the past')
    ]

    @api.depends('birthdate')
    def _compute_age(self):
        for pet in self:
            if pet.birthdate:
                pet.age = (fields.Date.today() - pet.birthdate).days // 365
            else:
                pet.age = 0
