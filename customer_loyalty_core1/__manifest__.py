{
    "name": "Customer Loyalty Core",
    "version": "1.0",
    "depends": ["base", "contacts"],
    "author": "Thai Hoang GmbH",
    "category": "Marketing",
    "description": "Core loyalty logic: points, gifts, history",
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "views/loyalty_history_views.xml",
        "views/gift_item_views.xml"
    ],
    "installable": True,
    "application": False
}
