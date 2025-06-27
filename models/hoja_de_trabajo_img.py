from odoo import models, fields

class HojaTrabajoImagen(models.Model):
    _name = 'hoja.trabajo.imagen'
    _description = 'Imagen asociada a la línea de trabajo'

    linea_id = fields.Many2one('hoja.trabajo.line', string="Línea de trabajo", ondelete="cascade", required=True)
    image = fields.Image("Imagen", required=True)
    descripcion = fields.Char("Descripción")
