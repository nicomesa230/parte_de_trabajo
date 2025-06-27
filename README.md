Parte de Trabajo – Módulo Odoo
Este módulo permite generar y gestionar partes de trabajo en Odoo, asociados a obras, clientes y empleados. Incluye campos personalizados para capturar información clave como materiales, medidas, jornadas, observaciones, firmas y más. También genera un PDF con el diseño específico de los partes.

📦 Requisitos
Odoo 16 o superior

Acceso como usuario administrador

Conocimientos básicos de instalación de módulos Odoo

🚀 Instalación
1. Clona el repositorio
cd /ruta/a/tu/odoo/custom/addons/
git clone https://github.com/nicomesa230/parte_de_trabajo.git
2. Reinicia el servidor de Odoo
Si estás utilizando Odoo en modo desarrollo:
./odoo-bin -d tu_base_de_datos -u parte_trabajo
O bien, reinicia el servicio si lo tienes en producción:

sudo service odoo restart
3. Activa el modo desarrollador
Accede a Odoo con un usuario administrador.

Ve a Ajustes > Activar el modo desarrollador (en el menú de usuario, arriba a la derecha).

4. Instala el módulo
Ve a Aplicaciones.

Haz clic en Actualizar lista de aplicaciones (icono con forma de escudo en la parte superior).

Busca Parte de Trabajo.

Haz clic en Instalar.

🛠️ Uso
Ve al nuevo menú Parte de Trabajo.

Crea un nuevo parte completando:

Cliente, Obra, Sistema, Serie

Jornadas y Empleados

Materiales usados

Medidas (ancho, alto, longitud…)

Observaciones y Fotos

Puedes subir firmas del cliente y del operario.

Al guardar, puedes generar un PDF personalizado desde el botón de impresión en la parte superior derecha.

🧾 Reporte PDF
El módulo incluye un reporte PDF con diseño personalizado que replica un parte de trabajo con todos los datos capturados, incluyendo firmas y fotos incrustadas.

📞 Soporte
Para dudas, errores o sugerencias, puedes abrir un issue o contactar directamente al desarrollador:

Autor: Nicolás Mesa
Email: nicomesa230@gmail.com

