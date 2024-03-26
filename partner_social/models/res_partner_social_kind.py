from odoo import models, fields


class ResPartnerSocialKind(models.Model):
    _name = 'res.partner.social.kind'
    _description = 'Social Network Kind'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    has_prefix = fields.Boolean(string='Has Prefix', default=True)
    has_suffix = fields.Boolean(string='Has Suffix', default=True)
    prefix = fields.Char(string='Prefix', help='Prefix for the social network kind. Example: https://')
    suffix = fields.Char(string='Suffix', help='Suffix for the social network kind. Example: @domain.com')
