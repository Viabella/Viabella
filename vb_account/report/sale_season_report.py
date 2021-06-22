from odoo import tools
from odoo import fields, models
from odoo.tools import float_round
import logging

class SaleSeasonReport(models.Model):
    _name = "sale.season.report"
    _description = "Sales Season Report"
    _auto = False
    _rec_name = 'season_id'
    _order = 'invoice_date desc'

    season_id = fields.Many2one('sale.season', string='Season', readonly=True)
    invoice_date = fields.Date('Invoice Date', readonly=True)
    partner_id = fields.Many2one('res.partner', string='Customer', readonly=True)
    company_name = fields.Char(string='Company' , compute='_compute_company_name')
    qty_sold = fields.Float(string='Qty Sold', readonly=True)
    sold_amount = fields.Monetary(string='$ Wholesale', readonly=True)
    qty_returned = fields.Float(string='Qty Returned', readonly=True)
    returned_amount = fields.Monetary(string='$ Returned', readonly=True)
    sell_through = fields.Float(string='Sell Thru %', compute='_compute_sell_thru')
    
    prior_qty_sold = fields.Float(string='PY Qty Sold',  compute='_compute_prior_year_data')
    prior_sold_amount = fields.Monetary(string='PY $ Wholesale', compute='_compute_prior_year_data')
    prior_qty_returned = fields.Float(string='PY Qty Returned', compute='_compute_prior_year_data')
    prior_returned_amount = fields.Monetary(string='PY $ Returned', compute='_compute_prior_year_data')    
    season_guarantee_pecentage = fields.Float(related='partner_id.season_guarantee_pecentage')
    account_move_line_id = fields.Many2one('account.move.line', string='Account Move Line', readonly=True)
    selected_year = fields.Integer(string='Year', search='_search_selected_year', compute='_compute_selected_year')
    currency_id = fields.Many2one(related='account_move_line_id.currency_id')
    
    def _compute_company_name(self):
        for record in self:
            record.company_name = record.partner_id.company_name or record.partner_id.get_company_name()
            
    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        with_ = ("WITH %s" % with_clause) if with_clause else ""

        # select_ = """
        #     aml.id as id,
        #     aml.id as account_move_line_id,
        #     aml.partner_id as partner_id,
        #     aml.season_id as season_id ,
        #     aml.invoice_date as invoice_date,
        #     CASE WHEN date_part('year', aml.invoice_date) = date_part('year', CURRENT_DATE) AND aml.credit > 0 THEN sum(aml.quantity) ELSE 0 END as qty_sold,
        #     CASE WHEN aml.invoice_date + interval '1' year >= date_trunc('year', CURRENT_DATE) AND  aml.invoice_date + interval '1' year < CURRENT_DATE  AND aml.credit > 0 THEN sum(aml.quantity) ELSE 0 END as prior_qty_sold,
        #     CASE WHEN date_part('year', aml.invoice_date) = date_part('year', CURRENT_DATE) AND aml.debit > 0 THEN sum(aml.quantity) ELSE 0 END as qty_returned,
        #     CASE WHEN aml.invoice_date + interval '1' year >= date_trunc('year', CURRENT_DATE) AND  aml.invoice_date + interval '1' year < CURRENT_DATE  AND aml.debit > 0 THEN sum(aml.quantity) ELSE 0 END as prior_qty_returned,
        #     CASE WHEN date_part('year', aml.invoice_date) = date_part('year', CURRENT_DATE) AND aml.credit > 0 THEN sum(aml.price_total) ELSE 0 END as sold_amount,
        #     CASE WHEN aml.invoice_date + interval '1' year >= date_trunc('year', CURRENT_DATE) AND  aml.invoice_date + interval '1' year < CURRENT_DATE  AND aml.credit > 0 THEN sum(aml.price_total) ELSE 0 END as prior_sold_amount,
        #                 CASE WHEN date_part('year', aml.invoice_date) = date_part('year', CURRENT_DATE) AND aml.debit > 0 THEN sum(aml.price_total) ELSE 0 END as returned_amount,
        #     CASE WHEN aml.invoice_date + interval '1' year >= date_trunc('year', CURRENT_DATE) AND  aml.invoice_date + interval '1' year < CURRENT_DATE  AND aml.debit > 0 THEN sum(aml.price_total) ELSE 0 END as prior_returned_amount
        # """
        select_ = """
            aml.id as id,
            aml.id as account_move_line_id,
            aml.partner_id as partner_id,
            aml.season_id as season_id ,
            aml.invoice_date as invoice_date,
            CASE WHEN aml.credit > 0 THEN sum(aml.quantity) ELSE 0 END as qty_sold,
            CASE WHEN aml.debit > 0 THEN sum(aml.quantity) ELSE 0 END as qty_returned,
            CASE WHEN aml.credit > 0 THEN sum(aml.price_total) ELSE 0 END as sold_amount,
            CASE WHEN aml.debit > 0 THEN sum(aml.price_total) ELSE 0 END as returned_amount
        """
        for field in fields.values():
            select_ += field

        from_ = """
                account_move_line aml
                WHERE aml.season_id IS NOT NULL AND aml.partner_id
        """ 

        groupby_ = """
            account_move_line_id,
            aml.partner_id,
            aml.season_id,
            aml.invoice_date
            %s
        """ % (groupby)

        return '%s (SELECT %s FROM %s GROUP BY %s)' % (with_, select_, from_, groupby_)

    def init(self):
        # self._table = sale_report
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (%s)""" % (self._table, self._query()))

    def _compute_sell_thru(self):
        for record in self:
            if record.sold_amount and record.sold_amount > 0:
                record.sell_through = float_round((record.sold_amount - record.returned_amount) / record.sold_amount, 2) * 100
            else:
                record.sell_through = 0
                
    def _search_selected_year(self, operator, value):
        start_date = f'{value}-01-01'
        end_date = f'{value}-12-31'
        ids = self.search([('invoice_date', '>=', start_date), ('invoice_date', '<=', end_date)]).ids
        return [('id', 'in', ids)]
            
    def _compute_selected_year(self):
        for record in self:
            record.selected_year = record.invoice_date.year
            
    def _compute_prior_year_data(self):
        seasons = self.mapped('season_id')
        partners = self.mapped('partner_id')
        ids = self.mapped('account_move_line_id').ids
        current_year = self[0].invoice_date.year if self else fields.Date.today().year
        start_date = f'{current_year - 1}-01-01'
        end_date = f'{current_year - 1}-12-31'
        datas = self.env['account.move.line'].search_read(domain=[('season_id.id', 'in', seasons.ids),
                                                  ('partner_id.id', 'in', partners.ids), 
                                                  ('id', 'not in', ids),
                                                  ('invoice_date', '>=', start_date), 
                                                  ('invoice_date', '<=', end_date)],
                                                 fields=['season_id', 'invoice_date', 'debit', 'credit', 
                                                         'quantity', 'price_total',
                                                         'partner_id'])
        for record in self:
            data = filter(lambda e: e['season_id'][0] == record.season_id.id 
                          and e['partner_id'][0] == record.partner_id.id
                          and fields.Datetime.from_string(e['invoice_date']).year == fields.Datetime.from_string(record.invoice_date).year - 1, datas)
            prior_credit = filter(lambda e: e['credit'] > 0, data)
            prior_debit = filter(lambda e: e['debit'] > 0, data)
            price_total = sum(map(lambda e: e['price_total'], prior_credit))
            record.prior_qty_sold = sum(map(lambda e: e['quantity'], prior_credit))
            record.prior_sold_amount = price_total
            record.prior_qty_returned = sum(map(lambda e: e['quantity'], prior_debit))
            record.prior_returned_amount = sum(map(lambda e: e['price_total'], prior_debit))