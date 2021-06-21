from odoo import models, fields

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"
    
    invoice_date = fields.Date(related='move_id.invoice_date', store=True, readonly=True)
    season_id = fields.Many2one(related='product_id.season_id', store=True, readonly=True)
    