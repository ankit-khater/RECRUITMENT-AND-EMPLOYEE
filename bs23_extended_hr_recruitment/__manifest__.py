{
    'name':'Extended HR Recuritment',
    'version':'1.0',
    'description': "Brain Station 32 extended Recuritment",
    'depends': ['base','hr','hr_recruitment'],
    'data': [
        'security/ir.model.access.csv',
        'security/hr_recruitment_security_extended.xml',
        'views/hr_applicant_form_view.xml',
        'views/hr_employee_form_view.xml'
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'


}