from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class HojaTrabajoLine(models.Model):
    _name = 'hoja.trabajo.line'
    _description = 'Línea de Trabajo Diaria'

    hoja_id = fields.Many2one('parte.trabajo', string="Hoja", ondelete='cascade')

    # Información de montaje
    zona_montaje = fields.Char("Zona de montaje")
    notas_montaje = fields.Text("Notas de montaje")

    # Jornada diaria
    fecha = fields.Date("Fecha", required=True, default=fields.Date.context_today)
    entrada_am = fields.Float("Entrada (am)")
    salida_am = fields.Float("Salida (am)")
    entrada_pm = fields.Float("Entrada (pm)")
    salida_pm = fields.Float("Salida(pm)")
    desplazamiento = fields.Float("Desplazamiento (h,m,s)")
    empleado_id = fields.Many2one('hr.employee', string="Empleado")

    # Observaciones
    observaciones = fields.Text("Observaciones")
    imagen_ids = fields.One2many('hoja.trabajo.imagen', 'linea_id', string="Imágenes del día")
    material_ids = fields.Many2many(
        'product.product',
        string="Materiales utilizados en la obra"
    )
    state = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('validado', 'Validado'),
        ('rechazado', 'Rechazado')
    ], string="Estado", default='pendiente', tracking=True)

    @api.constrains('imagen_ids')
    def _check_minimo_tres_imagenes(self):
        for record in self:
            if len(record.imagen_ids) < 3:
                raise ValidationError("Cada línea de trabajo debe tener al menos 3 imágenes.")
    

    def action_validar(self):
        for rec in self:
            rec.state = 'validado'

    def action_rechazar(self):
        for rec in self:
            rec.state = 'rechazado'