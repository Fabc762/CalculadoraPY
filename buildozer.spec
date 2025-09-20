[app]
# Nombre de la aplicación
title = MiCalculadora

# Identificador único del paquete
package.name = calculadora
package.domain = org.kivy

# Versión de la aplicación
version = 1.1

# Carpeta de tu código fuente y extensiones incluidas
source.dir = .
source.include_exts = py,png,kv,json,spec

# Requerimientos de Python y librerías de Kivy
requirements = python3,kivy

# Permisos que requiere la app (agrega más si los necesitas)
android.permissions = INTERNET

# Ícono personalizado (descomenta si tienes icono.png en la raíz)
# android.icon_filename = %(source.dir)s/icono.png

# Orientación de la pantalla, puede ser: portrait, landscape, sensor
orientation = portrait

# Nombre del archivo principal de tu app
main.py = main.py

# (Opcional) Para evitar errores con el log
log_level = 2

# (Opcional) Para que funcione bien en Android moderno
android.api = 33
android.minapi = 21

# (Opcional) Si usas .kv, asegúrate de incluirlo automáticamente
presplash.filename = %(source.dir)s/presplash.png
