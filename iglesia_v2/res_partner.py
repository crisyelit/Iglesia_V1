# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# Generated by the Odoo plugin for Dia !
#
from openerp import models,fields,api,exceptions
from datetime import timedelta,date


class res_partner(models.Model):
    """Tabla de Registro Maestro de Miembros de la iglesia"""
    _name = 'res.partner'
    _inherit='res.partner'

    #~ _columns = {
    zona_territorial_id = fields.Many2one('hsn.mins.zonas','Nombre de la zona', help='Zona en la que pertenece la celula')
    ofrenda = fields.Char('Ofrenda',size=6, help='Ofrenda recogida en la Celula')
    diezmo = fields.Char('Diezmo',size=50, help='Diezmo dado por el miembro')
    fecha_nacimiento = fields.Date('Fecha Nacimiento', size=10, help='Fecha de Nacimiento del miembro')
    numero_id = fields.Char('No. Identificación', size=20)
    direccion_oficina = fields.Char('Dirección Oficina', size=80, help='Direccion de donde trabaja')
    telefono_oficina = fields.Char('Teléfono de Oficina', size=20, help='Telefono de su trabajo')
    fax_oficina = fields.Char('Fax de Oficina', size=20, help='Fax de su trabajo'),
    partner_conyuge_id = fields.Many2one('res.partner', 'Conyuge', select=True, help='Nombre y Apellido de su Pareja')
    partner_hijo_id = fields.Many2one('res.partner', 'Hijo', select=True, help='Nombre y Apellido de su hijo')
    profesiones_id = fields.Many2one('res.partner', 'Profesión', help='Profesion en que se graduo')
    estado_civil = fields.Selection([('Soltero','Soltero'),('Casado','Casado'),('Divorciado','Divorciado'),('Unido','Unido'),('Otro','Otro')], 'Estado Civil', help='Estado civil que posee')

    nuevo_creyente = fields.Selection([('Si','Si'),('No','No')], 'Nuevo creyente ? ',  help='¿Es nuevo creyente?')
    fecha_conversion = fields.Date('Fecha de Conversion', size=10, help='¿Fecha en la que acepto a cristo?')
    lugar_conversion = fields.Char('Lugar de Conversion', size=80, help='¿Lugar en la que acepto a cristo?')
    donde_congregaba = fields.Char('Donde se congraba',   size=80, help='¿A que iglesia se congrega?')
    tiempo_asistir = fields.Float('Tiempo de Asistir (Años/meses)',digits=(4,2), help='¿Desde cuando esta congregandose?')
    todos_convertidos = fields.Selection([('Si','Si'),('No','No')], 'Todos converticos ? ', help='¿Estan convertidos toda su familia?' )
    bautismo = fields.Selection([('Si','Si'),('No','No')], 'Estas bautizado ? ', help='¿Esta bautizado?' )
    fecha_bautismo_agua = fields.Date('Fecha de bautismo en agua', size=10, help='¿Cuando fue bautizado con agua?' )
    fecha_bautismo_es = fields.Date('Fecha de bautismo en Espiritu Santo', size=10, help='¿Cuando fue bautizado en Espiritu Santo?')
    carta_pastor = fields.Selection([('Si','Si'),('No','No')], 'Se tralado con carta', help='¿Fue recibido con carta de pastor?')
    asiste_discipulado = fields.Selection([('Si','Si'),('No','No')], 'Asiste a un discipulado', help='¿Esta siendo discipulado?')
    se_indentifica = fields.Selection([('Si','Si'),('No','No')], 'Se identifica con la doctrina de la Iglesia ', help='¿Esta deacuerdo con las doctrinas de la iglesia?')
    doctrina_basica = fields.Selection([('Si','Si'),('No','No')], 'Recibió doctrina basica', help='¿Recibio las doctrinas base de la iglesia?')
    partner_discipulador_id = fields.Many2one('res.partner', 'Discipulador', select=True, help='¿Quien es su discipulador?')
    partner_recomienda_id = fields.Many2one('res.partner', 'Recomendado por', select=True, help='¿Fue recomendado o invitado por?')
    observaciones = fields.Text('Observaciones', help='Observaciones acotado por el miembro')
            #~ }
