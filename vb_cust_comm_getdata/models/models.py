# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class vb_cust_comm_getdata(models.Model):
#     _name = 'vb_cust_comm_getdata.vb_cust_comm_getdata'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100