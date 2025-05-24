from odoo import models, fields

class GiftItem(models.Model):
    _name = 'gift.item'
    _description = 'Redeemable Gift'

    name = fields.Char(string='Gift Name', required=True)
    points_required = fields.Integer(string='Points Required', required=True)
    available_qty = fields.Integer(string='Available Quantity')
    description = fields.Text(string='Description')
