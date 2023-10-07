from odoo import models, fields, api


class money_management_system(models.Model):
    _name = 'mms.expense'
    _description = 'money_management_system_expense'
    _rec_name = "total_amount"

    name = fields.Many2one('res.users', string="Name", default=lambda self: self.env.user)
    expense_date = fields.Date(string='Date', tracking=True)
    expense_category_line = fields.One2many('expense.category.line', 'expense_id', string="Expense Type")
    note = fields.Char(string="Note")
    total_amount = fields.Monetary(string='Total Amount', store=True, compute='_compute_total_amount', currency_field='currency_id')
    all_total_expense = fields.Monetary(string='Total Expense (All)', compute='_compute_all_total_expense', currency_field='currency_id')
    active = fields.Boolean(default=True)

    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)

    @api.depends('expense_category_line.amount')
    def _compute_total_amount(self):
        for expense in self:
            expense.total_amount = sum(expense.expense_category_line.mapped('amount'))

    @api.depends('total_amount')
    def _compute_all_total_expense(self):
        all_expenses = self.env['mms.expense'].search([])
        self.all_total_expense = sum(all_expenses.mapped('total_amount'))


class expenseCategories(models.Model):
    _name = 'expense.category.line'
    _description = 'expense Category Line'
    _rec_name = "category_id"

    expense_id = fields.Many2one('mms.expense', string='Expense', ondelete='cascade', inverse_name='expense_category_line')
    category_id = fields.Many2one('expense.category', string='Expense Type')
    amount = fields.Monetary(string='Amount', default=0.0, currency_field='currency_id')

    currency_id = fields.Many2one('res.currency', string='Currency', related='expense_id.currency_id', readonly=True)
