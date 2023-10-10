# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    def _compute_last_product(self):
        move = self.search([('state', '=', 'posted')], order='create_date desc', limit=1)
        if move:
            return move.invoice_line_ids[0].product_id.id
        else:
            return None

    number_of_packages = fields.Integer(
        string='Cantidad de Paquetes',
        required=False)
    last_product_to_used = fields.Many2one(
        comodel_name='product.product',
        string='Last Product',
        default=_compute_last_product,
        required=False)

    package_related_ids = fields.One2many(
        comodel_name='product.template',
        inverse_name='invoice_related_id',
        string='Paquetes Relacionados',
        required=False)
    package_count = fields.Integer(string="Count", copy=False, compute="_compute_package_count")

    def generate_package(self):
        line_count = 0
        for line in self.invoice_line_ids:
            line_count = line_count + 1
            line.create_new_product(
                str('P-') + str(line.move_id.name[-10:].replace('/', '-')) + str('-') + str(line_count))

    def _compute_package_count(self):
        for rec in self:
            rec.package_count = len(rec.package_related_ids)

    def action_view_package(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Paquetes',
            'view_mode': 'kanban',
            'res_model': 'product.template',
            'view_id': self.env.ref('gestion_paquetes.package_kanban_view').id,
            'domain': [('invoice_related_id', '=', self.id)],
            'context': "{'create': False}"
        }

    class AccountMoveLine(models.Model):
        _inherit = 'account.move.line'

        is_package = fields.Boolean(
            string='Es un apaquete',
            related='product_id.is_package',
            required=False)
        package_weight = fields.Float(
            string='Peso del Paquete en libras', default=1.0,
            required=False)

        last_product_to_used = fields.Many2one(
            comodel_name='product.product',
            string='Last Product',
            related='move_id.last_product_to_used',
            required=False)

        @api.onchange('package_weight', 'quantity')
        def _onchange_package_weight(self):
            for line in self:
                line.price_unit = line.quantity * line.package_weight * line.product_id.lst_price

        def create_new_product(self, product_name):
            '''This method create a new producto for every line in account move line, '''
            object_product_template = self.env['product.product'].create(
                {'name': product_name, 'detailed_type': 'product', 'is_package': True,
                 'invoice_related_id': self.move_id.id, 'responsable_id': self.env.user.id})

            return object_product_template
