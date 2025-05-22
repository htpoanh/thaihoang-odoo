{
    "name": "A-Point Loyalty Program",
    "summary": "Customer loyalty points management across Thái Hoàng company business units",
    "version": "1.0",
    "category": "Sales",
    "author": "Your Company",
    "website": "https://yourcompany.example",
    "license": "AGPL-3",
    "depends": ["base", "sale_management", "point_of_sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "views/a_point_views.xml",
        "data/a_point_data.xml"
    ],
    "installable": true,
    "application": false,
    "auto_install": false
}
