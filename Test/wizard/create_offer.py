from odoo import api,fields,models

class CreateOfferWizard(models.TransientModel):
    _name = 'create.offer.wizard'
    _description = "wizard of Offer"

    name = fields.Char(string="name",required=True)
    property_type_id = fields.Many2one("estate.property.type", string="Type")

    def action_create_offer(self):
        print("button clicked")
