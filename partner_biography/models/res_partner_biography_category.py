from odoo import models, fields, api


class ResPartnerBiographyCategory(models.Model):
    _name = 'res.partner.biography.category'
    _description = 'Biography Category'
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    biography_types_ids = fields.One2many('res.partner.biography.category.type', 'biography_category_id',
                                          string='Biography Types')
    biography_types_count = fields.Integer(compute='_compute_biography_types_count', string='Biography Types Count')

    @api.depends('biography_types_ids')
    def _compute_biography_types_count(self):
        for category in self:
            category.biography_types_count = len(category.biography_types_ids)
