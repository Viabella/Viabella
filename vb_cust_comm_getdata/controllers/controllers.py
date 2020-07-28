# -*- coding: utf-8 -*-
from odoo import http

# class VbCustCommGetdata(http.Controller):
#     @http.route('/vb_cust_comm_getdata/vb_cust_comm_getdata/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vb_cust_comm_getdata/vb_cust_comm_getdata/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vb_cust_comm_getdata.listing', {
#             'root': '/vb_cust_comm_getdata/vb_cust_comm_getdata',
#             'objects': http.request.env['vb_cust_comm_getdata.vb_cust_comm_getdata'].search([]),
#         })

#     @http.route('/vb_cust_comm_getdata/vb_cust_comm_getdata/objects/<model("vb_cust_comm_getdata.vb_cust_comm_getdata"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vb_cust_comm_getdata.object', {
#             'object': obj
#         })