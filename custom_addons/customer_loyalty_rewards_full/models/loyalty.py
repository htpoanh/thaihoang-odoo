from odoo import models, fields, api

class LoyaltyPoint(models.Model):
    _name = 'loyalty.point'
    _description = 'Customer Loyalty Points'

    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    points = fields.Integer(string='Points')
    company_id = fields.Many2one('res.company', default=lambda self: self.env.company)

class LoyaltyReward(models.Model):
    _name = 'loyalty.reward'
    _description = 'Loyalty Reward'

    name = fields.Char(string='Reward Name', required=True)
    points_cost = fields.Integer(string='Points Required', required=True)
    product_id = fields.Many2one('product.product', string='Reward Product')

class LoyaltyTransaction(models.Model):
    _name = 'loyalty.transaction'
    _description = 'Loyalty Transactions Log'

    partner_id = fields.Many2one('res.partner', string='Customer')
    reward_id = fields.Many2one('loyalty.reward', string='Reward')
    type = fields.Selection([('earn', 'Earn'), ('redeem', 'Redeem')], required=True)
    points = fields.Integer()
    date = fields.Datetime(default=fields.Datetime.now)
    pos_order_id = fields.Many2one('pos.order', string='POS Order')