from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    membership_card = fields.Char(string="Membership Card Barcode")
    points_balance = fields.Integer(string="Points Balance", default=0)

class PointTransaction(models.Model):
    _name = 'point.transaction'
    _description = 'Point Transaction History'

    partner_id = fields.Many2one('res.partner', string="Customer")
    points = fields.Integer(string="Points Earned")
    transaction_date = fields.Datetime(string="Transaction Date", default=fields.Datetime.now)

class Reward(models.Model):
    _name = 'reward'
    _description = 'Reward Items'

    name = fields.Char(string="Reward Name")
    points_required = fields.Integer(string="Points Required")
