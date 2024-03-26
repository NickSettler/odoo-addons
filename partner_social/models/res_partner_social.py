from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResPartnerSocial(models.Model):
    _name = 'res.partner.social'
    _description = 'Social Network'
    _rec_name = 'name'
    _order = 'partner_id, social_type_id'

    name = fields.Char(string='Name')
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    social_type_id = fields.Many2one('res.partner.social.type', string='Type', required=True)
    value = fields.Char(string='Value', required=True)
    complete_url = fields.Char(string='Complete URL', compute='_compute_complete_url')

    def _compute_complete_url(self):
        for record in self:
            record.complete_url = record.social_type_id.get_url(record.value)
