# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vb_ProdComm(models.Model):
    _inherit = ['product.template']
    
    @api.multi
    def vb_GetProdID(self):
        query = """select pt.name, coalesce(rd.name, '')
                     from product_template pt
                     inner join ir_model_data rd on rd.model = 'product.template' and rd.res_id = pt.id
                     """
        self.env.cr.execute(query)
        results = []
        for des, id in self.env.cr.fetchall():
            items = [des, id]
            results.append(items)
        print(results)
        return results

    @api.multi
    def vb_GetProdOH(self):
        query = """select pt.name, sns.x_name, sl.name, pq.quantity - pq.reserved_quantity
                    from product_template pt
                    inner join stock_quant pq on pq.product_id = pt.id
                    inner join stock_location sl on sl.id = pq.location_id 
                    inner join x_seasons sns on sns.id = pt.x_studio_season_code
                    where sl.name <> 'Inventory adjustment' """
        self.env.cr.execute(query)
        results = []
        for prod, seas, locn, qty in self.env.cr.fetchall():
            items = [prod, seas, locn, qty]
            results.append(items)
        print(results)
        return results
    
#                        pt.barcode,
#                        pt.standard_price,
    @api.multi
    def vb_GetProdNewUpdates(self):
        query = """select coalesce(pt.name, ''), 
                        coalesce(sns.x_name,  ''),
                        coalesce(pc.name, ''),
                        coalesce(sbt.name, ''),
                        coalesce(pt.x_studio_retail_price, 0.00),
                        coalesce(pt.list_price, 0.00),
                        coalesce(um.name, ''),
                        coalesce(pt.x_studio_brand, ''),
                        coalesce(pt.x_studio_brand_sort, ''),
                        coalesce(pt.x_studio_changes_to_come, ''),
                        coalesce(pt.x_studio_country_of_origin, ''),
                        coalesce(pt.x_studio_catalog_sort, ''),
                        coalesce(pt.x_studio_ni_form_pop, false),
                        coalesce(pt.x_studio_3_panel, ''),
                        coalesce(pt.x_studio_short_fold, false),
                        coalesce(pt.x_studio_top_fold, ''),
                        coalesce(pt.x_studio_bow, ''),
                        coalesce(pt.x_studio_ribbon, ''),
                        coalesce(pt.x_studio_cord, ''),
                        coalesce(pt.x_studio_fabric, ''),
                        coalesce(pt.x_studio_flocking, ''),
                        coalesce(pt.x_studio_glitter, false),
                        coalesce(pt.x_studio_protective_sheet, false),
                        coalesce(pt.x_studio_shaker, false),
                        coalesce(pt.x_studio_varnish, ''),
                        coalesce(pt.x_studio_virko, false),
                        coalesce(pt.x_studio_acetate, ''),
                        coalesce(pt.x_studio_beads, ''),
                        coalesce(pt.x_studio_blind, false),
                        coalesce(pt.x_studio_cello, ''),
                        coalesce(pt.x_studio_dangler, false),
                        coalesce(pt.x_studio_puff, ''),
                        coalesce(pt.x_studio_glitterpuff_mix, ''),
                        coalesce(pt.x_studio_handmade, false),
                        coalesce(pt.x_studio_paper_type, ''),
                        coalesce(pt.x_studio_reuse_die, ''),
                        coalesce(pt.x_studio_sequins, ''),
                        coalesce(pt.x_studio_silkscreen, ''),
                        coalesce(pt.x_studio_vellum, ''),
                        coalesce(pt.x_studio_combo, ''),
                        case when pt.active = false then 'Archived' else 'Active' end
                    from product_template pt
                    inner join x_seasons sns on sns.id = pt.x_studio_season_code
                    inner join product_category pc on pc.id = pt.categ_id
                    left outer join uom_uom um on um.id = pt.uom_id
                    left outer join product_template sbt on sbt.id = pt.x_studio_sbt_item
                     """
        self.env.cr.execute(query)
        results = []
        for prod, seas, pcat, sbtitem, rprce, wprce, uom, brand, bsort, ctocom, contorig, catsort, niform, panel3, sfold, tfold, bbow, brib, ccord, ffab, flocking, glit, protsheet, shaker, varn, virk, acet, beads, blind, cello, dangl, puff, gpuff, hmade, ptype, reuse, seqns, sscreen, vellum, combo, actv in self.env.cr.fetchall():
            items = [prod, seas, pcat, sbtitem, rprce, wprce, uom, brand, bsort, ctocom, contorig, catsort, niform, panel3, sfold, tfold, bbow, brib, ccord, ffab, flocking, glit, protsheet, shaker, varn, virk, acet, beads, blind, cello, dangl, puff, gpuff, hmade, ptype, reuse, seqns, sscreen, vellum, combo, actv]
            results.append(items)
        print(results)
        return results

    @api.multi
    def vb_GetProdNewUpdates2(self):
        query = """select coalesce(pt.name, ''), 
                        coalesce(sns.x_name,  ''),
                        coalesce(pt.x_studio_catalog_values, ''),
                        coalesce(pt.x_studio_glitter_data, ''),
                        coalesce(pt.x_studio_glitter_data_2, ''),
                        coalesce(pt.x_studio_lasercut, ''),
                        coalesce(pt.x_studio_script_reference, ''),
                        coalesce(pt.x_studio_spot_color, ''),
                        coalesce(pt.x_studio_uv_gloss, ''),
                        coalesce(pt.x_studio_virko_data, ''),
                        coalesce(pt.x_studio_blind_data, ''),
                        coalesce(pt.x_studio_foil_color, ''),
                        coalesce(pt.x_studio_alt_foil_color, ''),
                        coalesce(pt.x_studio_ink_on_foil, ''),
                        coalesce(pt.x_studio_tip_in, ''),
                        coalesce(pt.x_studio_tip_on, ''),
                        coalesce(pt.x_studio_additional_info, '')
                        
                    from product_template pt
                    inner join x_seasons sns on sns.id = pt.x_studio_season_code
                     """
        self.env.cr.execute(query)
        results = []
        for prod, seas, catval, glitdat, glitdat2, lcut, sref, scol, uvgloss, virkdata, bdata, fcol, altfcol, inkfoil, tipin, tipon, addinfo in self.env.cr.fetchall():
            items = [prod, seas, catval, glitdat, glitdat2, lcut, sref, scol, uvgloss, virkdata, bdata, fcol, altfcol, inkfoil, tipin, tipon, addinfo]
            results.append(items)
        print(results)
        return results
        
    @api.multi
    def vb_GetProdNewUpdates3(self):
        query = """select coalesce(pt.name, ''), 
                        coalesce(sns.x_name,  ''),
                        coalesce(pt.default_code, ''),
                        coalesce(pt.x_studio_gems, ''),
                        coalesce(pp.barcode, ''),
                        coalesce(ir.value_float, 0.00)
                    from product_template pt
                    inner join x_seasons sns on sns.id = pt.x_studio_season_code
                    left outer join product_product pp on pp.product_tmpl_id = pt.id
                    left outer join ir_property ir on replace(ir.res_id, 'product.product,', '') = cast(pp.id as varchar)
                     """
        self.env.cr.execute(query)
        results = []
        for prod, seas, descr, gems, bcode in self.env.cr.fetchall():
            items = [prod, seas, descr, gems, bcode]
            results.append(items)
        print(results)
        return results

    @api.multi
    def vb_ListInactItem(self):
        query = """select coalesce(pt.name, ''), 
                        coalesce(sns.x_name,  ''),
                        coalesce(pt.default_code, ''),
                        coalesce(pt.x_studio_gems, '')                      
                    from product_template pt
                    inner join x_seasons sns on sns.id = pt.x_studio_season_code
                    where pt.active = FALSE
                     """
        self.env.cr.execute(query)
        results = []
        for prod, seas, descr, gems in self.env.cr.fetchall():
            items = [prod, seas, descr, gems]
            results.append(items)
        print(results)
        return results

    @api.multi
    def vb_GetProdSBT(self):
        query = """select pt.name, coalesce(sbt.name, ''), coalesce(aa.code, ''), coalesce(xs.x_name, '')
                    from product_template pt
                    left outer join product_template sbt on sbt.id = pt.x_studio_sbt_item
                    left outer join x_seasons xs on xs.id = pt.x_studio_season_code
                    left outer join ir_property ir on replace(ir.res_id, 'product.template,', '') = cast(pt.id as varchar) and ir.name = 'property_account_income_id'
                    left outer join account_account aa on replace(ir.value_reference, 'account.account,', '') = cast(aa.id as varchar)
                    where pt.active = TRUE """
        self.env.cr.execute(query)
        results = []
        for prod, tname, sls, seas in self.env.cr.fetchall():
            items = [prod, tname, sls, seas]
            results.append(items)
        print(results)
        return results
    
    @api.multi
    def vb_GetProdAccts(self):
        query = """select pt.name, coalesce(aa.code, '')
                    from product_template pt
                    left outer join ir_property ir on replace(ir.res_id, 'product.template,', '') = cast(pt.id as varchar) and ir.name = 'property_account_income_id'
                    left outer join account_account aa on replace(ir.value_reference, 'account.account,', '') = cast(aa.id as varchar)
                    where pt.active = TRUE and pt.name = '000-09129-001' """
        self.env.cr.execute(query)
        results = []
        for prod, prc in self.env.cr.fetchall():
            items = [prod, prc]
            results.append(items)
        print(results)
        return results
    
