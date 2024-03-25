from odoo import models, fields


class PartnerPetBreed(models.Model):
    _description = "Pet Breed"
    _name = "res.partner.pet.breed"
    _order = "name"

    name = fields.Char(string="Name", required=True)
    kind_id = fields.Many2one('res.partner.pet.kind', string="Kind", required=True)
