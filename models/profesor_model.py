# -*- coding: utf-8 -*-
from odoo import models, fields, api
from random import choice
from datetime import datetime
from odoo.exceptions import ValidationError

class profesor_model(models.Model):
    _name = 'convalidaciones.profesor_model'
    _description = 'convalidaciones.profesor_model'

    name = fields.Char(string="Nombre", required=True, index=True)
    apellidos = fields.Char(string="Apellidos", required=True, index=True) 
    foto = fields.Binary()
    DNI = fields.Char(string="DNI", required=True, index=True)
    alumnos = fields.Many2many("convalidaciones.alumno_model",string="Alumnos")
    numAlumnos = fields.Char(string="Número alumnos", compute="_calcAlumnos",store=True)


    @api.depends("alumnos")
    def _calcAlumnos(self):
        self.numAlumnos = len(self.alumnos)
   
    @api.constrains("DNI")
    def _comprueba_dni(self):

        letras = "TRWAGMYFDPXBNJZSQVHLCKE"
        while True:
           
            letra = self.DNI[-1]
            num = int(self.DNI[0:8])
            if letras[num%23]==letra:
                
                break
            else:
                raise ValidationError("DNI no válido!")

            

    def validaDni(self):
        self.ensure_one()
        longitud = 10
        valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        p = ""
        p = p.join([choice(valores) for i in range(longitud)])
        self.password = p
        return True
