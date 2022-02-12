from odoo import api,fields,models

class CreateOfferWizard(models.TransientModel):
     _name = "create.offer.wizard"  #estate_property
     _description = "Test Model"
    

     name = fields.Char(string="Title", required=True, tracking=True)
    