from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    nego_id = fields.Many2one(
        'res.users',
        string='Nego',
        tracking=True,
    )
    driver_id = fields.Many2one(
        'res.users',
        string='Driver',
        tracking=True,
    )