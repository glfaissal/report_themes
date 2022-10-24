# -*- coding: utf-8 -*-

{
    'name': 'Odoo Professional Report Themes',
    'version': '15.0.0.0',
    'category': 'Tools',
    'license': 'OPL-1',
    'summary': '',
    'description': "",
    'license':'OPL-1',
    'author': 'Adiclas',
    'live_test_url':'#',
    'website': '#',
    'depends': ['base', 'account', 'sale', 'purchase', 'stock', 'sale_stock', 'base_vat','sale_management','purchase_stock'],
    'data': [

        "res_company.xml",

        "invoice_report/fency_report_account.xml",
        "invoice_report/fency_report_invoice.xml",
        "invoice_report/report_invoice_classic.xml",
        "invoice_report/report_invoice_modern.xml",
        "invoice_report/report_invoice_odoo_standard.xml",

        "delivery_report/stock_report_classic.xml",
        "delivery_report/fency_report_deliveryslip.xml",
        "delivery_report/modern_report_deliveryslip.xml",
        "delivery_report/odoo_standard_report_deliveryslip.xml",
        "delivery_report/report_deliveryslip_classic.xml",


        "purchase_report/classic_report_purchaseorder.xml",
        "purchase_report/classic_report_purchasequotation.xml",
        "purchase_report/fency_report_purchaseorder.xml",
        "purchase_report/fency_report_purchasequotation.xml",
        "purchase_report/modern_report_purchaseorder.xml",
        "purchase_report/modern_report_purchasequotation.xml",
        "purchase_report/odoo_standard_report_purchaseorder.xml",
        "purchase_report/odoo_standard_report_purchasequotation.xml",

        "sale_report/classic_report_saleorder.xml",
        "sale_report/fency_report_saleorder.xml",
        "sale_report/modern_report_saleorder.xml",
        "sale_report/odoo_standard_report_saleorder.xml",
             ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'live_test_url':'#',
    "images":['static/description/Banner.png'],
}
