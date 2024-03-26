from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ResPartnerSocialType(models.Model):
    _name = 'res.partner.social.type'
    _description = 'Social Network Type'
    _rec_name = 'name'
    _order = 'name'

    name = fields.Char(string='Name', required=True)
    kind_id = fields.Many2one('res.partner.social.kind', string='Kind')
    template = fields.Char(string='Template',
                           help='Template for the value. Use {value} as a placeholder for the value. Can be left empty if the value is a complete value.')

    def get_url(self, value):
        self.ensure_one()

        return "{prefix}{value}{suffix}".format(
            prefix=self.kind_id.has_prefix and self.kind_id.prefix or '',
            value=self.template.format(value=value) if self.template else value,
            suffix=self.kind_id.has_suffix and self.kind_id.suffix or ''
        )

    @api.constrains('template')
    def _check_template(self):
        for record in self:
            if record.template and '{value}' not in record.template:
                raise ValidationError('Template must contain the placeholder {value}')
