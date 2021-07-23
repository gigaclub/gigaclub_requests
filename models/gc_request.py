from odoo import fields, models, api


class GCRequest(models.Model):
    _name = 'gc.request'
    _description = 'GigaClub Request'

    receiver_id = fields.Reference(selection=[("gc.user", "gc.user")])
    sender_id = fields.Reference(selection=[("gc.user", "gc.user")])
    state = fields.Selection(selection=[("waiting", "Waiting"), ("accepted", "Accepted"), ("denied", "Denied")])
