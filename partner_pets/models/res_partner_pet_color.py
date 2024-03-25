from odoo import models, fields


class PartnerPetBreed(models.Model):
    _name = "res.partner.pet.color"
    _order = "name"

    name = fields.Char(string="Name", required=True)
    color = fields.Char(string="Color", required=True)
