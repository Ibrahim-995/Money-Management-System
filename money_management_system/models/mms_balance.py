from odoo import models, fields, api


class MoneyManagementSystemBalance(models.Model):
    _name = 'mms.balance'
    _description = 'Money Management System Balance'
    _rec_name = "available_balance"

    name = fields.Many2one('res.users', string="Name", default=lambda self: self.env.user)
    all_total_expense = fields.Monetary(string='Total Expense (All)', compute='_compute_all_total_expense', currency_field='currency_id')
    all_total_income = fields.Monetary(string='Total Income (All)', compute='_compute_all_total_income', currency_field='currency_id')
    available_balance = fields.Monetary(string='Available Balance', compute='_compute_available_balance',store=True, currency_field='currency_id')

    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)

    def refresh(self):
        pass

    @api.depends('all_total_expense')
    def _compute_all_total_expense(self):
        expenses = self.env['mms.expense'].search([])
        self.all_total_expense = sum(expenses.mapped('total_amount'))

    @api.depends('all_total_income')
    def _compute_all_total_income(self):
        incomes = self.env['mms.income'].search([])
        self.all_total_income = sum(incomes.mapped('total_amount'))

    @api.depends('all_total_expense', 'all_total_income')
    def _compute_available_balance(self):
        self.available_balance = self.all_total_income - self.all_total_expense
    