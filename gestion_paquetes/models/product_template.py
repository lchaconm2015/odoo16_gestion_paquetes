# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_package = fields.Boolean(
        string='Es un paquete',
        required=False)

    invoice_related_id = fields.Many2one(
        comodel_name='account.move',
        string='Factura de Origen',
        required=False)
