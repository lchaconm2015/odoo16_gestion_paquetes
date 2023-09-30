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
        #
        # admission = request.env['op.admission']
        # obj_admission_register = request.env['op.admission.register'].sudo().search(
        #     [('state', '=', 'application'),
        #      ('company_id', '=', request.env['website'].get_current_website().company_id.id)])

        return request.render('gestion_paquetes.search_package_id',
                              {'mensaje': 'Su paquete se encuentra en nuestros almacenes de la Habana',

                               })
