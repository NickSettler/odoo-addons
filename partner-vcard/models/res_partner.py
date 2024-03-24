from odoo import models


class Partner(models.Model):
    _name = "res.partner"
    _inherit = 'res.partner'

    def _build_vcard(self):
        vcard = super(Partner, self)._build_vcard()

        if self.birthdate_date:
            bday = vcard.add('BDAY')
            bday.value = str(self.birthdate_date)

        return vcard
