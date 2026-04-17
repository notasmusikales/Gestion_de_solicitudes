from odoo import models, fields, api
from odoo.exceptions import UserError


class GestionSolicitud(models.Model):
    _name = 'gestion.solicitud'
    _description = 'Gestión de Solicitudes'
    _order = 'id desc'

    name = fields.Char(string="Número", readonly=True, default='Nuevo', copy=False)
    partner_id = fields.Many2one('res.partner', string='Solicitante', required=True)
    categoria_id = fields.Many2one('gestion.categoria', string='Categoría', required=True)
    prioridad_id = fields.Many2one('gestion.prioridad', string='Prioridad', required=True)
    descripcion = fields.Text(string='Descripción', required=True)
    state = fields.Selection([
        ('nuevo', 'Nuevo'),
        ('en_proceso', 'En Proceso'),
        ('resuelto', 'Resuelto'),
        ('cerrado', 'Cerrado'),
        ('cancelado', 'Cancelado'),
    ], string='Estado', default='nuevo', required=True)
    assigned_to = fields.Many2one('res.users', string='Asignado a')
    date_deadline = fields.Date(string='Fecha Límite')
    date_created = fields.Datetime(string='Fecha Creación', default=fields.Datetime.now, readonly=True)
    date_resolved = fields.Datetime(string='Fecha Resolución', readonly=True)
    note = fields.Text(string='Notas Internas')
    attachment_ids = fields.Many2many('ir.attachment', string='Adjuntos')

    @api.model
def create(self, vals):
    if vals.get('name', 'Nuevo') == 'Nuevo':
        vals['name'] = self.env['ir.sequence'].next_by_code('gestion.solicitud') or 'Nuevo'
    return super(GestionSolicitud, self).create(vals)

    def action_asignar(self):
        self.write({'state': 'en_proceso'})

    def action_resolver(self):
        self.write({'state': 'resuelto', 'date_resolved': fields.Datetime.now()})

    def action_cerrar(self):
        self.write({'state': 'cerrado'})

    def action_cancelar(self):
        self.write({'state': 'cancelado'})

    def action_reabrir(self):
        self.write({'state': 'nuevo', 'date_resolved': False})