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
        if 'package_number' in post:
            obj_stock_quant = request.env['stock.quant'].sudo().search(
                [('product_id.name', '=', post['package_number']),
                 ('company_id', '=', request.env['website'].get_current_website().company_id.id)])
            if obj_stock_quant:
                mensaje = 'Su paquete se encuentra en nuestra ubicacion de:{}'.format(obj_stock_quant.location_id.name)
            else:
                mensaje = 'Su paquete no fue encontrado en nuestros almacenes, rectifique su número de paquete.'

        return request.render('gestion_paquetes.search_package_id',
                              {'mensaje': mensaje})
