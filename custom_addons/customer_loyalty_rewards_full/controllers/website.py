from odoo import http
from odoo.http import request

class WebsiteLoyalty(http.Controller):

    @http.route('/my/loyalty', auth='user', website=True)
    def loyalty_portal(self):
        partner = request.env.user.partner_id
        points = request.env['loyalty.point'].sudo().search([('partner_id', '=', partner.id)], limit=1)
        rewards = request.env['loyalty.reward'].sudo().search([])
        history = request.env['loyalty.transaction'].sudo().search([('partner_id', '=', partner.id)], order="date desc", limit=20)
        return request.render('customer_loyalty_rewards.website_loyalty_page', {
            'partner': partner,
            'points': points,
            'rewards': rewards,
            'history': history,
        })