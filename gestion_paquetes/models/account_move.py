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

class AccountMove(models.Model):
    _inherit = 'account.move.line'


    last_product_to_used = fields.Many2one(
        comodel_name='product.product',
        string='Last Product',
        related='move_id.last_product_to_used',
        required=False)

