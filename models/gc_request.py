from odoo import fields, models, api
from odoo.exceptions import ValidationError


class GCRequest(models.Model):
    _name = 'gc.request'
    _description = 'GigaClub Request'

    receiver_id = fields.Reference(selection=[("gc.user", "gc.user")])
    sender_id = fields.Reference(selection=[("gc.user", "gc.user")])
    state = fields.Selection(selection=[("waiting", "Waiting"), ("accepted", "Accepted"), ("denied", "Denied")])

    @api.constrains("receiver_id", "sender_id", "state")
    def _check_duplicate_request(self):
        for record in self:
            for compareRec in self.search([("id", "!=", record.id)]):
                if record.receiver_id == compareRec.receiver_id and record.sender_id == compareRec.sender_id and record.state == "waiting" and record.state == compareRec.state:
                    raise ValidationError("waiting requests should be unique!")
