from odoo import models, fields


class ResPartnerBiographyCategoryType(models.Model):
    _name = 'res.partner.biography.category.type'
    _description = 'Biography Category Type'
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    biography_category_id = fields.Many2one('res.partner.biography.category', string='Biography Category')
