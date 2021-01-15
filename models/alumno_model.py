# -*- coding: utf-8 -*-
from odoo import models, fields, api
from random import choice
from odoo.exceptions import ValidationError

class alumno_model(models.Model):
    _name = 'convalidaciones.alumno_model'
    _description = 'convalidaciones.alumno_model'

    name = fields.Char(string="Nombre", required=True, index=True)
    password = fields.Char(string="Contraseña", required=False, index=True,default="000")
    foto = fields.Binary()
    edad = fields.Integer(string="Edad", required=True, index=True)
    localidad = fields.Char(string="Localidad", required=True, index=True)
    provincia = fields.Char(string="Provincia", required=True, index=True)
    email = fields.Char(string="Email", required=True, index=True)
    convalidaciones = fields.One2many("convalidaciones.conv_model","alumno_id",string="Convalidaciones")
    profesores = fields.Many2many("convalidaciones.profesor_model",string="Profesores")

    @api.constrains("edad")
    def _comprueba_edad(self):
        if self.edad < 14:
            raise ValidationError("La edad no puede ser menor de 14!")

    def generaPass(self):
        self.ensure_one()
        longitud = 10
        valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        p = ""
        p = p.join([choice(valores) for i in range(longitud)])
        self.password = p
        return True
