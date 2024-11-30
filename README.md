## Guía para Implementar Aplicaciones Dash en Render
Este proyecto proporciona una guía para implementar aplicaciones web dinámicas **Dash** en la plataforma como servicio (PaaS) **Render**, utilizando herramientas como **dash-tools**. La guía incluye los conceptos esenciales para la preparación del entorno, la configuración del proyecto y el despliegue de la aplicación.

## Tabla de Contenidos
- [Objetivo](#objetivo)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Prerrequisitos](#prerrequisitos)
- [Metodología](#metodología)
  - [Instalación de Git](#instalación-de-git)
  - [Desarrollar la Aplicación Web con Dash](#desarrollar-la-aplicación-web-con-dash)
  - [Validar Git](#validar-git)
  - [Configurar la Estructura del Proyecto con Dash Tools](#configurar-la-estructura-del-proyecto-con-dash-tools)
  - [Despliegue en Render](#despliegue-en-render)
- [Software](#software)
- [Instalación](#instalación)

## Objetivo
El objetivo de este proyecto es desarrollar una aplicación web interactiva utilizando **Dash**. Se utilizarán herramientas de control de versiones como **Git** en Visual Studio Code para gestionar el código de manera eficiente. El proyecto es cargado en **GitHub** para su almacenamiento remoto. Finalmente, la aplicación será desplegada en Render, asegurando su ejecución de manera segura y accesible en la web. 

## Estructura del proyecto
```bash
project-root/
├── src/                        # Carpeta que contiene el código fuente
    └── app.py                  # Código principal de la aplicación Dash
        └── server = app.server # Exposición del servidor Flask utilizado por Dash
├── render.yaml                 # Archivo de configuración de Render
├── requirements.txt            # Dependencias necesarias para la aplicación
└── README.md                   # Documentación del proyecto
```
## Prerrequisitos
- Una cuenta en **GitHub** y un repositorio para el proyecto. Puedes registrarte gratuitamente en [github.com](https://github.com/).
- Una cuenta en **Render** para desplegar la aplicación web. puedes crearla de manera gratuita en [render.com](https://render.com/) 

## Metodología
## Instalación de Git
Antes de iniciar, lo primero es tener instalado **Git** en nuestra computadora. 
Puedes descargarlo desde la página oficial: [git-scm.com](https://git-scm.com/). Una vez descargado, procede a instalarlo siguiendo las instrucciones proporcionadas en el sitio web.

## Desarrollar la Aplicación Web con Dash
Sigue estas convenciones al desarrollar tu aplicación web interactiva con **Dash**:

1. **Archivo principal (`app.py`)**: Render ejecuta por defecto un archivo llamado `app.py`. Nombrarlo así evita configurar manualmente la ruta de inicio de la aplicación.
2. **Directorio `src`**: Es recomendable colocar `app.py` en un directorio llamado `src` para mantener el proyecto organizado, aunque no es obligatorio.
3. **Instancia `server = app.server`**: Define `server = app.server` en `app.py` para exponer la instancia Flask subyacente, lo cual es necesario para que Render gestione correctamente la aplicación como un servicio web.

## Validar Git
Antes de comenzar, asegúrate de que **Git** está instalado en tu computadora:

**Validar la instalación de Git:** Ejecuta el siguiente comando en tu terminal para comprobar la versión instalada:
```bash
git --version
```

## Configurar la Estructura del Proyecto con Dash Tools
**Dash Tools** es una herramienta que simplifica la preparación del proyecto, asegurando que todos los requisitos para el despliegue en **Render** estén cubiertos. Sigue los pasos para configurar la estructura del proyecto:

1. **Abrir la Interfaz de Dash Tools**  
Ejecuta el siguiente comando en la terminal para acceder a la interfaz gráfica (GUI) de **Dash Tools**:
```bash
dashtools gui
```
2. **Tareas Automatizadas con Dash Tools**  
Dash Tools realiza diversas tareas para asegurar la compatibilidad del proyecto con Render:
    - **Validación del Proyecto**
        - Confirmación de la existencia de `src/app.py`: Verifica que el archivo principal de la aplicación, esté presente y estructurado correctamente.
         - Definición de `app.server`: Garantiza que en archivo principal exista una instancia definida como `server = app.server`.

    - **Generación de Archivos Clave**
        - **`render.yaml`**: Archivo de configuración para desplegar la aplicación en Render.
        - **`requirements.txt`**: Archivo que contiene las dependencias necesarias para la ejecución de la aplicación.

    - **Guardar y Verificar la Estructura del Proyecto**
        Una vez que Dash Tools haya validado y generado los archivos necesarios, verifica que la organización del proyecto sea la siguiente:
        ```bash
        project-root/
        ├── src/                        # Carpeta que contiene el código fuente
            └── app.py                  # Código principal de la aplicación Dash
                └── server = app.server # Exposición del servidor Flask utilizado por Dash
        ├── render.yaml                 # Archivo de configuración de Render
        ├── requirements.txt            # Dependencias necesarias para la aplicación
        └── README.md                   # Documentación del proyecto
        ```
## Despliegue en Render
Antes de desplegar tu proyecto en **Render**, asegúrate de que esté subido a **GitHub**.

**Pasos previos:**
1. **Sube tu proyecto a GitHub**, incluyendo los archivos `app.py`, `render.yaml`, y `requirements.txt`. Para esto, abre una **nueva terminal** (diferente a la que estás utilizando para **Dash Tools**) y usa los comandos básicos de Git para cargar tu proyecto a GitHub:
   - Inicializa el repositorio: `git init`
   - Agrega los archivos: `git add .`
   - Realiza un commit: `git commit -am "Primer commit"`
   - Vincula el repositorio remoto (si no lo has hecho previamente): `git remote add origin <URL-de-tu-repositorio>`
   - Sube los cambios: `git push -u origin main`

2. **Conecta Dash Tools a tu repositorio de GitHub** para iniciar el despliegue haciendo clic en el boton para el despligue.
Dash Tools se encargará del despliegue en **Render** una vez que tu proyecto esté listo.

Para más información, puedes consultar este Video Tutorial [Share your Dash App with Others on the Web - Render](https://www.youtube.com/watch?v=XWJBJoV5yww). en el canal de YouTube **Charming Data** donde el autor muestra de una manera fácil y rápida como implementar tu aplicación con **Dash** en la web, usando Dash Tools de Andrew, un miembro de la comunidad de Plotly.

## Software
**Requisitos**
1. Python 3.x
2. Visual Studio Code
3. Bibliotecas necesarias:
   - `pandas`
   - `plotly`
   - `dash`
   - `dash-tools`

## Instalación
```bash
pip install pandas plotly dash dash-tools
