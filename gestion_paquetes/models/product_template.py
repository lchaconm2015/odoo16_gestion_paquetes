# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.product'

    is_package  = fields.Boolean(
        string='Es un paquete',
        required=False)
