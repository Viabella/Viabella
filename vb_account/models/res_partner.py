from odoo import models, api, fields

class ResPartner(models.Model):
    _inherit = "res.partner"
    
    season_guarantee_pecentage = fields.Float(string='Season Gurantee Percentage')
    
    @api.model
    def _commercial_fields(self):
        fields = super()._commercial_fields()
        if fields:
            fields += ['active']
        else:
            fields = ['active']
        return fields    
    
    def get_company_name(self):
        self.ensure_one()
        company_name = self.name
        if not self.is_company:
            record = self.search([('id', 'parent_of', self.id), ('is_company', '=', True)], limit=1)
            company_name = record.name
        return company_name