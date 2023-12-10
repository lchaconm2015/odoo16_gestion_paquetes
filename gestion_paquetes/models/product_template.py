# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools
from odoo.modules import get_module_resource
import base64
from odoo.modules.module import get_module_resource


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

    paq_location_id = fields.Many2one(
        comodel_name='paq_location',
        string='Ubicación',
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

    @api.onchange('paq_location_id')
    def _onchange_paq_location_id(self):
        if self.package_state != 'entregado':
            self.package_state = 'transportandose'

    @api.model
    def _get_default_image_value(self):
        image = False
        img_path = get_module_resource('l16_gestion_paquetes', 'static/img', 'paquete.png')  # your default image path
        if img_path:
            with open(img_path, 'rb') as f:  # read the image from the path
                image = f.read()
        if image:  # if the file type is .jpg then you don't need this whole if condition.
            image = tools.image_colorize(image)
        return tools.image_resize_image_big(base64.b64encode(image))

    def _default_image(self):
        image_path = get_module_resource('gestion_paquetes', 'static/img', 'paquete.png')
        return base64.b64encode(open(image_path, 'rb').read())

    @api.model
    def create(self, vals):
        if vals.get('is_package'):
            vals['image_1920'] = self._default_image()
        return super(ProductTemplate, self).create(vals)

    # def write(self, vals):
    #      result = super(ProductTemplate, self).write(vals)
    #      if vals.get('location_id'):
    #        stage_rec = self.env['crm.stage'].search([('id ', '=', vals.get('stage_id'))], limit=1)
    #        if stage_rec:
    #
    #      return result
