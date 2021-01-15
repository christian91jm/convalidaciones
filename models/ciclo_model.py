 #-*- coding: utf-8 -*-
from odoo import models, fields, api


class ciclo_model(models.Model):
    _name = 'convalidaciones.ciclo_model'
    _description = 'convalidaciones.ciclo_model'
    #restricciones donde se involucran varios registros
    _sql_constraints = [("ciclos_name_uniq","UNIQUE(name)","No puede haber dos ciclos con el mismo nombre!"),]

    name = fields.Char(string="Ciclo", required="True", index="True", help="Nombre del ciclo")
    descripcion = fields.Html(string="Descripción", help="Contenido del ciclo")
    modulos = fields.One2many("convalidaciones.modulo_model","ciclo",string="Módulos")


