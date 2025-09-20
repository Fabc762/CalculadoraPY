[app]
# --- Datos básicos de la app ---
title = Calculadora
package.name = calculadora
package.domain = org.tuusuario   # cambia "tuusuario" por algo único
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# --- Icono y versión ---
icon.filename = icono.png
version = 0.1

# --- Dependencias de Python ---
requirements = python3,kivy

# --- Orientación de la pantalla ---
orientation = portrait

# --- Permisos opcionales (si necesitas) ---
# android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
