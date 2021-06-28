from odoo import models, api, fields, _

class BarcodeLabel(models.Model):
    _name = "barcode.label"
    _description = 'Barcode Label'
    
    from_name = fields.Char(string='From Name')
    from_address = fields.Char(string='From Address')
    from_city = fields.Char(string='From City')
    from_state_id = fields.Many2one('res.country.state', string='From State', domain="[('country_id.code', '=', 'US')]")
    from_zip = fields.Char(string='From Zip')
    
    ship_to_name = fields.Char(string='Ship To Name')
    ship_to_address = fields.Char(string='Ship To Address')
    ship_to_city = fields.Char(string='Ship To City')
    ship_to_state_id = fields.Many2one('res.country.state', string='Ship To State', domain="[('country_id.code', '=', 'US')]")
    ship_to_zip = fields.Char(string='Ship To Zip')
    
    carrier_name = fields.Char(string='Carrier Name')
    po_number = fields.Char(string='PO#')
    dpci = fields.Char(string='DPCI')
    case_pack = fields.Integer(string='Casepack', default=1)
    description = fields.Char(string='Description')
    sscc = fields.Char(string='SSCC')
    
    