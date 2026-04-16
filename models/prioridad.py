from odoo import models, fields


class GestionPrioridad(models.Model):
    _name = 'gestion.prioridad'
    _description = 'Prioridad de Solicitudes'
    _order = 'secuencia'

    name = fields.Char(string='Nombre', required=True)
    code = fields.Char(string='Código', required=True)
    secuencia = fields.Integer(string='Secuencia', default=10)
    description = fields.Text(string='Descripción')
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('unique_code', 'unique(code)', 'El código debe ser único')
    ]