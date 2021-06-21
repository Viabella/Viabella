from odoo import models, api

class AccountInvoice(models.Model):
    _inherit = 'account.move'
    
    @api.model
    def vb_GetInvHead(self):
        query = """select am.name, am.invoice_date, am.invoice_date_due, pm.name, am.amount_tax, am.amount_total, am.amount_untaxed, am.date, am.name, cm.name
                     from account_move am
                     inner join account_payment_term pm on pm.id = ai.invoice_payment_term_id
                     inner join res_partner cm on cm.id = am.partner_id
                     where am.invoice_date = current_date - interval '1 day'
                     """
        self.env.cr.execute(query)
        results = []
        for name, id in self.env.cr.fetchall():
            items = [name, id]
            results.append(items)
        return results

    @api.model
    def vb_GetInvLine(self):
        query = """select am.name, pt.name, sn.x_name, aml.quantity, aml.price_unit, aml.sequence, aml.price_total, aml.price_subtotal, aml.discount
                     from account_move am
                     inner join account_move_line aml on aml.move_id = am.id
                     inner join product_template pt on pt.id = aml.product_id
                     left outer join x_seasons sn on sn.id = pt.x_studio_season_code
                     left outer join uom_uom um on um.id = aml.uom_id
                     where aml.invoice_date = current_date - interval '1 day'
                     """
        self.env.cr.execute(query)
        results = []
        for name, id in self.env.cr.fetchall():
            items = [name, id]
            results.append(items)
        return results
