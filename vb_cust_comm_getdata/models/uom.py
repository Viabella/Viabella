from odoo import models, api

class Uom(models.Model):
    _inherit = 'uom.uom'
    
    @api.model
    def vb_GetUOMID(self):
        query = """select ai.name, coalesce(ir.name, '')
                     from uom_uom ai
                     left outer join ir_model_data ir on ir.model = 'uom.uom' and ir.res_id = ai.id
                     where ai.active = TRUE
                     """
        self.env.cr.execute(query)
        results = []
        for name, id in self.env.cr.fetchall():
            items = [name, id]
            results.append(items)
        return results
