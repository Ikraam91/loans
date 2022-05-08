 -*- coding: utf-8 -*-

from odoo import models, fields, api


class loans(models.Model):
      _name = 'loans.loans'
      _description = 'loans Profile'
      _inherit = ['mail.thread', 'mail.activity.mixin']

     name = fields.Char(string='Name')
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    #description = fields.Text()

#  @api.depends('value')
  #  def _value_pc(self):
    #     for record in self:
         #    record.value2 = float(record.value) / 100
