from odoo import models, fields


class Partner(models.Model):
    _name = "res.partner"
    _inherit = 'res.partner'

    _complete_name_displayed_types = ('invoice', 'delivery', 'other', 'home', 'school', 'work')

    type = fields.Selection(selection_add=[
        ('home', 'Home Address'),
        ('school', 'School Address'),
        ('work', 'Work Address'),
    ], )

    def _get_complete_name(self):
        self.ensure_one()

        displayed_types = self._complete_name_displayed_types
        type_description = dict(self._fields['type']._description_selection(self.env))

        name = self.name or ''
        if self.company_name or self.parent_id:
            if not name and self.type in displayed_types:
                name = type_description[self.type]

            name = f"{self.commercial_company_name or self.sudo().parent_id.name}, {name}"
        return name.strip()
