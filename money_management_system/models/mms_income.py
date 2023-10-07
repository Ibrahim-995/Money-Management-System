from odoo import models, fields, api


class money_management_system(models.Model):
    _name = 'mms.income'
    _description = 'money_management_system_income'
    _rec_name = "total_amount"

    name = fields.Many2one('res.users', string="Name", default=lambda self: self.env.user)
    income_date = fields.Date(string='Date', tracking=True)
    income_category_line = fields.One2many('income.category.line', 'income_id', string="Income Type")
    note = fields.Char(string="Note")
    total_amount = fields.Monetary(string='Total Amount', store=True, compute='_compute_total_amount', currency_field='currency_id')
    all_total_income = fields.Monetary(string='Total Income (All)', compute='_compute_all_total_income', currency_field='currency_id')
    active = fields.Boolean(default=True)


    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)

    @api.depends('income_category_line.amount')
    def _compute_total_amount(self):
        for income in self:
            income.total_amount = sum(income.income_category_line.mapped('amount'))

    @api.depends('total_amount')
    def _compute_all_total_income(self):
        all_incomes = self.env['mms.income'].search([])
        self.all_total_income = sum(all_incomes.mapped('total_amount'))


class IncomeCategories(models.Model):
    _name = 'income.category.line'
    _description = 'Income Category Line'
    _rec_name = "category_id"

    income_id = fields.Many2one('mms.income', string='Income', ondelete='cascade', inverse_name='income_category_line')
    category_id = fields.Many2one('income.category', string='Income Type')
    amount = fields.Monetary(string='Amount', default=0.0, currency_field='currency_id')

    currency_id = fields.Many2one('res.currency', string='Currency', related='income_id.currency_id', readonly=True)
