from django.shortcuts import render
import os
from dotenv import load_dotenv
load_dotenv()
from pypdf import PdfReader
import google.generativeai as genai
import json
from django.http import JsonResponse
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))



def home(request):
    texto_cv = ""
    oferta = ""
    analisis = ""

    if request.method == "POST":
        oferta = request.POST.get("oferta", "")

        if request.FILES.get("cv"):
            pdf = request.FILES["cv"]
            reader = PdfReader(pdf)

            for page in reader.pages:
                texto_cv += page.extract_text() or ""

            prompt = f"""
Actúa como un recruiter técnico senior.

CV:
{texto_cv}

OFERTA:
{oferta}

Respondé en español con:
- Compatibilidad (0-100%)
- Fortalezas
- Habilidades faltantes
- Nivel estimado
- Recomendaciones
"""

            model = genai.GenerativeModel("gemini-2.5-flash")
            response = model.generate_content(prompt)
            analisis = response.text

    return render(request, "home.html", {
        "texto": texto_cv,
        "oferta": oferta,
        "analisis": analisis,
    })

import json
from django.http import JsonResponse

def analyze(request):
    if request.method != "POST":
        return JsonResponse({"error": "Solo se permite POST"}, status=405)

    try:
        data = json.loads(request.body)

        descripcion = data.get("descripcion", "")
        cv = data.get("cv", "")

        if not descripcion or not cv:
            return JsonResponse(
                {"error": "Faltan descripcion o cv"},
                status=400
            )

        prompt = f"""
Actúa como un recruiter técnico senior.

CV:
{cv}

OFERTA:
{descripcion}

Respondé en español con:
- Compatibilidad (0-100%)
- Fortalezas
- Habilidades faltantes
- Nivel estimado
- Recomendaciones
"""

        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)

        return JsonResponse({
            "analysis": response.text
        })

    except Exception as e:
        return JsonResponse({
            "error": str(e)
        }, status=500)