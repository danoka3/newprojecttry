# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Library(models.Model):
    
    _name = "library.book"
    _description = "Library Info"
    
    
    name = fields.Char(string="Title" , required=True)
    descriptipn = fields.Text(string="Description")
    author = fields.Char(string="Author Name", required=True)
    editor = fields.Char(string="Editor")
    year_of_edition = fields.Date("Date")
    genre = fields.Selection(string="Genre",
                            selection=[("action","Action"),
                                      ("novel","Novel"),
                                      ("self-improvement","Self-improvement")],
                            copy=False)
    
    active = fields.Boolean(string="Active", default=True)