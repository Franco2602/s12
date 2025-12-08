# Guía de Despliegue Paso a Paso

Este proyecto ha sido creado para ser lo más simple posible de desplegar. Sigue estos pasos cuidadosamente.

## 1. Preparación Local (Ya realizado por el asistente)
El proyecto ya tiene la estructura necesaria:
- `manage.py`, `requirements.txt`, `Procfile` (no necesario para PA pero buena práctica), `.gitignore`.
- Base de datos configurada (SQLite por defecto).

## 2. Subir a GitHub
Como no tienes Git instalado o configurado en la terminal, necesitarás hacerlo:

1.  **Instalar Git**: Descarga e instala Git desde [git-scm.com](https://git-scm.com/).
2.  **Crear Repositorio**: Ve a [GitHub.com](https://github.com), inicia sesión y crea un nuevo repositorio (ej: `mi-proyecto-django`). No marques "Initialize with README".
3.  **Subir código**:
    - Abre una terminal en la carpeta de este proyecto (`c:\Users\franc\Desktop\BD`).
    - Ejecuta los siguientes comandos uno por uno:
      ```bash
      git init
      git add .
      git commit -m "Primer commit"
      git branch -M main
      git remote add origin https://github.com/TU_USUARIO/mi-proyecto-django.git
      git push -u origin main
      ```
    *(Reemplaza `TU_USUARIO` y `mi-proyecto-django` con tus datos reales)*.

## 3. Despliegue en PythonAnywhere

1.  **Crear cuenta**: Regístrate en [PythonAnywhere.com](https://www.pythonanywhere.com/).
2.  **Consola Bash**: En el "Dashboard", ve a "Consoles" y abre una **Bash** console.
3.  **Clonar el proyecto**:
    ```bash
    git clone https://github.com/TU_USUARIO/mi-proyecto-django.git
    ```
4.  **Crear entorno virtual**:
    ```bash
    cd mi-proyecto-django
    mkvirtualenv --python=/usr/bin/python3.10 mi-entorno
    pip install -r requirements.txt
    ```
5.  **Configurar Web App**:
    - Ve a la pestaña **Web** (arriba a la derecha).
    - Haz clic en **Add a new web app**.
    - Elige **Manual configuration** (no elijas la opción de Django automática, la manual da más control y es fácil si ya tienes el código).
    - Elige **Python 3.10** (o la versión que usaste en el virtualenv).
6.  **Configurar Rutas en la pestaña Web**:
    - **Source code**: Ingresa la ruta completa, ej: `/home/TU_USUARIO/mi-proyecto-django`.
    - **Working directory**: Igual que arriba.
    - **Virtualenv**: Ingresa el nombre de tu entorno, ej: `mi-entorno` (o la ruta completa si te la pide).
7.  **Configurar WSGI**:
    - En la pestaña Web, busca la sección "WSGI configuration file" y haz clic en el enlace.
    - Borra todo el contenido y pega esto (ajustando los nombres):
      ```python
      import os
      import sys

      path = '/home/TU_USUARIO/mi-proyecto-django'
      if path not in sys.path:
          sys.path.append(path)

      os.environ['DJANGO_SETTINGS_MODULE'] = 'gestion_datos.settings'

      from django.core.wsgi import get_wsgi_application
      application = get_wsgi_application()
      ```
    - Guarda el archivo.
8.  **Base de Datos y Archivos Estáticos**:
    - Vuelve a la consola Bash.
    - Ejecuta las migraciones:
      ```bash
      python manage.py migrate
      python manage.py createsuperuser
      python manage.py collectstatic
      ```
    - En la pestaña **Web**, sección **Static files**:
      - URL: `/static/`
      - Directory: `/home/TU_USUARIO/mi-proyecto-django/staticfiles`
9.  **Finalizar**:
    - Ve arriba del todo en la pestaña **Web** y dale al botón verde **Reload**.
    - ¡Listo! Tu sitio debería estar online.

## Notas Importantes
- **Base de Datos**: Este proyecto usa SQLite. En PythonAnywhere funciona bien, pero si reinicias o borras archivos podrías perder datos si no tienes cuidado. Para producción real se recomienda MySQL (incluido en PythonAnywhere), pero añade complejidad.
- **Seguridad**: En `settings.py`, `DEBUG = True` está activado. Para producción deberías ponerlo en `False` y configurar `ALLOWED_HOSTS` con tu dominio de PythonAnywhere (ej: `['tu-usuario.pythonanywhere.com']`).
