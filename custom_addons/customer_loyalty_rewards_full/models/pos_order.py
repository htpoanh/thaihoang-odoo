from odoo import models

class PosOrder(models.Model):
    _inherit = 'pos.order'

    def _create_order_picking(self):
        res = super()._create_order_picking()
        for order in self:
            if order.partner_id and order.amount_total:
                point_obj = self.env['loyalty.point'].sudo()
                record = point_obj.search([('partner_id', '=', order.partner_id.id)], limit=1)
                if record:
                    record.points += int(order.amount_total)
                else:
                    point_obj.create({'partner_id': order.partner_id.id, 'points': int(order.amount_total)})
                self.env['loyalty.transaction'].sudo().create({
                    'partner_id': order.partner_id.id,
                    'type': 'earn',
                    'points': int(order.amount_total),
                    'pos_order_id': order.id
                })
        return res