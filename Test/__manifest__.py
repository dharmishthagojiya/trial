{
    'name': 'TestModule',
    'sequence': -100,
    'depends': ['base','mail'],
    'data': ['security/ir.model.access.csv', 
             'views/estate_view.xml',
             'views/property_type.xml',
             'views/user.xml',
             'wizard/create_offer.py'
             ],
    'application': 'True'
}
