# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vb_CustComm(models.Model):
    _inherit = ['account.invoice']
    
    @api.multi
    def vb_GetInvHead(self):
        query = """select ai.number, ai.date_invoice, ai.date_due, pm.name, ai.amount_tax, ai.amount_total, ai.amount_untaxed, ai.date, ai.name, cm.name
                     from account_invoice ai
                     inner join account_payment_term pm on pm.id = ai.payment_term_id
                     inner join res_partner cm on cm.id = ai.partner_id
                     where ai.date_invoice = current_date - interval '1 day'
                     """
        self.env.cr.execute(query)
        results = []
        for name, id in self.env.cr.fetchall():
            items = [name, id]
            results.append(items)
        print(results)
        return results

    @api.multi
    def vb_GetInvLine(self):
        query = """select ai.number, pt.name, sn.x_name, al.quantity, al.price_unit, al.sequence, al.price_total, price_subtotal, al.discount
                     from account_invoice ai
                     inner join account_invoice_line al on al.invoice_id = ai.id
                     inner join product_template pt on pt.id = al.product_id
                     left outer join x_seasons sn on sn.id = pt.x_studio_season_code
                     left outer join uom_uom um on um.id = al.uom_id
                     where ai.date_invoice = current_date - interval '1 day'
                     """
#        al.price_tax, 
        self.env.cr.execute(query)
        results = []
        for name, id in self.env.cr.fetchall():
            items = [name, id]
            results.append(items)
        print(results)
        return results
