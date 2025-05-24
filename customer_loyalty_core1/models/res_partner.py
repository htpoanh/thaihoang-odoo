from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    loyalty_points = fields.Integer(string='Loyalty Points', default=0)
    customer_code = fields.Char(string='Customer Code', readonly=True)
