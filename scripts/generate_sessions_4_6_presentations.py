from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "05_entregables" / "06_presentaciones"
OUT_DIR.mkdir(parents=True, exist_ok=True)

DARK = RGBColor(28, 38, 52)
BLUE = RGBColor(17, 94, 170)
LIGHT = RGBColor(242, 246, 250)
TEXT = RGBColor(40, 54, 66)
WHITE = RGBColor(255, 255, 255)
ACCENT = RGBColor(76, 136, 216)
GREEN = RGBColor(65, 135, 104)


def add_bg(slide):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = WHITE


def add_header(slide, title):
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.75))
    bar.fill.solid()
    bar.fill.fore_color.rgb = LIGHT
    bar.line.color.rgb = LIGHT
    tb = slide.shapes.add_textbox(Inches(0.55), Inches(0.15), Inches(12.0), Inches(0.45))
    p = tb.text_frame.paragraphs[0]
    p.text = title
    p.alignment = PP_ALIGN.LEFT
    r = p.runs[0]
    r.font.name = "Calibri"
    r.font.size = Pt(18)
    r.font.bold = True
    r.font.color.rgb = DARK


def add_title(slide, title, subtitle=None):
    box = slide.shapes.add_textbox(Inches(0.7), Inches(0.95), Inches(11.8), Inches(0.7))
    p = box.text_frame.paragraphs[0]
    p.text = title
    p.alignment = PP_ALIGN.LEFT
    r = p.runs[0]
    r.font.name = "Calibri"
    r.font.size = Pt(28)
    r.font.bold = True
    r.font.color.rgb = DARK

    if subtitle:
        box2 = slide.shapes.add_textbox(Inches(0.72), Inches(1.6), Inches(11.2), Inches(0.5))
        p2 = box2.text_frame.paragraphs[0]
        p2.text = subtitle
        p2.alignment = PP_ALIGN.LEFT
        r2 = p2.runs[0]
        r2.font.name = "Calibri"
        r2.font.size = Pt(14)
        r2.font.bold = True
        r2.font.color.rgb = BLUE


def add_bullets(slide, items, left=0.9, top=1.9, width=11.5, height=4.5, size=20):
    box = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = box.text_frame
    tf.word_wrap = True
    for idx, item in enumerate(items):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.text = item
        p.level = 0
        p.bullet = True
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(8)
        r = p.runs[0]
        r.font.name = "Calibri"
        r.font.size = Pt(size)
        r.font.color.rgb = TEXT


def add_formula(slide, expression, left=1.1, top=2.0, width=11.0, height=0.7):
    box = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    p = box.text_frame.paragraphs[0]
    p.text = expression
    p.alignment = PP_ALIGN.CENTER
    r = p.runs[0]
    r.font.name = "Calibri"
    r.font.size = Pt(20)
    r.font.color.rgb = BLUE
    r.font.bold = True


def add_two_cols(slide, left_title, right_title, left_items, right_items):
    left_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.8), Inches(5.5), Inches(4.5))
    left_tf = left_box.text_frame
    p = left_tf.paragraphs[0]
    p.text = left_title
    p.alignment = PP_ALIGN.LEFT
    r = p.runs[0]
    r.font.name = "Calibri"
    r.font.size = Pt(20)
    r.font.bold = True
    r.font.color.rgb = BLUE
    for item in left_items:
        p = left_tf.add_paragraph()
        p.text = item
        p.bullet = True
        p.alignment = PP_ALIGN.LEFT
        r = p.runs[0]
        r.font.name = "Calibri"
        r.font.size = Pt(17)
        r.font.color.rgb = TEXT

    right_box = slide.shapes.add_textbox(Inches(6.7), Inches(1.8), Inches(5.5), Inches(4.5))
    right_tf = right_box.text_frame
    p = right_tf.paragraphs[0]
    p.text = right_title
    p.alignment = PP_ALIGN.LEFT
    r = p.runs[0]
    r.font.name = "Calibri"
    r.font.size = Pt(20)
    r.font.bold = True
    r.font.color.rgb = BLUE
    for item in right_items:
        p = right_tf.add_paragraph()
        p.text = item
        p.bullet = True
        p.alignment = PP_ALIGN.LEFT
        r = p.runs[0]
        r.font.name = "Calibri"
        r.font.size = Pt(17)
        r.font.color.rgb = TEXT


def add_cover(prs, title, subtitle, session_no):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_bg(slide)
    band = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.8))
    band.fill.solid(); band.fill.fore_color.rgb = LIGHT; band.line.color.rgb = LIGHT
    box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.2), Inches(10.5), Inches(1.2))
    box.fill.solid(); box.fill.fore_color.rgb = BLUE; box.line.color.rgb = BLUE
    tp = box.text_frame.paragraphs[0]
    tp.text = title
    tp.alignment = PP_ALIGN.LEFT
    r = tp.runs[0]
    r.font.name = "Calibri"
    r.font.size = Pt(26)
    r.font.bold = True
    r.font.color.rgb = WHITE

    sub = slide.shapes.add_textbox(Inches(0.9), Inches(2.8), Inches(9.0), Inches(1.0))
    p = sub.text_frame.paragraphs[0]
    p.text = subtitle
    r = p.runs[0]
    r.font.name = "Calibri"
    r.font.size = Pt(19)
    r.font.color.rgb = TEXT

    badge = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(10.6), Inches(1.8), Inches(1.9), Inches(1.9))
    badge.fill.solid(); badge.fill.fore_color.rgb = ACCENT; badge.line.color.rgb = ACCENT
    tb = slide.shapes.add_textbox(Inches(10.7), Inches(2.2), Inches(1.7), Inches(0.9))
    p2 = tb.text_frame.paragraphs[0]
    p2.text = f"{session_no:02d}"
    p2.alignment = PP_ALIGN.CENTER
    r2 = p2.runs[0]
    r2.font.name = "Calibri"
    r2.font.size = Pt(28)
    r2.font.bold = True
    r2.font.color.rgb = WHITE


def build_session_4():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    add_cover(prs, "Criptografía post-cuántica: ML-KEM y Kyber", "Tema 4 — KEMs, LWE y despliegue práctico", 4)

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 4 — núcleo del problema"); add_title(slide, "¿Qué amenaza a RSA y ECC?")
    add_bullets(slide, [
        "RSA depende de factorizar números grandes.",
        "ECC depende del logaritmo discreto sobre curvas.",
        "Shor los rompe con un ordenador cuántico suficientemente grande.",
        "La amenaza real también incluye el almacenamiento y descifrado futuro de tráfico cifrado.",
    ])

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 4 — definición del objetivo"); add_title(slide, "Qué hace un KEM")
    add_formula(slide, "KeyGen() -> (pk, sk)")
    add_formula(slide, "Encaps(pk) -> (c, K)")
    add_formula(slide, "Decaps(sk, c) -> K")
    add_bullets(slide, [
        "El KEM no cifra el archivo completo; acuerda una clave compartida.",
        "Después se usa una KDF y un cifrado autenticado como AES-GCM.",
        "La clave pública puede transmitirse; la privada debe protegerse.",
    ], top=3.2)

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 4 — intuición matemática"); add_title(slide, "LWE y Module-LWE")
    add_formula(slide, "b = A·s + e   (mod q)")
    add_bullets(slide, [
        "A y b pueden ser públicos; s es el secreto y e es un error pequeño.",
        "La estructura de ruido hace que el problema sea difícil de resolver sin la clave correcta.",
        "ML-KEM usa Module-LWE con polinomios y un anillo cociente.",
    ], top=2.7)

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 4 — ejemplo guiado"); add_title(slide, "Ejemplo simple de LWE")
    add_formula(slide, "q = 17,   A = [[4, 7], [3, 5]],   s = [2, 6]^T,   e = [1, -1]^T")
    add_formula(slide, "b = A·s + e = [51,35]^T ≡ [0,1]^T (mod 17)")
    add_bullets(slide, [
        "La idea es que el atacante observa A y b, pero no conoce s.",
        "El ruido hace que el problema no sea un sistema lineal exacto.",
        "ML-KEM escala este concepto a millones de dimensiones y parámetros bien diseñados.",
    ], top=3.6, height=2.3)

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 4 — comparación rápida"); add_title(slide, "Familias post-cuánticas")
    add_two_cols(slide, "Retículos", "Códigos y hashes", [
        "ML-KEM / Kyber",
        "ML-DSA / Dilithium",
        "NTRU",
    ], [
        "HQC",
        "Classic McEliece",
        "SLH-DSA / SPHINCS+",
    ])

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 4 — flujo de uso"); add_title(slide, "Aplicación real")
    add_formula(slide, "ML-KEM -> secreto compartido -> HKDF -> clave simétrica -> AES-GCM")
    add_bullets(slide, [
        "El cliente encapsula con la clave pública del servidor.",
        "Ambos obtienen el mismo secreto compartido.",
        "A partir de ahí, la capa simétrica cifra los datos reales.",
        "La clave privada del KEM debe permanecer protegida y rotarse correctamente.",
    ], top=3.1)

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 4 — conclusión"); add_title(slide, "Resumen")
    add_bullets(slide, [
        "La amenaza cuántica impacta especialmente a RSA, ECC y DH.",
        "ML-KEM no es un cifrado completo: es un KEM para acordar claves.",
        "LWE es la base matemática que hace posible algoritmos resistentes a nivel cuántico.",
        "En un proyecto real, se combina con KDF, AEAD y gestión segura de claves.",
    ])

    return prs


def build_session_5():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    add_cover(prs, "Métodos post-cuánticos (II): NTRU", "Tema 5 — polinomios, convolución circular y cifrado basado en retículos", 5)

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 5 — idea central"); add_title(slide, "Qué es NTRU")
    add_bullets(slide, [
        "NTRU trabaja con polinomios de coeficientes pequeños.",
        "La clave pública mezcla dos polinomios secretos usando aritmética modular.",
        "El receptor usa su clave privada para recuperar el mensaje original.",
        "Es una construcción clásica basada en retículos y anillos de polinomios.",
    ])

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 5 — anillo"); add_title(slide, "Convolución circular")
    add_formula(slide, "R = Z[x]/(x^N - 1)")
    add_formula(slide, "x^N ≡ 1, x^(N+1) ≡ x, x^(N+2) ≡ x^2")
    add_bullets(slide, [
        "El producto de dos polinomios se reduce módulo x^N - 1.",
        "Eso produce una convolución circular en lugar de una multiplicación lineal normal.",
        "Es crucial para entender por qué la clave pública y el ciphertext se comportan como mezclas de polinomios.",
    ], top=3.3)

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 5 — generación de claves"); add_title(slide, "Clave pública y privada")
    add_formula(slide, "h ≡ p · f_q^{-1} * g   (mod q)")
    add_bullets(slide, [
        "Se eligen polinomios pequeños f y g.",
        "Se exige que f tenga inversa en los módulos p y q.",
        "La clave pública es h; la privada incluye la información necesaria para recuperar el mensaje.",
    ], top=2.9)

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 5 — cifrado y descifrado"); add_title(slide, "Flujo del algoritmo")
    add_formula(slide, "c ≡ r * h + m   (mod q)")
    add_formula(slide, "a ≡ f * c   (mod q)")
    add_formula(slide, "m ≡ f_p^{-1} * center_q(a)   (mod p)")
    add_bullets(slide, [
        "r es un polinomio aleatorio pequeño usado para ocultar el mensaje.",
        "f y la reducción modular permiten recuperar el mensaje original.",
        "El centrado de coeficientes es un paso crítico del descifrado.",
    ], top=4.0)

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 5 — ejemplo didáctico"); add_title(slide, "Mini ejemplo con coeficientes pequeños")
    add_formula(slide, "N = 4,   p = 3,   q = 17")
    add_formula(slide, "f = [1, 3, 0, 0],   g = [0, 1, -1, 0],   h = [9,10,1,14]")
    add_bullets(slide, [
        "Se usa un ejemplo pequeño para ilustrar la estructura, no para seguridad real.",
        "El ciphertext se genera añadiendo el mensaje al producto r * h.",
        "El receptor recupera el mensaje con el producto con f y la reducción módulo p.",
    ], top=3.2)

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 5 — Python"); add_title(slide, "Demostración rápida")
    add_bullets(slide, [
        "Se puede implementar NTRU con una convolución circular en pequeños ejemplos.",
        "El objetivo didáctico es comprobar que el circuito de cifrado/descifrado funciona.",
        "En producción no se usa este ejemplo: se requieren parámetros seguros y validación de implementación.",
    ], top=2.1)

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 5 — cierre"); add_title(slide, "Resumen")
    add_bullets(slide, [
        "NTRU es un KEM muy importante didácticamente y en historia de la PQC.",
        "Su seguridad depende de propiedades de polinomios y retículos.",
        "ML-KEM es el estándar principal del NIST; NTRU permanece importante por aprendizaje y compatibilidad experimental.",
        "El patrón general sigue siendo el mismo: clave pública, encapsulación, secreto compartido y cifrado simétrico.",
    ])

    return prs


def build_session_6():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    add_cover(prs, "Métodos post-cuánticos (III): ML-DSA y SLH-DSA", "Tema 6 — firmas digitales y estado actual de la estandarización", 6)

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 6 — diferencia clave"); add_title(slide, "Firma, KEM y cifrado no son lo mismo")
    add_two_cols(slide, "KEM", "Firma", [
        "Establece una clave compartida.",
        "Usa encapsulación y desencapsulación.",
        "Se usa para secretos de sesión.",
    ], [
        "Prueba origen e integridad.",
        "Usa firmar y verificar.",
        "Resultado: validación por clave pública.",
    ])

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 6 — ML-DSA"); add_title(slide, "Firma basada en retículos")
    add_formula(slide, "t = A·s_1 + s_2   (mod q)")
    add_formula(slide, "w = A·y   (mod q)")
    add_formula(slide, "c = H(mu || highBits(w))")
    add_formula(slide, "z = y + c·s_1")
    add_bullets(slide, [
        "ML-DSA deriva de CRYSTALS-Dilithium, una firma post-cuántica basada en retículos.",
        "La transformación Fiat-Shamir convierte un reto interactivo en una firma no interactiva.",
        "La verificación comprueba si el reto reconstruido coincide con el hash del mensaje y el compromiso.",
    ], top=4.2)

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 6 — ML-DSA"); add_title(slide, "Ejemplo didáctico")
    add_formula(slide, "A = [[4,7],[3,5]], s = [2,1]^T, y = [1,2]^T")
    add_formula(slide, "t = A·s = [15,11]^T,  w = A·y = [1,13]^T")
    add_formula(slide, "c = H(m || w) = 2,  z = y + 2·s = [5,4]^T")
    add_bullets(slide, [
        "La idea es mostrar que la firma y la verificación embeben el mismo compromiso.",
        "Si el mensaje cambia, cambia también el reto del hash y la firma deja de ser válida.",
        "En la implementación real aparecen polinomios, límites y rechazo de muestras para mantener la seguridad.",
    ], top=3.9)

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 6 — SLH-DSA"); add_title(slide, "Firma basada en funciones hash")
    add_formula(slide, "leaf_i = H(pk_i)")
    add_formula(slide, "node = H(left || right)")
    add_formula(slide, "root = autenticación final del árbol")
    add_bullets(slide, [
        "SLH-DSA se apoya en funciones hash y árboles de Merkle.",
        "La clave pública está asociada a la raíz del árbol y no a un retículo.",
        "Es una alternativa matemática distinta a ML-DSA con una base completamente diferente.",
    ], top=4.2)

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 6 — estado actual"); add_title(slide, "Estandarización NIST")
    add_two_cols(slide, "Finalizados", "En desarrollo / diversidad", [
        "ML-KEM (FIPS 203)",
        "ML-DSA (FIPS 204)",
        "SLH-DSA (FIPS 205)",
    ], [
        "HQC-KEM",
        "FN-DSA / Falcon",
        "Diversidad matemática y evaluación continua",
    ])

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 6 — migración"); add_title(slide, "Plan práctico")
    add_bullets(slide, [
        "Inventario: algoritmos, certificados, claves y vida útil de los datos.",
        "Prueba de ML-KEM en un protocolo híbrido para un intercambio clave robusto.",
        "Migración de firmas a ML-DSA o SLH-DSA según tamaño, latencia y soporte disponible.",
        "Añadir versiones de algoritmo, rotación y vigilancia funcional antes de despliegue total.",
    ])

    slide = prs.slides.add_slide(prs.slide_layouts[6]); add_bg(slide); add_header(slide, "Tema 6 — cierre"); add_title(slide, "Resumen")
    add_bullets(slide, [
        "ML-DSA y SLH-DSA resuelven el problema de firma post-cuántica con bases matemáticas distintas.",
        "ML-KEM, ML-DSA y SLH-DSA ya son estándares finales del NIST.",
        "La migración real exige criptoagilidad, pruebas y un plan de transición bien documentado.",
        "La combinación con AES-GCM y KDF es esencial para un diseño seguro.",
    ])

    return prs


def save_pptx(presentation, filename):
    path = OUT_DIR / filename
    presentation.save(path)
    print(f"Generated: {path}")


def main():
    save_pptx(build_session_4(), "sesion_4_ml_kem_kyber.pptx")
    save_pptx(build_session_5(), "sesion_5_ntru.pptx")
    save_pptx(build_session_6(), "sesion_6_ml_dsa_dilithium.pptx")


if __name__ == "__main__":
    main()
