{
    "name": "Customer Loyalty: Points, Gifts, QR & Portal",
    "summary": "Tích điểm, đổi quà, quét QR và giao diện khách hàng",
    "version": "1.1",
    "category": "Sales",
    "author": "Thai Hoang GmbH",
    "license": "AGPL-3",
    "depends": ["base", "point_of_sale", "portal", "website"],
    "data": [
        "security/ir.model.access.csv",
        "views/loyalty_views.xml"
    ],
    "assets": {
        "point_of_sale.assets": [
            "customer_loyalty_gift_selector_advanced_qr/static/src/js/gift_selector_popup.js"
        ]
    },
    "installable": True,
    "application": True,
    "auto_install": False
}