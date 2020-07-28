# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vb_CustComm(models.Model):
    _inherit = ['res.partner']
    
    @api.multi
    def vb_GetCustID(self):
        query = """select coalesce(rp.name, ''), coalesce(ir.name, '')
                     from res_partner rp
                     inner join ir_model_data ir on ir.model = 'res.partner' and ir.res_id = rp.id
                     """
        self.env.cr.execute(query)
        results = []
        for name, id in self.env.cr.fetchall():
            items = [name, id]
            results.append(items)
        print(results)
        return results

    @api.multi
    def vb_GetCustNewUpdates(self):
        query = """select coalesce(rp.name, ''),
                     coalesce(rp.x_studio_company_name, ''),
                     coalesce(rp.x_studio_home_office, ''),
                     coalesce(rp.street, ''),
                     coalesce(rp.street2, ''),
                     coalesce(rp.city, ''),
                     coalesce(st.name, ''),
                     coalesce(rp.zip, ''),
                     coalesce(rp.x_studio_merchandiser_freq_1, ''),
                     coalesce(rp.x_studio_everyday_time_1, 0.00),
                     coalesce(rp.x_studio_seasonal_time, 0.00),
                     coalesce(rp.x_studio_ed_footage, ''),
                     coalesce(rp.x_studio_seasonal_footage, ''),
                     coalesce(rp.x_studio_competitor_pockets, 0),
                     coalesce(rp.x_studio_account_manager, ''),
                     coalesce(rp.x_studio_seas_guarantee_, 0.00),
                     coalesce(rp.x_studio_program, ''),
                     coalesce(rp.x_studio_sales_agreement_exp_date, '2001-01-01'),
                     coalesce(rp.x_studio_owner_name, ''),
                     coalesce(rp.x_studio_ap_contact, ''),
                     coalesce(pt.name, '')
                     from res_partner rp
                     left outer join ir_property ir on replace(ir.res_id, 'res.partner,', '') = cast(rp.id as varchar)
                     left outer join account_payment_term pt on replace(ir.value_reference, 'account.payment.term,', '') = cast(pt.id as varchar)
                     left outer join res_country_state st on st.id = rp.state_id
                     where rp.customer = TRUE and (rp.parent_id is null or rp.parent_id = 0) and rp.name is not null and rp.name <> ''
                     """
#                     left outer join ir_property ir on ir.res_id = 'res.partner,' + cast(rp.id as varchar(20))
#                     left outer join account_payment_term pt on 'account.payment.term,' + cast(pt.id as varchar(20)) = ip.value_reference
        self.env.cr.execute(query)
        results = []
        for name, comp, hoff, st1, st2, cit, stte, zp, mfreq, edtime, stime, edfoot, sfoot, cpock, amanag, sguar, prgm, saed, oname, apcon, pterm in self.env.cr.fetchall():
            items = [name, comp, hoff, st1, st2, cit, stte, zp, mfreq, edtime, stime, edfoot, sfoot, cpock, amanag, sguar, prgm, saed, oname, apcon, pterm]
            results.append(items)
        print(results)
        return results

    @api.multi
    def vb_GetCustNewUpdates2(self):
        query = """select coalesce(rp.name, ''),
                     coalesce(sp.x_studio_company_name, ''),
                     coalesce(sp.street, ''),
                     coalesce(sp.street2, ''),
                     coalesce(sp.city, ''),
                     coalesce(s1.name, ''),
                     coalesce(sp.zip, ''),
                     coalesce(rp.x_studio_inactive_category, ''),
                     coalesce(rp.x_studio_inactive_reason, ''),
                     coalesce(rp.phone, ''),
                     coalesce(rp.email, ''),
                     coalesce(rp.x_studio_reactivation_date, '2001-01-01'),
                     coalesce(rp.active, TRUE),
                     coalesce(rp.x_studio_segment_group, ''),
                     coalesce(rl0.category_id, 0),
                     coalesce(rl1.category_id, 0),
                     coalesce(rl2.category_id, 0),
                     coalesce(rl3.category_id, 0),
                     coalesce(rl4.category_id, 0),
                     coalesce(rl5.category_id, 0),
                     coalesce(rl6.category_id, 0),
                     coalesce(rl7.category_id, 0),
                     coalesce(rl8.category_id, 0),
                     coalesce(rl9.category_id, 0),
                     coalesce(rl10.category_id, 0),
                     coalesce(rl11.category_id, 0),
                     coalesce(rl12.category_id, 0),
                     coalesce(rl13.category_id, 0),
                     coalesce(rl14.category_id, 0)
                     from res_partner rp
                     left outer join res_country_state st on st.id = rp.state_id
                     left outer join res_partner sp on sp.parent_id = rp.id
                     left outer join res_country_state s1 on s1.id = sp.state_id
                     left outer join res_partner_res_partner_category_rel rl0 on rl0.partner_id = rp.id and rl0.category_id = 11
                     left outer join res_partner_res_partner_category_rel rl1 on rl1.partner_id = rp.id and rl1.category_id = 12
                     left outer join res_partner_res_partner_category_rel rl2 on rl2.partner_id = rp.id and rl2.category_id = 9
                     left outer join res_partner_res_partner_category_rel rl3 on rl3.partner_id = rp.id and rl3.category_id = 7
                     left outer join res_partner_res_partner_category_rel rl4 on rl4.partner_id = rp.id and rl4.category_id = 15
                     left outer join res_partner_res_partner_category_rel rl5 on rl5.partner_id = rp.id and rl5.category_id = 3
                     left outer join res_partner_res_partner_category_rel rl6 on rl6.partner_id = rp.id and rl6.category_id = 5
                     left outer join res_partner_res_partner_category_rel rl7 on rl7.partner_id = rp.id and rl7.category_id = 13
                     left outer join res_partner_res_partner_category_rel rl8 on rl8.partner_id = rp.id and rl8.category_id = 10
                     left outer join res_partner_res_partner_category_rel rl9 on rl9.partner_id = rp.id and rl9.category_id = 1
                     left outer join res_partner_res_partner_category_rel rl10 on rl10.partner_id = rp.id and rl10.category_id = 2
                     left outer join res_partner_res_partner_category_rel rl11 on rl11.partner_id = rp.id and rl11.category_id = 4
                     left outer join res_partner_res_partner_category_rel rl12 on rl12.partner_id = rp.id and rl12.category_id = 6
                     left outer join res_partner_res_partner_category_rel rl13 on rl13.partner_id = rp.id and rl13.category_id = 14
                     left outer join res_partner_res_partner_category_rel rl14 on rl14.partner_id = rp.id and rl14.category_id = 8
                     where rp.customer = TRUE and (rp.parent_id is null or rp.parent_id = 0) and rp.name is not null and rp.name <> ''
                     """
#                     inner join res_partner_res_partner_category_rel rl on rl.partner_id = rp.id
#                    inner join res_partner_category rc on rc.id = rl.category_id
        self.env.cr.execute(query)
        results = []
        for name, stname, shst1, shst2, shcit, shstte, shzp, incat, inreas, phn, eml, react, isact, seggrp, cated, catseas, cleanps, incomp, isho, keyac, mercds, mchg, nopush, plano, rscp, sbt, sloc, taxem, useupc in self.env.cr.fetchall():
            items = [name, stname, shst1, shst2, shcit, shstte, shzp, incat, inreas, phn, eml, react, isact, seggrp, cated, catseas, cleanps, incomp, isho, keyac, mercds, mchg, nopush, plano, rscp, sbt, sloc, taxem, useupc]
            results.append(items)
        print(results)
        return results

    @api.multi
    def vb_CustAR_AP(self):
        query = """select coalesce(rp.name, ''), coalesce(acr.code, ''), coalesce(acp.code, '')
                     from res_partner rp 
                     left outer join ir_property irr on replace(irr.res_id, 'res.partner,', '') = cast(rp.id as varchar) and irr.value_reference like 'account.account%' and irr.name = 'property_account_receivable_id'
                     left outer join ir_property irp on replace(irp.res_id, 'res.partner,', '') = cast(rp.id as varchar) and irp.value_reference like 'account.account%' and irp.name = 'property_account_payable_id'
                     left outer join account_account acr on replace(irr.value_reference, 'account.account,', '') = cast(acr.id as varchar) 
                     left outer join account_account acp on replace(irp.value_reference, 'account.account,', '') = cast(acp.id as varchar) 
                     """
        self.env.cr.execute(query)
        results = []
        for name, arcode, apcode in self.env.cr.fetchall():
            items = [name, arcode, apcode]
            results.append(items)
        print(results)
        return results

    @api.multi
    def vb_TestCustAR_AP(self):
        query = """select ir.name, ir.res_id, coalesce(ir.value_reference, ''), coalesce(rp.name, '')
                     from ir_property ir
                     inner join res_partner rp on cast(rp.id as varchar) = replace(ir.res_id, 'res.partner,', '')
                     where ir.res_id like 'res.partner%' and ir.name like '%account%'
                     order by ir.name
                     """
        self.env.cr.execute(query)
        results = []
        for name, id, ref, rname in self.env.cr.fetchall():
            items = [name, id, ref, rname]
            results.append(items)
        print(results)
        return results

    @api.multi
    def vb_GetSBTCustBranch(self):
        query = """select coalesce(rp.name, ''), coalesce(rp.x_studio_branch_number, ''), coalesce(acr.code, ''), coalesce(acp.code, '')
                     from res_partner rp
                     inner join res_partner_res_partner_category_rel rl11 on rl11.partner_id = rp.id and rl11.category_id = 4
                     inner join res_partner_category rc on rc.id = rl11.category_id
                     left outer join ir_property irr on replace(irr.res_id, 'res.partner,', '') = cast(rp.id as varchar) and irr.value_reference like 'account.account%' and irr.name = 'property_account_receivable_id'
                     left outer join ir_property irp on replace(irp.res_id, 'res.partner,', '') = cast(rp.id as varchar) and irp.value_reference like 'account.account%' and irp.name = 'property_account_payable_id'
                     left outer join account_account acr on replace(irr.value_reference, 'account.account,', '') = cast(acr.id as varchar) 
                     left outer join account_account acp on replace(irp.value_reference, 'account.account,', '') = cast(acp.id as varchar) 
                     where rp.active = TRUE and rc.name is not null and rc.name <> ''
                     """
        self.env.cr.execute(query)
        results = []
        for name, bnum, arc, apc in self.env.cr.fetchall():
            items = [name, bnum, arc, apc]
            results.append(items)
        print(results)
        return results

