from odoo import models, fields


class PartnerPetKind(models.Model):
    _description = "Pet Kind"
    _name = "res.partner.pet.kind"
    _order = "name"

    name = fields.Char(string="Name", required=True)
