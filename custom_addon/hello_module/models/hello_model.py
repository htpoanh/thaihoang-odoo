from odoo import models, fields

class HelloModel(models.Model):
    _name = 'hello.model'
    _description = 'Hello Thai Hoang'

    name = fields.Char(string="Tên thương hiệu", required=True)
