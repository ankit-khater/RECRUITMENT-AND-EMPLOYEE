import string
from odoo import models,fields,api

class Employee(models.Model):
    _inherit = "hr.employee"

    emergency_contact_ids = fields.One2many('emergency.contact.line', 'employee_id',string='Emergency Contacts')
    educations_line_ids = fields.One2many('applicant.education.line', 'emp_id',string='Educations')