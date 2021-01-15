 #-*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime

class conv_model(models.Model):
    _name = 'convalidaciones.conv_model'
    _description = 'convalidaciones.conv_model'

    fecha = fields.Date(string="Fecha",required=True, default=datetime.today())
    modulo_id = fields.Many2one("convalidaciones.modulo_model", "Módulo")
    alumno_id = fields.Many2one("convalidaciones.alumno_model", "Alumno")