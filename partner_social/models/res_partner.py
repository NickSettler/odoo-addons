from odoo import models, fields, api


class Partner(models.Model):
    _name = "res.partner"
    _inherit = 'res.partner'

    social_ids = fields.One2many('res.partner.social', 'partner_id', string='Social Networks')
    social_count = fields.Integer(compute='_compute_social_count', string='Social Networks Count')

    @api.depends('social_ids')
    def _compute_social_count(self):
        for partner in self:
            partner.social_count = len(partner.social_ids)
