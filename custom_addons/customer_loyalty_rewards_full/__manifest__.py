{
    "name": "Customer Loyalty Rewards",
    "version": "1.0",
    "category": "Sales",
    "summary": "Tích điểm và đổi quà cho khách hàng",
    "description": "Module tích điểm, đổi quà, và tích hợp POS + App.",
    "depends": ["base", "point_of_sale", "website"],
    "data": [
        "security/ir.model.access.csv",
        "views/loyalty_point_views.xml",
        "views/loyalty_reward_views.xml",
        "views/res_partner_views.xml",
    ],
    "assets": {
        "point_of_sale.assets": [
            "customer_loyalty_rewards/static/src/js/pos_loyalty.js",
        ],
    },
    "installable": True,
    "application": True,
    "auto_install": False
}