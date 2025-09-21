[app]

# (str) Nombre de tu aplicación
title = Mi App Kivy

# (str) Nombre del paquete (en minúsculas, sin espacios)
package.name = miapp

# (str) Nombre del paquete Java (debe ser único, estilo dominio)
package.domain = org.miapp

# (str) Versión
version = 1.0.0

# (str) Ruta al script principal
source.dir = .
source.main = main.py

# (list) Requisitos de la app (añade los módulos que uses)
requirements = python3,kivy

# (bool) Incluir archivos fuente en el APK
include_source = true

# (str) Orientación: portrait, landscape o all
orientation = portrait

# === RUTAS Y VERSIONES ANDROID ===
# (str) Ruta del SDK Android que instalaste en GitHub Actions
android.sdk_path = /home/runner/android-sdk

# (int) API de Android que quieres usar
android.sdk_api = 33

# (str) Versión exacta de Build Tools que ya está instalada
android.build_tools_version = 33.0.2

# (str) Versión mínima de Android
android.minapi = 21

# (bool) Incluir depurador
android.debug = true

# (str) Permisos extra (si necesitas)
#android.permissions = INTERNET

# (str) Icono
#icon.filename = %(source.dir)s/data/icon.png

# (str) Nombre del paquete Java principal
#android.entrypoint = org.kivy.android.PythonActivity

# ====================

[buildozer]

# (str) Nombre del directorio bin para los APK
bin_dir = bin

# (bool) Si se debe limpiar antes de compilar
log_level = 2
