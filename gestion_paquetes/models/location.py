# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Location(models.Model):
    _name = 'paq_location'
    _description = 'Location'

    name = fields.Char()
    code = fields.Char(
        string='Código',
        required=False)
    address = fields.Char(
        string='Dirección',
        required=False)
