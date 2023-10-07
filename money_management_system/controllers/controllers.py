# -*- coding: utf-8 -*-
# from odoo import http


# class MoneyManagementSystem(http.Controller):
#     @http.route('/money_management_system/money_management_system', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/money_management_system/money_management_system/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('money_management_system.listing', {
#             'root': '/money_management_system/money_management_system',
#             'objects': http.request.env['money_management_system.money_management_system'].search([]),
#         })

#     @http.route('/money_management_system/money_management_system/objects/<model("money_management_system.money_management_system"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('money_management_system.object', {
#             'object': obj
#         })
