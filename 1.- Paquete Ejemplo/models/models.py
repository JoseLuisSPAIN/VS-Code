from odoo import models, fields

class test_usuario_model(models.Model):

    _name = 'test_usuario.model'
    _description = 'Esto es un ejemplo de modelo para ORM'

    nombre = fields.Char('Nombre')
    #prm_apellido = fields.Char('Primer Apellido')
    #sgn_apellido = fields.Char('Segundo Apellido')

    
