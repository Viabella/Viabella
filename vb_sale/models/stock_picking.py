from odoo import models, _
from odoo.exceptions import ValidationError

class StockPicking(models.Model):
    _inherit = "stock.picking"
    
    def button_validate(self):
        invalid_pickings = self.filtered(lambda p: not p.with_context(active_test=False).partner_id.active)
        if invalid_pickings:
            raise ValidationError (_(f"You cannot validate this picking because customer {invalid_pickings[0].with_context(active_test=False).partner_id.name} was archived"))
        invalid_pickings = self.filtered(lambda p: p.sale_id.state == 'on_hold')
        if invalid_pickings:
            raise ValidationError (_(f"You cannot validate this picking because order {invalid_pickings[0].sale_id.name} was on-hold"))
        return super().action_confirm()