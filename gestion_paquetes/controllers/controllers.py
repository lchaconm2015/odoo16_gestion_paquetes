# -*- coding: utf-8 -*-
# from odoo import http


# class GestionPaquetes(http.Controller):
#     @http.route('/gestion_paquetes/gestion_paquetes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_paquetes/gestion_paquetes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_paquetes.listing', {
#             'root': '/gestion_paquetes/gestion_paquetes',
#             'objects': http.request.env['gestion_paquetes.gestion_paquetes'].search([]),
#         })

#     @http.route('/gestion_paquetes/gestion_paquetes/objects/<model("gestion_paquetes.gestion_paquetes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_paquetes.object', {
#             'object': obj
#         })
