from odoo import models, fields


class GestionCategoria(models.Model):
    _name = 'gestion.categoria'
    _description = 'Categoría de Solicitudes'
    _order = 'name'

    name = fields.Char(string='Nombre', required=True)
    code = fields.Char(string='Código', required=True)
    description = fields.Text(string='Descripción')
    active = fields.Boolean(default=True)

    _sql_constraints = [
        ('unique_code', 'unique(code)', 'El código debe ser único')
    ]