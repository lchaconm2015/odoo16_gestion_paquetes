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

    responsable_id = fields.Many2one(
        comodel_name='res.users',
        string='Responsable',
        required=False)

    location_province = fields.Char(
        string='Ubicación (Provincia)',
        required=False)
    location_country = fields.Many2one(
        comodel_name='res.country',
        string='Ubicación (País)',
        required=False)
    package_state = fields.Selection(
        string='Estado del Paquete',
        selection=[('empaquetado', 'Empaquetado'),
                   ('transportandose', 'Transportándose'),
                   ('recibido', 'Recibido por el despachador'),
                   ('entregado', 'Entregado al destinatario'),
                   ],
        required=False, )
