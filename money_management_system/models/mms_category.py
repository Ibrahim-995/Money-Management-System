# -*- coding: utf-8 -*-

from odoo import models, fields, api


class money_management_income_category(models.Model):
    _name = 'income.category'
    _description = 'money_management_system_income'

    name = fields.Char(string = "Name")
    note = fields.Char(string = "Note")
    active = fields.Boolean(default=True)



class money_management_espense_category(models.Model):
    _name = 'expense.category'
    _description = 'money_management_system_expense'

    name = fields.Char(string = "Name")
    note = fields.Char(string = "Note")
    active = fields.Boolean(default=True)