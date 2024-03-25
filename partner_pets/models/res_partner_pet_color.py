from odoo import models, fields


class PartnerPetColor(models.Model):
    _description = "Pet Color"
    _name = "res.partner.pet.color"
    _order = "name"

    name = fields.Char(string="Name", required=True)
    color = fields.Char(string="Color", required=True)
