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
        if 'package_number' in post:
            obj_stock_quant = request.env['stock.quant'].sudo().search(
                [('product_id.name', '=', post['package_number']),
                 ('company_id', '=', request.env['website'].get_current_website().company_id.id),
                 ('inventory_quantity_auto_apply', '=', 1)])
            if obj_stock_quant:
                mensaje = 'Su paquete fue encontrado en nuestro sistema'
                show_detail = True
            else:
                mensaje = 'Su paquete no fue encontrado en nuestros almacenes, rectifique su número de paquete.'
            partner = None
            shipping_addres = ''
            object_stock_picking = request.env['stock.picking'].search([('product_id.name', '=', post['package_number'])])
            obj_account_move = request.env['account.move'].search(
                [('invoice_picking_id.id', '=', object_stock_picking.id)])

            partner = obj_account_move.partner_id.name

            package_number = obj_stock_quant.product_id.name
            shipping_addres = obj_account_move.partner_shipping_id.street
            location = obj_stock_quant.location_id.name
            invoice_number = obj_account_move.name

        return request.render('gestion_paquetes.search_package_id',
                              {'mensaje': mensaje, 'package_number': package_number,
                               'shipping_addres': shipping_addres, 'invoice_number': invoice_number,
                               'partner_name': partner, 'location': location, 'show_detail': show_detail})
