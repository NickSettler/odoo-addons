import logging
from odoo import models, fields

_logger = logging.getLogger(__name__)

try:
    import vobject
except ImportError:
    _logger.warning(
        "`vobject` Python module not found, vcard file generation disabled. Consider installing this module if you want to generate vcard files")
    vobject = None


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

    def _build_vcard(self):
        vcard = super(Partner, self)._build_vcard()

        allowed_vcard_adr_types = ('home', 'school', 'work')

        if vcard.adr and self.type in allowed_vcard_adr_types:
            vcard.adr.type_param = self.type

        for child in self.child_ids:
            if child.type not in allowed_vcard_adr_types:
                continue
            adr = vcard.add('ADR')
            adr.value = vobject.vcard.Address(street=child.street or '', city=child.city or '', code=child.zip or '')
            if child.state_id:
                adr.value.region = child.state_id.name
            if child.country_id:
                adr.value.country = child.country_id.name

            adr.type_param = child.type

        return vcard
