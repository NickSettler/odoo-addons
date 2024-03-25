from odoo import models, fields


class PartnerPetKind(models.Model):
    _name = "res.partner.pet.kind"
    _order = "name"

    name = fields.Char(string="Name", required=True)
