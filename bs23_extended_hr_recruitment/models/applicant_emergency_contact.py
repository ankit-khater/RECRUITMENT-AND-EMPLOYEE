import string
from odoo import models,fields,api

class Applicant(models.Model):
    _inherit = "hr.applicant"

    emergency_contact_ids = fields.One2many('emergency.contact.line', 'applicant_id',string='Emergency Contact')
    educations_line_ids = fields.One2many('applicant.education.line', 'applicants_id',string='Educations')

    def create_employee_from_applicant(self):
        res = super(Applicant,self).create_employee_from_applicant()
        context={}
        emergency_contact_list = []
        for emc in self.emergency_contact_ids:
            emergency_contact_list.append((0,0,{
                'name':emc.name,
                'address':emc.address,
                'phone':emc.phone,
            }))

        context['default_emergency_contact_ids'] = emergency_contact_list
        edu_list = []
        for edu in self.educations_line_ids:
            edu_list.append((0,0,{
                'institute': edu.institute,
                'degree_type_id': edu.degree_type_id.id,
                'passing_year' : edu.passing_year
            }))  
        context['default_educations_line_ids'] = edu_list  
        res['context'] = context    
        return res



class HrApplicant(models.Model):
    _name = 'emergency.contact.line'
    _description = 'Emeregency Contact of Applicant'

    name = fields.Char(string = 'Name')
    address = fields.Text(string = 'Address')
    phone = fields.Char(string = 'Phone')
    applicant_id = fields.Many2one('hr.applicant', string='Applicants Id')
    employee_id = fields.Many2one('hr.employee', string='Employee Id')

class ApplicantEducationsLine(models.Model):
    _name = 'applicant.education.line'    
    _description = 'Applicant Education Line'

    institute = fields.Char(string='Institute')
    degree_type_id = fields.Many2one('hr.recruitment.degree',string='Degree')
    passing_year = fields.Char(string='Passing Year')
    applicants_id = fields.Many2one('hr.applicant',string='Applicants Id')
    emp_id = fields.Many2one('hr.employee',string='Employee Id')


    