from odoo import models, fields

class LoyaltyHistory(models.Model):
    _name = 'loyalty.history'
    _description = 'Loyalty Point History'

    partner_id = fields.Many2one('res.partner', string="Customer", required=True)
    change = fields.Integer(string="Point Change", required=True)
    reason = fields.Char(string="Reason")
    date = fields.Datetime(string="Date", default=fields.Datetime.now)
    origin = fields.Char(string="Origin")
