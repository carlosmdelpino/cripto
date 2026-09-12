from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from textwrap import wrap

ROOT = Path(r"C:\Users\cmari\Desktop\IEP\CriptografíaPostcuantica")


def add_pdf(path: Path, title: str, paragraphs: list[str]):
    c = canvas.Canvas(str(path), pagesize=letter)
    c.setTitle(title)
    c.setAuthor("Criptografía Postcuántica")
    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, 750, title)
    y = 720
    c.setFont("Helvetica", 11)
    for paragraph in paragraphs:
        lines = wrap(paragraph, width=92)
        if not lines:
            continue
        for line in lines:
            if y < 72:
                c.showPage()
                c.setFont("Helvetica", 11)
                y = 750
            c.drawString(72, y, line)
            y -= 16
        y -= 10
    c.save()


practice_text = [
    "Práctica de la Unidad 1: Fundamentos de la criptografía",
    "Objetivo: comprender los principios básicos de la criptografía y aplicarlos con Python.",
    "Tareas principales:",
    "1. Identificar los objetivos de seguridad: confidencialidad, integridad, autenticación y no repudio.",
    "2. Diferenciar entre criptografía simétrica, asimétrica e híbrida.",
    "3. Resolver ejercicios de aritmética modular, por ejemplo 23 mod 7, 29 mod 10 y 43 mod 5.",
    "4. Calcular un hash SHA-256 del texto mensaje_secreto y analizar el impacto de cualquier cambio.",
    "5. Redactar una reflexión final sobre la seguridad digital en aplicaciones cotidianas.",
    "6. Entregar el notebook con los apartados completos y una conclusión con tres ideas principales.",
    "Criterios de evaluación: claridad conceptual, rigor matemático, uso correcto de Python y calidad de la argumentación.",
    "Fecha de referencia: XX-YY-ZZZZ."
]

quiz_text = [
    "Test de conocimientos de la Unidad 1",
    "Instrucciones: cada pregunta tiene cuatro opciones y solo una es correcta.",
    "Preguntas clave:",
    "1. ¿Cuál es el objetivo principal de la confidencialidad?",
    "2. ¿Qué propiedad garantiza la integridad de un archivo?",
    "3. ¿Qué tipo de criptografía usa la misma clave para cifrar y descifrar?",
    "4. ¿Qué diferencia principal hay entre una clave pública y una privada?",
    "5. ¿Qué función transforma la entrada en una salida de longitud fija?",
    "6. ¿Qué permite la firma digital?",
    "7. ¿Qué significa 23 ≡ 2 (mod 7)?",
    "8. ¿Qué es un número primo?",
    "9. ¿Qué combina la criptografía híbrida?",
    "10. ¿Cómo se comprueba la integridad de un archivo?",
    "Respuestas correctas: 1-B, 2-B, 3-A, 4-B, 5-B, 6-B, 7-B, 8-B, 9-C, 10-B.",
    "La seguridad de la información depende de confidencialidad, integridad, autenticación y no repudio."
]

add_pdf(ROOT / "05_entregables" / "03_practicas" / "unidad_1" / "01_resumen_tareas_unidad_1.pdf", "Resumen de tareas - Unidad 1", practice_text)
add_pdf(ROOT / "05_entregables" / "04_tests" / "unidad_1" / "01_test_unidad_1.pdf", "Test de la Unidad 1", quiz_text)
print("PDFs generados correctamente.")
