# Project Documentation

## Introducción

Este proyecto es un ejemplo de aplicación web basada en **Flask** que integra autenticación, formularios y una pequeña API. Sirve como plantilla mínima para aplicaciones que hacen uso de base de datos y una interfaz ligera con temática "neo‑cyberpunk".

### Tecnologías utilizadas
- **Python** y **Flask** como framework principal.
- **Flask-WTF**, **Flask-Login** y **Flask-SQLAlchemy** para formularios, autenticación y ORM.
- **SQLite** como motor de base de datos por defecto.
- **Bootstrap 5** para la maquetación y estilo básico.
- Hojas de estilo y JavaScript personalizados para la temática neon.

La estructura sigue el patrón habitual de aplicaciones Flask utilizando **blueprints** para separar las rutas de autenticación y las principales.

## Estructura de Archivos

```
Flask_Template/
├── app/                # Paquete principal de la aplicación
│   ├── __init__.py     # Crea la app y registra extensiones/blueprints
│   ├── auth.py         # Rutas de login, logout y registro de usuarios
│   ├── forms.py        # Definición de formularios WTForms
│   ├── main.py         # Rutas principales y API de contactos
│   ├── models.py       # Modelos de base de datos (Usuario y Contacto)
│   ├── static/         # Recursos estáticos (CSS y JS)
│   │   ├── style.css
│   │   └── theme.js
│   └── templates/      # Plantillas Jinja2
│       ├── base.html
│       ├── contact.html
│       ├── index.html
│       ├── login.html
│       └── register.html
├── config.py           # Configuración de Flask y la base de datos
├── requirements.txt    # Dependencias del proyecto
├── run.py              # Punto de entrada para ejecutar el servidor
└── README.md
```

### Relaciones entre componentes

- **`app/__init__.py`** crea la aplicación, inicializa las extensiones y registra los *blueprints* `auth` y `main`.
- **`auth.py`** depende de `forms.py` para los formularios de login/registro y de `models.py` para consultar la tabla `User`.
- **`main.py`** utiliza `ContactForm` y el modelo `Contact` para almacenar mensajes enviados desde `/contact` y expone esos registros vía `/api/contacts`.
- **`models.py`** define las tablas `User` y `Contact` que se usan desde los blueprints.
- Las plantillas HTML extienden `base.html`, que incluye la barra de navegación y el cargado de CSS/JS.
- `theme.js` modifica la variable `--glow-strength` definida en `style.css` mediante el control deslizante incluido en la plantilla base.

### Diagrama resumido

```
[run.py] --> create_app() --+--> [auth blueprint] -> login/logout/register
                            |
                            +--> [main blueprint] -> index/contact/api

[forms.py] <--- used by --- auth.py & main.py
[models.py] <--- imported by --- auth.py, main.py, run.py
```

