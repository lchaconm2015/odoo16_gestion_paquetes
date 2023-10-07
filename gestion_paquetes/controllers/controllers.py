# -*- coding: utf-8 -*-

from odoo import http, tools, _, SUPERUSER_ID
from odoo.http import content_disposition, Controller, request, route
import logging
import datetime
from odoo.exceptions import ValidationError, UserError

_logger = logging.getLogger(__name__)


class CustomPortal(http.Controller):

    @http.route('/search_package', type='http', auth='user', website=True)
    def search_package(self, **kw):
        '''Create admission '''

        return request.render('gestion_paquetes.search_package_id',
                              {
                              })

    @route(['/search_package/submit'], type='http', auth='user', website=True)
    def search_package_submit(self, redirect=None, **post):
        mensaje = ''
        show_detail = False
        obj_stock_quant = None
        package_number = ''
        shipping_addres = ''
        invoice_number = ''
        partner = None
        location = None

        if 'package_number' in post:
            obj_product_template = request.env['product.template'].sudo().search(
                [('name', '=', post['package_number'])])
            if obj_product_template:
                mensaje = 'Su paquete fue encontrado en nuestro sistema'
                show_detail = True
                partner = None
                shipping_addres = ''

                obj_account_move = request.env['account.move'].search(
                    [('id', '=', obj_product_template.invoice_related_id.id)])

                partner = obj_account_move.partner_id.name

                package_number = obj_product_template.name
                shipping_addres = obj_account_move.partner_shipping_id.street
                location = obj_product_template.location_country.name
                invoice_number = obj_account_move.name
                package_state = obj_product_template.package_state
            else:
                mensaje = 'Su paquete no fue encontrado en nuestros almacenes, rectifique su número de paquete.'

        return request.render('gestion_paquetes.search_package_id',
                              {'mensaje': mensaje, 'package_number': package_number,
                               'shipping_addres': shipping_addres, 'invoice_number': invoice_number,
                               'partner_name': partner, 'location': location, 'show_detail': show_detail,'package_state':package_state})
