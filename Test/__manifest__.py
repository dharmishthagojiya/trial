{
    'name': 'TestModule',
    'sequence': -100,
    'depends': ['base','mail'],
    'data': ['security/ir.model.access.csv',
             'views/estate_view.xml',
             'views/property_type.xml',
             'views/user.xml',
             "report/estate_reports.xml",
             "report/estate_report_views.xml",
             'wizard/create_offer_view.xml',
             ],
    "demo": [
        "data/estate_demo.xml"
    ],
    'application': 'True'
}
