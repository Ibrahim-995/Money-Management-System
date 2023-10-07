# -*- coding: utf-8 -*-
{
    'name': "Money Management System",

    'summary': """
        Money management system""",

    'description': """
        Calculate Mone Income and Expense
    """,

    'author': "Ibrahim Khalil Ullah",
    'website': "http://www.daffodilvarsity.com",

    
    'category': 'Management System',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/mms_category.xml',
        'views/mms_menu.xml',
        'views/mms_income.xml',
        'views/mms_expense.xml',
        'views/mms_balance_dashboard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'license': 'LGPL-3',
}
