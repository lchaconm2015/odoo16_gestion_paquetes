# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    beneficiary_id = fields.Many2one(
        comodel_name='res.partner',
        string='Beneficiario',
        required=False)

    number_of_packages = fields.Integer(
        string='Cantidad de Paquetes',
        required=False)


