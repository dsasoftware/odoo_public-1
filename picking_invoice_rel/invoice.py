# -*- coding: utf-8 -*-
# #############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2011 Tiny SPRL (<http://tiny.be>).
#    Copyright (C) 2011 Camptocamp Austria (<http://www.camptocamp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from osv import fields, orm


class AccountInvoice(orm.Model):
    _inherit = "account.invoice"

    _columns = {
        'picking_ids': fields.many2many('stock.picking', 'picking_invoice_rel', 'invoice_id', 'picking_id', 'Pickings'),
        'sale_order_ids': fields.many2many('sale.order', 'sale_order_invoice_rel', 'invoice_id', 'order_id',
                                           'Sale Orders', readonly=True,
                                           help="This is the list of sale orders linked to this invoice. "),
    }

    def copy(self, cr, uid, id, default=None, context=None):
        """

        :param cr:
        :param uid:
        :param id:
        :param default:
        :param context:
        :return:
        """
        default = default or {}
        default.update({
            'picking_ids': [],
            'sale_order_ids': [],
        })
        return super(AccountInvoice, self).copy(
            cr, uid, id, default=default, context=context)
                            

