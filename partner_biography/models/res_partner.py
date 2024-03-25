from odoo import models, fields, api


class Partner(models.Model):
    _name = "res.partner"
    _inherit = 'res.partner'

    biography_lines_ids = fields.One2many('res.partner.biography.line', 'partner_id', string='Biography Lines')
    biography_lines_count = fields.Integer(compute='_compute_biography_lines_count', string='Biography Lines Count')

    @api.depends('biography_lines_ids')
    def _compute_biography_lines_count(self):
        for partner in self:
            partner.biography_lines_count = len(partner.biography_lines_ids)

    def action_view_biography_lines(self):
        for contact in self:
            relation_model = self.env['res.partner.biography.line']
            relations = relation_model.search([('partner_id', '=', contact.id)])
            action = self.env["ir.actions.act_window"]._for_xml_id("partner_biography.res_partner_biography_lines_action")
            action['domain'] = [('id', 'in', relations.ids)]
            context = action.get("context", "{}").strip()[1:-1]
            elements = context.split(",") if context else []
            to_add = [
                """
                'search_default_partner_id': {0},
                'default_partner_id': {0},
                'active_model': 'res.partner',
                'active_id': {0},
                'active_ids': [{0}],
                """.format(contact.id)
            ]
            context = "{" + ", ".join(elements + to_add) + "}"
            action['context'] = context
            return action
