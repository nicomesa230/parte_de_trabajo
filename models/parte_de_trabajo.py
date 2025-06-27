from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HojaTrabajo(models.Model):
    _name = "parte.trabajo"
    _description = "Hojas de trabajo a rellenar cada día"

    cliente_id = fields.Many2one('res.partner', string="Cliente", required=True)
    obra_id = fields.Many2one('gestion.obra', string="Obra", required=True)
    obra_nombre = fields.Char(compute="_compute_obra_nombre", store=False)
    trabajo_realizar = fields.Char(string="Trabajo a realizar")
    n_serie = fields.Integer(string="Nº serie")
    altura = fields.Float(string="Altura (m)")
    longitud = fields.Float(string="Longitud (m)")
    oferta = fields.Float(string="Oferta")
    sistema = fields.Char(string="Sistema")
    npcl = fields.Char(string="N.P.C.L.")
    firma_montador = fields.Binary(string="Firma Montador")
    firma_cliente = fields.Binary(string="Firma Cliente")
    line_ids = fields.One2many('hoja.trabajo.line', 'hoja_id', string="Días de trabajo")
    firma_montador_url = fields.Char(compute="_compute_firma_urls", store=False)
    firma_cliente_url = fields.Char(compute="_compute_firma_urls", store=False)
    state = fields.Selection([
        ('borrador', 'Borrador'),
        ('en_progreso', 'En progreso'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado')
    ], string="Estado", default='borrador', tracking=True)

    @api.constrains('line_ids')
    def _check_lineas_con_imagenes(self):
        for parte in self:
            for linea in parte.line_ids:
                if len(linea.imagen_ids) < 3:
                    raise ValidationError(
                        f"La línea de trabajo del {linea.fecha} para el empleado {linea.empleado_id.name or 'sin asignar'} debe tener al menos 3 imágenes."
                    )

    @api.depends('firma_montador', 'firma_cliente')
    def _compute_firma_urls(self):
        for record in self:
            firma_montador = False
            firma_cliente = False

            if record.firma_montador:
                try:
                    firma_montador = f"data:image/png;base64,{record.firma_montador.decode('utf-8').strip()}"
                except Exception:
                    firma_montador = False

            if record.firma_cliente:
                try:
                    firma_cliente = f"data:image/png;base64,{record.firma_cliente.decode('utf-8').strip()}"
                except Exception:
                    firma_cliente = False

            record.firma_montador_url = firma_montador
            record.firma_cliente_url = firma_cliente

    @api.depends('obra_id.nombre')
    def _compute_obra_nombre(self):
        for record in self:
            record.obra_nombre = record.obra_id.nombre or "Sin nombre"

    def action_en_progreso(self):
        for rec in self:
            rec.state = 'en_progreso'

    def action_finalizar(self):
        for rec in self:
            rec.state = 'finalizado'

    def action_cancelar(self):
        for rec in self:
            rec.state = 'cancelado'
    
    def report_pt_pdf(self):
        """Generar el reporte de la hoja de trabajo"""
        return self.env.ref('parte_de_trabajo.action_report_parte_trabajo').report_action(self)