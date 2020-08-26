# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vb_ProdComm(models.Model):
    _inherit = ['product.product']
    
    @api.multi
    def vb_GetPProdID(self):
        query = """select coalesce(pi.name), coalesce(rd.name, '')
                     from product_product pt
                     left outer join product_template pi on pi.id = pt.id
                     left outer join ir_model_data rd on rd.model = 'product.product' and rd.res_id = pt.id
                     """
        self.env.cr.execute(query)
        results = []
        for des, id in self.env.cr.fetchall():
            items = [des, id]
            results.append(items)
        print(results)
        return results

