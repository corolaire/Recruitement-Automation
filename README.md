# Recruitement-Automation
# Recruitment Automation API

API desarrollada en Django que utiliza **Google Gemini (Generative AI)** para automatizar el análisis de candidatos: recibe la descripción de un puesto y el CV de un candidato, y devuelve un **puntaje de compatibilidad** entre ambos, agilizando el proceso de preselección de talento.

## 🎯 Objetivo

Reducir el tiempo de screening manual de CVs, permitiendo evaluar automáticamente qué tan compatible es un candidato con una búsqueda laboral específica mediante inteligencia artificial generativa.

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **Django** — framework backend
- **Google Generative AI (Gemini API)** — motor de análisis e IA
- **python-dotenv** — manejo seguro de variables de entorno
- **SQLite** — base de datos
- **Postman** — testing de endpoints

## 📋 Requisitos previos

- Python 3.10 o superior
- Una API Key de Gemini ([Google AI Studio](https://aistudio.google.com/apikey))

## 🚀 Instalación y puesta en marcha

1. **Cloná el repositorio**
   ```bash
   git clone https://github.com/corolaire/Recruitement-Automation.git
   cd Recruitement-Automation
   ```

2. **Creá y activá un entorno virtual**
   ```bash
   python -m venv venv
   # Windows (PowerShell)
   venv\Scripts\Activate.ps1
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Instalá las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurá las variables de entorno**

   Creá un archivo `.env` en la raíz del proyecto con el siguiente contenido:
   ```
   GEMINI_API_KEY=tu_clave_de_gemini_aca
   ```

5. **Aplicá las migraciones**
   ```bash
   python manage.py migrate
   ```

6. **Levantá el servidor**
   ```bash
   python manage.py runserver
   ```

   La API va a estar disponible en `http://127.0.0.1:8000/`

## 📡 Uso de la API

### `POST /analyze`

Recibe la descripción de un puesto y el CV de un candidato, y devuelve el puntaje de compatibilidad entre ambos.

**Request:**
```json
{
  "descripcion": "Se busca AI Developer con experiencia en Python y APIs",
  "cv": "Micaela es developer en inteligencia artificial, experiencia en Python..."
}
```

**Response:**
```json
{
  "puntaje": 85
}
```

## 📁 Estructura del proyecto

```
recruitement-automation/
├── config/              # Configuración del proyecto Django (settings, urls)
├── recruitment/         # App principal: lógica de análisis con Gemini
├── manage.py
├── requirements.txt
└── .env                 # Variables de entorno (no versionado)
```

## 🔒 Seguridad

Las credenciales sensibles (API Keys) se gestionan mediante variables de entorno y **nunca** se suben al repositorio (ver `.gitignore`).

## ✍️ Autora

**Micaela Corolaire**
Desarrolladora de Automatización de Procesos e IA
[@micaela-corolaire](https://github.com/corolaire)
