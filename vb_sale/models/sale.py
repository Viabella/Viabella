from odoo import models, api, fields, _
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    state = fields.Selection(selection_add=[('on_hold', 'On Hold')])
    
    def action_confirm(self):
        invalid_orders = self.filtered(lambda o: not o.with_context(active_test=False).partner_id.active)
        if invalid_orders:
            raise ValidationError (_(f"You cannot confirm this order because customer {invalid_orders[0].with_context(active_test=False).partner_id.name} was archived"))
        return super().action_confirm()
    
    def action_on_hold(self):
        self.ensure_one()
        self.update({'state': 'on_hold'})
        
    def action_unhold(self):
        self.ensure_one()
        self.update({'state': 'sale'})
        
    @api.model
    def get_orders(self, **kwargs):
        orders = self.search([('state', '=', kwargs.get('state', False))])
        return orders.read()
    
    def get_order_detail(self, **kwargs):
        self.ensure_one()
        return {field: self[field] for field in kwargs.get('fields', [])}