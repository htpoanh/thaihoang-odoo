from odoo import http
from odoo.http import request

class LoyaltyAPI(http.Controller):

    @http.route('/api/loyalty/points', auth='public', type='json', methods=['POST'])
    def get_points(self, **kwargs):
        partner_id = kwargs.get('partner_id')
        partner = request.env['res.partner'].sudo().browse(int(partner_id))
        points = request.env['loyalty.point'].sudo().search([('partner_id', '=', partner.id)], limit=1)
        return {"points": points.points if points else 0}

    @http.route('/api/loyalty/rewards', auth='public', type='json', methods=['GET'])
    def list_rewards(self):
        rewards = request.env['loyalty.reward'].sudo().search_read([], ['name', 'points_cost'])
        return {"rewards": rewards}

    @http.route('/api/loyalty/redeem', auth='public', type='json', methods=['POST'])
    def redeem_reward(self, **kwargs):
        partner_id = int(kwargs['partner_id'])
        reward_id = int(kwargs['reward_id'])

        reward = request.env['loyalty.reward'].sudo().browse(reward_id)
        points = request.env['loyalty.point'].sudo().search([('partner_id', '=', partner_id)], limit=1)
        if not points or points.points < reward.points_cost:
            return {"success": False, "message": "Không đủ điểm"}

        points.points -= reward.points_cost
        request.env['loyalty.transaction'].sudo().create({
            'partner_id': partner_id,
            'reward_id': reward_id,
            'type': 'redeem',
            'points': reward.points_cost
        })
        return {"success": True, "message": "Đổi quà thành công"}