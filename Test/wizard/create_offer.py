from odoo import api,fields,models

class CreateOfferWizard(models.TransientModel):
    _name = 'create.offer.wizard'
    _description = "wizard of Offer"

    name = fields.Char(string="name", required=True)
    property_type_id = fields.Many2one("estate.property.type", string="Type")

    def action_create_offer(self):
        print("button clicked")
'''from odoo import api, fields, models


class CreateOfferWizard(models.TransientModel):
    _name = 'create.offer.wizard'
    _description = "wizard of Offer"

    amount = fields.Float(string="Price")
    status = fields.Selection(string="Status", selection=[('accepted', 'Accepted'), ('refused', 'Refused')], copy=False)
    # partner_id = fields.Many2one('res.partner', required=True)
    validity = fields.Integer(string="Validity (days)", default="7")
    date_deadline = fields.Date(string="Deadline", compute="_compute_date", inverse="_inverse_date")

    def action_create_offer(self):
             vals = {
             'price': self.price,
             'validity': self.validate,
             'partner_id':self.partner_id,
             'date_deadline':self.date_deadline,
             'status':self.status
             }
             print("vals....", vals)
             self.env['estate.property.offer'].Create(vals)

    @api.depends("validity")
    def _compute_date(self):
        for rec in self:
            rec.date_deadline = fields.Datetime.add(rec.create_date.date(), days=rec.validity)

    def _inverse_date(self):
        fmt = '%Y-%m-%d'
        for rec in self:
            d1 = fields.datetime.strptime(str(rec.date_deadline), fmt)
            d2 = fields.datetime.strptime(str(rec.create_date.date()), fmt)
            diff = (d1 - d2).days
            rec.validity = str(diff)



'''