# -*- coding: utf-8 -*-
# © 2016 Akretion (Alexis de Lattre <alexis.delattre@akretion.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class ViettelSInvoiceType(models.Model):
    _name = 'viettel.sinvoice.type'
    _description = 'Viettel S-Invoice Type'
    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    description = fields.Char(string='Description')