# -*- coding: utf-8 -*-

from odoo import models, fields, api

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
    
    ısbn_no = fields.Integer("Isbn No")