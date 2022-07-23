# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Library(models.Model):
    
    _name = "library.book"
    _description = "Library Info"
    
    
    name = fields.Char(string="Title" , required=True)
    description = fields.Text(string="Description")
    author = fields.Char(string="Author Name", required=True)
    editor = fields.Char(string="Editor")
    year_of_edition = fields.Date(string="Year Of Edition")
    genre = fields.Selection(string="Genre",
                            selection=[("action","Action"),
                                      ("novel","Novel"),
                                      ("self-improvement","Self-improvement")],
                            copy=False)
    
    active = fields.Boolean(string="Active", default=True)
    
    notes = fields.Text(string="Notes")
    
    ısbn_no = fields.Char("Isbn No", size=13, default='-')
    
@api.onchange('ısbn_no')
def _check_ısbn_no(self):
    if len(self.ısbn_no) < 13:
        raise ValidationError('ISBN No cannot be less than 13 lenght')
   
       

            
     
            
        