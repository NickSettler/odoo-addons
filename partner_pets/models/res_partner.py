from odoo import models, fields, api


class Partner(models.Model):
    _name = "res.partner"
    _inherit = 'res.partner'

    pets_count = fields.Integer(string="Number of Pets", compute='_compute_pets_count')
    pets = fields.One2many('res.partner.pet', 'owner_id', string="Pets", auto_join=True, search=False, copy=False)

    @api.depends('pets')
    def _compute_pets_count(self):
        for partner in self:
            partner.pets_count = len(partner.pets)

    def action_view_pets(self):
        for contact in self:
            relation_model = self.env['res.partner.pet']
            relations = relation_model.search([('owner_id', '=', contact.id)])
            action = self.env["ir.actions.act_window"]._for_xml_id("partner_pets.action_res_partner_pet_all")
            action['domain'] = [('id', 'in', relations.ids)]
            context = action.get("context", "{}").strip()[1:-1]
            elements = context.split(",") if context else []
            to_add = [
                """
                'search_default_owner_id': {0},
                'default_owner_id': {0},
                'active_model': 'res.partner',
                'active_id': {0},
                'active_ids': [{0}],
                """.format(contact.id)
            ]
            context = "{" + ", ".join(elements + to_add) + "}"
            action['context'] = context
            return action
