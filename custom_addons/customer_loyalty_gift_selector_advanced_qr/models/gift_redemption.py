from odoo import models, fields, api

class GiftRedemption(models.Model):
    _name = 'gift.redemption'
    _description = 'Gift Redemption Log'

    partner_id = fields.Many2one('res.partner', string="Customer", required=True)
    gift_name = fields.Char(string="Gift Name", required=True)
    points_used = fields.Float(string="Points Used", required=True)
    date = fields.Datetime(string="Redemption Time", default=fields.Datetime.now)

    @api.model
    def redeem_gift(self, partner_id, gift_name, points):
        loyalty = self.env['customer.loyalty'].search([('partner_id', '=', partner_id)], limit=1)
        if loyalty and loyalty.points >= points:
            loyalty.points -= points
            self.create({
                'partner_id': partner_id,
                'gift_name': gift_name,
                'points_used': points
            })
            return True
        return False
