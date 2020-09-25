# © 2018 Fanha (Fanha Giang <fanha99@hotmail.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api, _
import requests
import json
from odoo.exceptions import UserError

class ResCompany(models.Model):
    _inherit = 'res.company'

    vsi_domain = fields.Char()
    vsi_tin = fields.Char()
    vsi_username = fields.Char()
    vsi_password = fields.Char()
    vsi_template = fields.Char()
    vsi_series = fields.Char()
    vsi_type = fields.Many2one('viettel.sinvoice.type', 'Invoice Type')

    def check_vsi_server(self):
        headers = {"Content-type": "application/json; charset=utf-8"}
        company_id = self
        api_url = company_id.vsi_domain + '/InvoiceAPI/InvoiceUtilsWS/getProvidesStatusUsingInvoice'

        data = {
            "supplierTaxCode": company_id.vsi_tin,
            "pattern": company_id.vsi_template,
            "serial": company_id.vsi_series,
        }

        # jsondata = json.dumps(data)
        result = requests.post(api_url, json=data, headers=headers, auth=(company_id.vsi_username, company_id.vsi_password))

        if result.status_code == 200:
            output = json.loads(result.text)
            if not output['errorCode'] and not output['description']:
                raise UserError("Số hóa đơn đã sử dụng %s / %s" % (output['numOfpublishInv'], output['totalInv']))
            else:
                raise UserError("%s\n%s" % (output['errorCode'], output['description']))
        else:
            raise UserError("Lỗi Kết Nối: %s" % (result.status_code))
