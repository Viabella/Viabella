from odoo import fields, models, _


class SaleSeason(models.Model):
    _name = "sale.season"
    _description = "Sales Season"
    _rec_name = "display_name"
    
    display_name = fields.Char(string='Display Name', compute='_compute_display_name')
    name = fields.Char(string='Season', required=True)
    code = fields.Char(string='Code', required=True)
    
    def _compute_display_name(self):
        for record in self:
            if record.name and record.code:
                record.display_name = f'{record.name} ({record.code})'
            else:
                record.display_name = _('New')