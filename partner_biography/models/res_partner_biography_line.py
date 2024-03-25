from odoo import models, fields, api


class ResPartnerBiographyLine(models.Model):
    _name = 'res.partner.biography.line'
    _description = 'Biography Line'
    _order = 'date desc'
    _rec_name = 'partner_id'

    biography_type = fields.Many2one('res.partner.biography.category.type', string='Biography Type', required=True)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    date = fields.Date(string='Date', required=True)

    related_partners_ids = fields.Many2many('res.partner', string='Related Partners')
    summary = fields.Char(string='Summary')
    notes = fields.Text(string='Notes')

    @api.depends(lambda self: (self._rec_name,) if self._rec_name else ())
    def _compute_display_name(self):
        for line in self:
            line.display_name = f"{line.partner_id.complete_name} / {line.biography_type.name}"
