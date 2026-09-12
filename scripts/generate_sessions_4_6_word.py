from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt


OUT_DIR = Path("05_entregables/02_word")


def add_formula(doc: Document, expression: str) -> None:
    """Insert a centered native Word equation containing linear math notation."""
    paragraph = doc.add_paragraph()
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    math_paragraph = OxmlElement("m:oMathPara")
    math_properties = OxmlElement("m:oMathParaPr")
    justification = OxmlElement("m:jc")
    justification.set(qn("m:val"), "center")
    math_properties.append(justification)
    math_paragraph.append(math_properties)

    math = OxmlElement("m:oMath")
    math_run = OxmlElement("m:r")
    math_text = OxmlElement("m:t")
    math_text.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    math_text.text = expression
    math_run.append(math_text)
    math.append(math_run)
    math_paragraph.append(math)
    paragraph._p.append(math_paragraph)


def add_code(doc: Document, code: str) -> None:
    paragraph = doc.add_paragraph()
    paragraph.paragraph_format.space_after = Pt(8)
    run = paragraph.add_run(code.strip())
    run.font.name = "Consolas"
    run.font.size = Pt(8.5)


def add_table(doc: Document, headers: list[str], rows: list[list[str]]) -> None:
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = "Table Grid"
    for cell, header in zip(table.rows[0].cells, headers):
        cell.text = header
    for row in rows:
        cells = table.add_row().cells
        for cell, value in zip(cells, row):
            cell.text = value


def section(doc: Document, title: str) -> None:
    doc.add_heading(title, level=2)


def paragraphs(doc: Document, *items: str) -> None:
    for item in items:
        doc.add_paragraph(item)


def bullets(doc: Document, *items: str) -> None:
    for item in items:
        doc.add_paragraph(item, style="List Bullet")


def numbered(doc: Document, *items: str) -> None:
    for item in items:
        doc.add_paragraph(item, style="List Number")


def exercise(doc: Document, number: int, title: str, statement: str) -> None:
    paragraph = doc.add_paragraph()
    run = paragraph.add_run(f"Ejercicio {number}. {title}. ")
    run.bold = True
    paragraph.add_run(statement)


def solution(doc: Document, text: str) -> None:
    paragraph = doc.add_paragraph()
    run = paragraph.add_run("Solución comentada. ")
    run.bold = True
    paragraph.add_run(text)


def configure_document(doc: Document, title: str) -> None:
    doc.core_properties.title = title
    doc.core_properties.subject = "Criptografía post-cuántica"
    doc.core_properties.author = "Material docente de criptografía"

    for section_ in doc.sections:
        section_.top_margin = Inches(0.7)
        section_.bottom_margin = Inches(0.7)
        section_.left_margin = Inches(0.8)
        section_.right_margin = Inches(0.8)

    normal = doc.styles["Normal"]
    normal.font.name = "Aptos"
    normal.font.size = Pt(10.5)
    normal.paragraph_format.space_after = Pt(5)
    normal.paragraph_format.line_spacing = 1.08


def start_document(title: str, subtitle: str) -> Document:
    doc = Document()
    configure_document(doc, title)
    doc.add_heading(title, level=0)
    doc.add_paragraph(subtitle)
    doc.add_paragraph("Duración orientativa: 30 minutos")
    doc.add_paragraph(
        "Enfoque: una base matemática bien explicada, un ejemplo resuelto, "
        "ejercicios breves y una conexión directa con un proyecto real."
    )
    return doc


def build_session_4() -> Document:
    title = (
        "Sesión 4. Criptografía post-cuántica: introducción. "
        "Métodos de criptografía post-cuántica (II)"
    )
    doc = start_document(
        title,
        "Método principal: ML-KEM, derivado de CRYSTALS-Kyber y estandarizado en NIST FIPS 203.",
    )

    section(doc, "1. Objetivos y guion de la sesión")
    bullets(
        doc,
        "Entender qué cambia cuando el adversario dispone de un ordenador cuántico grande.",
        "Distinguir un KEM de un cifrado de datos y de una firma digital.",
        "Relacionar el problema LWE con las operaciones de ML-KEM.",
        "Resolver una encapsulación didáctica y usar una implementación existente desde Python.",
    )
    add_table(
        doc,
        ["Minutos", "Actividad"],
        [
            ["0-6", "Amenaza cuántica y objetivo de la criptografía post-cuántica."],
            ["6-10", "Mapa de familias y diferencia entre KEM y firma."],
            ["10-18", "Base matemática: LWE y Module-LWE."],
            ["18-25", "Ejemplo guiado de encapsulación."],
            ["25-30", "Ejercicios, Python y uso en proyecto."],
        ],
    )

    section(doc, "2. Qué significa post-cuántica")
    paragraphs(
        doc,
        "La criptografía post-cuántica usa ordenadores clásicos y redes normales. Lo que cambia es "
        "el problema matemático en el que se apoya la seguridad: se eligen problemas para los que "
        "no se conoce un ataque eficiente ni clásico ni cuántico.",
        "El algoritmo de Shor amenaza RSA, Diffie-Hellman y la criptografía de curva elíptica porque "
        "resuelve eficientemente la factorización y el logaritmo discreto en un ordenador cuántico "
        "suficientemente grande. Grover afecta a la búsqueda exhaustiva, pero su ventaja es cuadrática, "
        "por lo que las primitivas simétricas se compensan usando claves suficientemente largas.",
    )
    add_formula(doc, "coste clásico ≈ 2ⁿ   →   coste con Grover ≈ 2ⁿᐟ²")
    paragraphs(
        doc,
        "La urgencia no depende solo de cuándo exista ese ordenador. Un atacante puede almacenar hoy "
        "tráfico cifrado y tratar de descifrarlo años después. Este escenario se conoce como "
        "«recoger ahora, descifrar después» y afecta sobre todo a datos con una vida confidencial larga.",
    )

    section(doc, "3. Familias de métodos post-cuánticos")
    add_table(
        doc,
        ["Familia", "Idea matemática", "Ejemplos", "Uso principal"],
        [
            ["Retículos", "Vectores cortos y ecuaciones con ruido", "ML-KEM, ML-DSA, NTRU", "KEM y firmas"],
            ["Códigos", "Decodificar palabras con errores", "HQC, Classic McEliece", "KEM"],
            ["Funciones hash", "Árboles y firmas de un solo uso", "SLH-DSA", "Firmas"],
            ["Otras líneas", "Isogenias y sistemas multivariantes", "SQIsign, MAYO, UOV", "Investigación"],
        ],
    )
    paragraphs(
        doc,
        "En esta sesión se estudia una sola construcción con detalle: ML-KEM. La tabla sirve para "
        "ubicarla y para mostrar que «post-cuántico» no significa una única técnica matemática.",
    )

    section(doc, "4. Antes del algoritmo: qué hace un KEM")
    paragraphs(
        doc,
        "Un mecanismo de encapsulación de claves no cifra un archivo completo. Su trabajo es producir "
        "el mismo secreto compartido en dos extremos. Ese secreto se entrega después a una función de "
        "derivación y a un cifrado autenticado como AES-GCM o ChaCha20-Poly1305.",
    )
    add_formula(doc, "(ek, dk) ← KeyGen()")
    add_formula(doc, "(K, c) ← Encaps(ek)")
    add_formula(doc, "K′ ← Decaps(dk, c)   y, si c es válido,   K′ = K")
    bullets(
        doc,
        "ek es la clave pública de encapsulación y puede distribuirse.",
        "dk es la clave privada de desencapsulación y debe protegerse.",
        "c es el texto de encapsulación que viaja por la red.",
        "K no viaja por la red: ambos extremos lo obtienen mediante operaciones distintas.",
    )

    section(doc, "5. Base matemática: de un sistema lineal a LWE")
    paragraphs(
        doc,
        "En un sistema lineal exacto, conocer la matriz y el resultado permite intentar recuperar el "
        "vector desconocido mediante álgebra lineal. Learning With Errors añade un vector de error "
        "pequeño. El receptor legítimo aprovecha la estructura y los márgenes de redondeo; el atacante "
        "ve muchas ecuaciones que no encajan exactamente.",
    )
    add_formula(doc, "b = A·s + e   (mod q)")
    bullets(
        doc,
        "A es una matriz pública con coeficientes módulo q.",
        "s es un vector secreto pequeño.",
        "e es un vector de error pequeño y aleatorio.",
        "b es público, pero el ruido impide tratarlo como un sistema lineal exacto.",
    )
    paragraphs(
        doc,
        "ML-KEM utiliza Module-LWE. Sus componentes son polinomios y la multiplicación se realiza en un "
        "anillo cociente. Esta estructura acelera el cálculo y reduce el tamaño de las claves sin "
        "convertir el problema en el sistema lineal sencillo del ejemplo de aula.",
    )
    add_formula(doc, "R_q = ℤ_q[x] / (x²⁵⁶ + 1)")
    add_formula(doc, "b⃗ = A·s⃗ + e⃗   en vectores de polinomios de R_q")

    section(doc, "6. Ejemplo guiado: una muestra LWE")
    paragraphs(doc, "Tomamos los siguientes valores pequeños, adecuados solo para aprender:")
    add_formula(doc, "q = 17,   A = [[4, 7], [3, 5]],   s = [2, 6]ᵀ,   e = [1, −1]ᵀ")
    numbered(
        doc,
        "Multiplicamos la matriz por el secreto.",
        "Añadimos el error antes de reducir módulo 17.",
        "Publicamos A y b; mantenemos s en secreto.",
    )
    add_formula(doc, "A·s = [4·2 + 7·6, 3·2 + 5·6]ᵀ = [50, 36]ᵀ")
    add_formula(doc, "b = [50, 36]ᵀ + [1, −1]ᵀ = [51, 35]ᵀ ≡ [0, 1]ᵀ   (mod 17)")
    paragraphs(
        doc,
        "Sin el error se observaría el resultado exacto. Con el error, el par público se parece a una "
        "ecuación lineal, pero no tiene una solución exacta ordinaria. Los parámetros reales contienen "
        "muchas más dimensiones y distribuciones de ruido cuidadosamente definidas.",
    )

    section(doc, "7. Ejemplo guiado: encapsulación didáctica de un bit")
    paragraphs(
        doc,
        "Esta miniatura no es ML-KEM real. Conserva únicamente la intuición de mezclar un mensaje con "
        "una muestra LWE y recuperarlo por proximidad. Usamos el par público anterior y codificamos el "
        "bit uno cerca de la mitad del módulo.",
    )
    add_formula(doc, "m = 1,   Δ = ⌊q/2⌋ = 8,   r = [1, 1]ᵀ")
    add_formula(doc, "u = Aᵀ·r = [7, 12]ᵀ   (mod 17)")
    add_formula(doc, "v = bᵀ·r + Δ·m = 1 + 8 = 9   (mod 17)")
    add_formula(doc, "c = (u, v) = ([7, 12]ᵀ, 9)")
    paragraphs(doc, "El receptor usa el secreto para retirar la parte lineal:")
    add_formula(doc, "sᵀ·u = 2·7 + 6·12 = 86 ≡ 1   (mod 17)")
    add_formula(doc, "v − sᵀ·u = 9 − 1 = 8 = Δ   ⇒   m = 1")
    paragraphs(
        doc,
        "La versión estandarizada incorpora polinomios, compresión, hashes, comprobación implícita del "
        "texto de encapsulación y una transformación de seguridad. El ejemplo solo explica por qué un "
        "error pequeño todavía permite decidir entre dos regiones del módulo.",
    )

    section(doc, "8. Ejercicios")
    exercise(doc, 1, "Muestra LWE", "Calcula el vector público para:")
    add_formula(doc, "q = 17,   A = [[6, 2], [1, 8]],   s = [3, 4]ᵀ,   e = [−1, 1]ᵀ")
    add_formula(doc, "b = A·s + e   (mod 17)")
    solution(doc, "El producto es el siguiente:")
    add_formula(doc, "A·s = [26, 35]ᵀ,   A·s + e = [25, 36]ᵀ ≡ [8, 2]ᵀ   (mod 17)")

    exercise(doc, 2, "Desencapsulación", "Recupera el bit a partir de:")
    add_formula(doc, "q = 17,   s = [2, 6]ᵀ,   u = [7, 12]ᵀ,   v = 9")
    solution(doc, "Se obtiene el valor codificado en la mitad del módulo:")
    add_formula(doc, "v − sᵀ·u = 9 − 86 ≡ 8   (mod 17)   ⇒   m = 1")

    exercise(
        doc,
        3,
        "Concepto de KEM",
        "Indica cuáles de estos datos pueden viajar por la red: ek, dk, c y K. Explica por qué un KEM "
        "no sustituye a AES-GCM.",
    )
    solution(
        doc,
        "Pueden transmitirse ek y c. dk y K son secretos. El KEM establece K; AES-GCM usa una clave "
        "derivada de K para aportar confidencialidad e integridad a mensajes de longitud arbitraria.",
    )

    section(doc, "9. Python: ML-KEM dentro de un cifrado híbrido")
    paragraphs(
        doc,
        "El siguiente ejemplo usa implementaciones ya hechas. liboqs proporciona ML-KEM y "
        "cryptography proporciona HKDF y AES-GCM. El código es apropiado para laboratorio y prototipado; "
        "un producto debe usar una biblioteca y una integración validadas para su entorno.",
    )
    add_code(
        doc,
        r'''
import os

import oqs
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.hkdf import HKDF


def derive_key(shared_secret: bytes, context: bytes) -> bytes:
    return HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"orders-api:" + context,
    ).derive(shared_secret)


algorithm = "ML-KEM-768"
message = b'{"order_id":42,"amount":"199.00"}'
aad = b"orders-api:v1"

with oqs.KeyEncapsulation(algorithm) as server:
    public_key = server.generate_keypair()

    with oqs.KeyEncapsulation(algorithm) as client:
        kem_ciphertext, secret_client = client.encap_secret(public_key)

    secret_server = server.decap_secret(kem_ciphertext)
    assert secret_client == secret_server

    nonce = os.urandom(12)
    key_client = derive_key(secret_client, aad)
    ciphertext = AESGCM(key_client).encrypt(nonce, message, aad)

    key_server = derive_key(secret_server, aad)
    plaintext = AESGCM(key_server).decrypt(nonce, ciphertext, aad)
    assert plaintext == message
''',
    )
    exercise(
        doc,
        4,
        "Python",
        "Cambia el valor de aad únicamente durante el descifrado. Anota la excepción y explica qué "
        "propiedad aporta el cifrado autenticado.",
    )
    solution(
        doc,
        "El descifrado falla porque AES-GCM autentica tanto el ciphertext como los datos asociados. "
        "Esto detecta una modificación aunque aad no esté cifrado.",
    )

    section(doc, "10. Cómo se integra en un proyecto")
    add_table(
        doc,
        ["Elemento", "Se guarda o transmite", "Tratamiento"],
        [
            ["public_key / ek", "Directorio, certificado o configuración", "Autenticar su propietario"],
            ["kem_ciphertext / c", "Mensaje de establecimiento", "Puede ser público"],
            ["nonce y aad", "Junto al ciphertext simétrico", "No son secretos; no reutilizar nonce"],
            ["shared_secret / K", "Solo en memoria", "Derivar clave y eliminar cuanto antes"],
            ["secret_key / dk", "Servidor, HSM o módulo protegido", "Rotación, acceso mínimo y sin logs"],
        ],
    )
    paragraphs(
        doc,
        "Durante una migración se puede combinar un secreto clásico y uno post-cuántico dentro de un "
        "protocolo híbrido revisado. No basta con concatenar algoritmos de manera improvisada: la "
        "identidad, la transcripción del protocolo y el contexto deben quedar ligados a la derivación.",
    )
    add_formula(doc, "K_sesión = HKDF(K_clásico ∥ K_PQC, contexto_del_protocolo)")

    section(doc, "11. Ideas clave")
    bullets(
        doc,
        "La criptografía post-cuántica se ejecuta hoy en sistemas clásicos.",
        "ML-KEM establece un secreto compartido; no cifra directamente todos los datos.",
        "Su intuición matemática parte de ecuaciones modulares con ruido.",
        "Una integración real necesita KDF, cifrado autenticado, autenticación de claves y gestión segura." ,
    )
    section(doc, "12. Fuentes esenciales")
    bullets(
        doc,
        "NIST FIPS 203, Module-Lattice-Based Key-Encapsulation Mechanism Standard: https://csrc.nist.gov/pubs/fips/203/final",
        "NIST SP 800-227, Recommendations for Key-Encapsulation Mechanisms: https://csrc.nist.gov/pubs/sp/800/227/final",
        "Open Quantum Safe, liboqs-python: https://github.com/open-quantum-safe/liboqs-python",
    )
    return doc


def build_session_5() -> Document:
    title = "Sesión 5. Métodos de criptografía post-cuántica (II)"
    doc = start_document(
        title,
        "Método principal: NTRU, una construcción basada en retículos y aritmética de polinomios.",
    )

    section(doc, "1. Objetivos y guion de la sesión")
    bullets(
        doc,
        "Interpretar un polinomio como un vector de coeficientes.",
        "Calcular productos en un anillo con convolución circular.",
        "Comprender generación de claves, cifrado y descifrado de NTRU.",
        "Comprobar el ejemplo con una implementación didáctica en Python.",
    )
    add_table(
        doc,
        ["Minutos", "Actividad"],
        [
            ["0-7", "Anillo de polinomios y convolución circular."],
            ["7-14", "Construcción de claves NTRU."],
            ["14-23", "Ejemplo completo de cifrado y descifrado."],
            ["23-28", "Ejercicios y comprobación con Python."],
            ["28-30", "Uso y posición actual de NTRU."],
        ],
    )

    section(doc, "2. Idea central de NTRU")
    paragraphs(
        doc,
        "NTRU representa mensajes, claves y aleatoriedad como polinomios de coeficientes pequeños. "
        "La clave pública mezcla dos polinomios secretos mediante una inversa modular. Para quien "
        "conoce la clave privada, multiplicar el ciphertext por el polinomio adecuado devuelve los "
        "coeficientes a una zona pequeña desde la que puede recuperarse el mensaje.",
        "La intuición geométrica es la de un retículo: muchas combinaciones públicas son posibles, pero "
        "la clave privada proporciona una representación corta y útil. En clase trabajaremos desde la "
        "aritmética de polinomios, que permite ver todas las operaciones.",
    )

    section(doc, "3. Base matemática: el anillo de polinomios")
    paragraphs(
        doc,
        "Fijamos un grado N y hacemos que los términos que superan ese grado vuelvan al principio. "
        "Cuando se reduce por el polinomio indicado abajo, se cumple que la potencia N-ésima equivale a "
        "uno. El producto se convierte así en una convolución circular.",
    )
    add_formula(doc, "R = ℤ[x] / (xᴺ − 1)")
    add_formula(doc, "xᴺ ≡ 1,   xᴺ⁺¹ ≡ x,   xᴺ⁺² ≡ x²")
    add_formula(doc, "(a ∗ b)ₖ = Σᵢ₌₀ᴺ⁻¹ aᵢ · b₍ₖ₋ᵢ₎ mod N")
    paragraphs(
        doc,
        "Además se reducen los coeficientes con dos módulos. El módulo pequeño representa el mensaje y "
        "el módulo grande deja espacio para mezclar mensaje y aleatoriedad sin perder la posibilidad de "
        "centrar los coeficientes durante el descifrado.",
    )
    add_formula(doc, "R_p = (ℤ/pℤ)[x]/(xᴺ − 1),   R_q = (ℤ/qℤ)[x]/(xᴺ − 1),   p < q")

    section(doc, "4. Generación de claves NTRU")
    paragraphs(
        doc,
        "Se eligen polinomios pequeños f y g. El requisito importante es que f tenga inversa en los dos "
        "módulos. Ser invertible significa que existe otro polinomio cuyo producto con f equivale al "
        "elemento neutro.",
    )
    add_formula(doc, "f ∗ f_p⁻¹ ≡ 1   (mod p, xᴺ − 1)")
    add_formula(doc, "f ∗ f_q⁻¹ ≡ 1   (mod q, xᴺ − 1)")
    paragraphs(doc, "La clave pública se calcula mezclando la inversa módulo q con g:")
    add_formula(doc, "h ≡ p · f_q⁻¹ ∗ g   (mod q)")
    bullets(
        doc,
        "Clave pública: h.",
        "Clave privada: f y su inversa módulo p; algunas variantes conservan más valores.",
        "Seguridad: recuperar polinomios cortos compatibles con h debe ser difícil con parámetros reales.",
    )

    section(doc, "5. Cifrado y descifrado")
    paragraphs(
        doc,
        "Para cifrar se elige un polinomio aleatorio pequeño r. Su presencia hace que dos cifrados del "
        "mismo mensaje sean distintos. El receptor multiplica por f y, gracias a la definición de h, "
        "la parte que contiene g queda multiplicada por p y desaparece al reducir módulo p.",
    )
    add_formula(doc, "c ≡ r ∗ h + m   (mod q)")
    add_formula(doc, "a ≡ f ∗ c   (mod q)")
    add_formula(doc, "a ≡ p · r ∗ g + f ∗ m   (mod q)")
    paragraphs(
        doc,
        "Antes de reducir módulo p se centran los coeficientes de a en un intervalo alrededor de cero. "
        "Este paso es esencial: un residuo grande módulo q puede representar realmente un número negativo "
        "pequeño. Finalmente se multiplica por la inversa de f módulo p.",
    )
    add_formula(doc, "m ≡ f_p⁻¹ ∗ center_q(a)   (mod p)")

    section(doc, "6. Ejemplo guiado completo")
    paragraphs(
        doc,
        "Usamos vectores de cuatro coeficientes. La posición i representa el coeficiente de la potencia "
        "i-ésima. Los números son deliberadamente pequeños y no ofrecen seguridad.",
    )
    add_formula(doc, "N = 4,   p = 3,   q = 17")
    add_formula(doc, "f = 1 + 3x = [1, 3, 0, 0]")
    add_formula(doc, "g = x − x² = [0, 1, −1, 0]")
    add_formula(doc, "f_p⁻¹ = 1,   f_q⁻¹ = [7, 13, 12, 15]")
    paragraphs(doc, "Primero comprobamos la inversa y calculamos la clave pública:")
    add_formula(doc, "f ∗ f_q⁻¹ ≡ [1, 0, 0, 0]   (mod 17)")
    add_formula(doc, "f_q⁻¹ ∗ g ≡ [3, 9, 6, 16]   (mod 17)")
    add_formula(doc, "h ≡ 3 · [3, 9, 6, 16] ≡ [9, 10, 1, 14]   (mod 17)")
    paragraphs(doc, "Ciframos un mensaje pequeño con un polinomio aleatorio pequeño:")
    add_formula(doc, "m = 1 − x² = [1, 0, −1, 0],   r = 1 + x² = [1, 0, 1, 0]")
    add_formula(doc, "r ∗ h ≡ [10, 7, 10, 7]   (mod 17)")
    add_formula(doc, "c ≡ r ∗ h + m ≡ [11, 7, 9, 7]   (mod 17)")
    paragraphs(doc, "El receptor multiplica por f y centra cada coeficiente:")
    add_formula(doc, "a ≡ f ∗ c ≡ [15, 6, 13, 0]   (mod 17)")
    add_formula(doc, "center₁₇(a) = [−2, 6, −4, 0]")
    add_formula(doc, "m ≡ f_p⁻¹ ∗ a ≡ [1, 0, 2, 0]   (mod 3)")
    paragraphs(
        doc,
        "El residuo dos módulo tres representa menos uno. Por tanto se recupera el vector original. El "
        "descifrado puede fallar si los coeficientes crecen demasiado y el centrado deja de distinguir "
        "la representación correcta; los parámetros reales se eligen para controlar esa probabilidad.",
    )
    add_formula(doc, "[1, 0, 2, 0]   (mod 3) = [1, 0, −1, 0] = m")

    section(doc, "7. Ejercicios")
    exercise(
        doc,
        1,
        "Convolución circular",
        "En el anillo de grado cuatro, multiplica los siguientes polinomios:",
    )
    add_formula(doc, "a = 1 + x,   b = 1 + x³,   x⁴ ≡ 1")
    solution(doc, "Se desarrolla el producto y se pliega la cuarta potencia:")
    add_formula(doc, "a·b = 1 + x + x³ + x⁴ ≡ 2 + x + x³")

    exercise(
        doc,
        2,
        "Cifrado",
        "Con la clave pública del ejemplo y los valores indicados, calcula el ciphertext.",
    )
    add_formula(doc, "h = [9, 10, 1, 14],   r = [1, 0, 1, 0],   m = [1, 0, −1, 0]")
    solution(doc, "La convolución y la suma producen:")
    add_formula(doc, "c ≡ [10, 7, 10, 7] + [1, 0, −1, 0] ≡ [11, 7, 9, 7]   (mod 17)")

    exercise(
        doc,
        3,
        "Centrado",
        "Centra los residuos siguientes en el intervalo de menos ocho a ocho y redúcelos módulo tres.",
    )
    add_formula(doc, "[15, 6, 13, 0]   (mod 17)")
    solution(doc, "Los residuos quince y trece representan menos dos y menos cuatro:")
    add_formula(doc, "[15, 6, 13, 0] → [−2, 6, −4, 0] → [1, 0, 2, 0]   (mod 3)")

    exercise(
        doc,
        4,
        "Razonamiento",
        "Explica por qué el término que contiene g desaparece al final del descifrado.",
    )
    solution(doc, "Ese término contiene el factor p, por lo que todos sus coeficientes son cero módulo p.")
    add_formula(doc, "p · r ∗ g ≡ 0   (mod p)")

    section(doc, "8. Python: implementación didáctica ya resuelta")
    paragraphs(
        doc,
        "El programa reproduce exactamente el ejemplo. Implementa únicamente convolución circular y "
        "reducción modular; las inversas ya calculadas se introducen como datos para que el ejercicio se "
        "centre en la mecánica de NTRU.",
    )
    add_code(
        doc,
        r'''
N = 4
P = 3
Q = 17


def cyclic_convolution(a: list[int], b: list[int], modulus: int) -> list[int]:
    return [
        sum(a[i] * b[(k - i) % N] for i in range(N)) % modulus
        for k in range(N)
    ]


def add_mod(a: list[int], b: list[int], modulus: int) -> list[int]:
    return [(x + y) % modulus for x, y in zip(a, b)]


def center(values: list[int], modulus: int) -> list[int]:
    return [x if x <= modulus // 2 else x - modulus for x in values]


f = [1, 3, 0, 0]
f_inv_p = [1, 0, 0, 0]
f_inv_q = [7, 13, 12, 15]
g = [0, 1, -1, 0]
m = [1, 0, -1, 0]
r = [1, 0, 1, 0]

assert cyclic_convolution(f, f_inv_q, Q) == [1, 0, 0, 0]

h = [(P * x) % Q for x in cyclic_convolution(f_inv_q, g, Q)]
c = add_mod(cyclic_convolution(r, h, Q), m, Q)

a = center(cyclic_convolution(f, c, Q), Q)
recovered = cyclic_convolution(f_inv_p, a, P)

assert h == [9, 10, 1, 14]
assert c == [11, 7, 9, 7]
assert recovered == [1, 0, 2, 0]  # 2 representa -1 módulo 3
''',
    )
    exercise(
        doc,
        5,
        "Python",
        "Cambia el mensaje por el vector [0, 1, 0, -1], cifra, descifra y comprueba el resultado con un "
        "assert. Después cambia r y verifica que cambia c pero no el mensaje recuperado.",
    )

    section(doc, "9. Uso con una implementación existente")
    paragraphs(
        doc,
        "liboqs mantiene NTRU para experimentación e interoperabilidad. El patrón de uso vuelve a ser el "
        "de un KEM; en un proyecto se reutilizaría el mismo sobre digital de la sesión 4. NTRU no fue "
        "seleccionado como estándar NIST, por lo que no debe presentarse como sustituto normativo de ML-KEM.",
    )
    add_code(
        doc,
        r'''
import oqs


algorithm = "NTRU-HPS-2048-509"
enabled = oqs.get_enabled_kem_mechanisms()
if algorithm not in enabled:
    raise RuntimeError(f"{algorithm} no está habilitado en esta compilación de liboqs")

with oqs.KeyEncapsulation(algorithm) as receiver:
    public_key = receiver.generate_keypair()
    with oqs.KeyEncapsulation(algorithm) as sender:
        kem_ciphertext, secret_sender = sender.encap_secret(public_key)
    secret_receiver = receiver.decap_secret(kem_ciphertext)

assert secret_sender == secret_receiver
''',
    )
    bullets(
        doc,
        "No implementar NTRU desde el ejemplo de aula: faltan parámetros seguros, codificación y defensas.",
        "Comprobar el estado normativo del algoritmo antes de elegirlo para un producto.",
        "Proteger las claves y evitar diferencias observables entre tipos de fallo.",
        "Usar el secreto KEM mediante una KDF y un cifrado autenticado, igual que con ML-KEM.",
    )

    section(doc, "10. Ideas clave")
    bullets(
        doc,
        "NTRU permite ver una construcción de retículos a través de polinomios y convolución circular.",
        "La inversa de f y el centrado de coeficientes son los pasos que hacen posible el descifrado.",
        "Los ejemplos pequeños explican la mecánica, pero no aportan seguridad.",
        "En el ecosistema NIST actual, ML-KEM es el KEM principal estandarizado; NTRU tiene valor docente e histórico.",
    )
    section(doc, "11. Fuentes esenciales")
    bullets(
        doc,
        "Hoffstein, Pipher y Silverman, NTRU: A Ring-Based Public Key Cryptosystem.",
        "NTRU Round 3 Submission Package: https://ntru.org/",
        "Open Quantum Safe, estado de algoritmos: https://github.com/open-quantum-safe/liboqs",
        "NIST IR 8545, estado de la cuarta ronda: https://csrc.nist.gov/pubs/ir/8545/final",
    )
    return doc


def build_session_6() -> Document:
    title = "Sesión 6. Métodos de criptografía post-cuántica (III). Estado actual"
    doc = start_document(
        title,
        "Métodos: ML-DSA y SLH-DSA. Cierre: estándares y migración a fecha de 12 de septiembre de 2026.",
    )

    section(doc, "1. Objetivos y guion de la sesión")
    bullets(
        doc,
        "Distinguir firma digital, cifrado y encapsulación de claves.",
        "Comprender la ecuación de verificación de ML-DSA.",
        "Entender una firma basada en hash mediante un árbol de Merkle.",
        "Interpretar el estado actual de la estandarización y proponer una migración práctica.",
    )
    add_table(
        doc,
        ["Minutos", "Actividad"],
        [
            ["0-4", "Firma frente a KEM y cifrado."],
            ["4-15", "ML-DSA: explicación, ejemplo y ejercicio."],
            ["15-22", "SLH-DSA: explicación, ejemplo y ejercicio."],
            ["22-26", "Python aplicado a documentos firmados."],
            ["26-30", "Estado actual y ejercicio de migración."],
        ],
    )

    section(doc, "2. Firma, cifrado y KEM no son lo mismo")
    add_table(
        doc,
        ["Primitiva", "Objetivo", "Operación principal", "Secreto principal"],
        [
            ["KEM", "Establecer una clave", "Encapsular / desencapsular", "Clave de desencapsulación"],
            ["Cifrado AEAD", "Ocultar y autenticar datos", "Cifrar / descifrar", "Clave simétrica"],
            ["Firma", "Probar origen e integridad", "Firmar / verificar", "Clave de firma"],
        ],
    )
    paragraphs(
        doc,
        "Una firma no oculta el mensaje. El emisor calcula una firma con su clave privada y cualquier "
        "receptor puede verificarla con la clave pública. La validez solo tiene sentido si el verificador "
        "confía en que esa clave pública pertenece realmente al firmante.",
    )
    add_formula(doc, "σ ← Sign(sk, m)")
    add_formula(doc, "Verify(pk, m, σ) ∈ {válida, inválida}")

    section(doc, "3. Método 1: ML-DSA explicado")
    paragraphs(
        doc,
        "ML-DSA, derivado de CRYSTALS-Dilithium, es la firma principal de NIST basada en retículos. "
        "Trabaja con vectores de polinomios, secretos pequeños y una versión no interactiva de un "
        "protocolo de reto-respuesta. La explicación siguiente omite el redondeo, las pistas y varios "
        "hashes, pero mantiene la ecuación que conecta firma y verificación.",
        "La clave pública contiene una matriz generada de forma determinista y un producto ruidoso del "
        "secreto. El ruido evita que la clave pública sea un sistema lineal exacto del que se extraiga el "
        "secreto.",
    )
    add_formula(doc, "t = A·s₁ + s₂   (mod q)")
    paragraphs(
        doc,
        "Para firmar se elige un vector efímero y, se calcula un compromiso. El reto se obtiene mediante "
        "un hash que incluye el mensaje; esta es la idea de la transformación Fiat-Shamir.",
    )
    add_formula(doc, "w = A·y   (mod q)")
    add_formula(doc, "c = H(μ ∥ highBits(w))")
    add_formula(doc, "z = y + c·s₁")
    paragraphs(
        doc,
        "El firmante rechaza y vuelve a empezar si z u otros valores salen de los límites permitidos. "
        "Este muestreo por rechazo evita que la distribución de las firmas filtre información útil sobre "
        "el secreto. El verificador reconstruye el compromiso a partir de datos públicos.",
    )
    add_formula(doc, "w′ = A·z − c·t   (mod q)")
    add_formula(doc, "c ?= H(μ ∥ highBits(w′))")

    section(doc, "4. Ejemplo guiado de ML-DSA")
    paragraphs(
        doc,
        "La miniatura usa enteros en lugar de polinomios y elimina el ruido. No es una firma segura; "
        "permite comprobar a mano por qué la misma ecuación funciona al firmar y verificar.",
    )
    add_formula(doc, "q = 17,   A = [[4, 7], [3, 5]],   s = [2, 1]ᵀ")
    add_formula(doc, "t = A·s = [15, 11]ᵀ   (mod 17)")
    add_formula(doc, "y = [1, 2]ᵀ")
    add_formula(doc, "w = A·y = [18, 13]ᵀ ≡ [1, 13]ᵀ   (mod 17)")
    add_formula(doc, "c = H(m ∥ w) = 2")
    add_formula(doc, "z = y + c·s = [1, 2]ᵀ + 2·[2, 1]ᵀ = [5, 4]ᵀ")
    paragraphs(doc, "La firma didáctica es el par formado por la respuesta y el reto.")
    add_formula(doc, "σ = (z, c) = ([5, 4]ᵀ, 2)")
    paragraphs(doc, "El verificador reconstruye el compromiso:")
    add_formula(doc, "A·z ≡ [14, 1]ᵀ,   c·t ≡ [13, 5]ᵀ   (mod 17)")
    add_formula(doc, "A·z − c·t ≡ [1, 13]ᵀ = w   (mod 17)")
    paragraphs(
        doc,
        "Si cambia el mensaje, cambia el reto calculado por el hash. La firma antigua deja de ser "
        "coherente aunque z no se haya modificado.",
    )

    section(doc, "5. Ejercicios de ML-DSA")
    exercise(doc, 1, "Verificación", "Comprueba la firma con los datos del ejemplo:")
    add_formula(doc, "z = [5, 4]ᵀ,   c = 2,   t = [15, 11]ᵀ")
    solution(doc, "La reconstrucción coincide con el compromiso original:")
    add_formula(doc, "A·z − c·t ≡ [14, 1]ᵀ − [13, 5]ᵀ ≡ [1, 13]ᵀ   (mod 17)")

    exercise(
        doc,
        2,
        "Mensaje alterado",
        "Supón que al modificar el mensaje el reto pasa a cinco. Verifica usando el mismo valor z.",
    )
    solution(doc, "La reconstrucción ya no coincide con el compromiso firmado:")
    add_formula(doc, "A·z − 5·t ≡ [14, 1]ᵀ − [7, 4]ᵀ ≡ [7, 14]ᵀ   (mod 17)")

    exercise(
        doc,
        3,
        "Muestreo por rechazo",
        "Explica qué podría ocurrir si el firmante publicara siempre z, incluso cuando sus coeficientes "
        "fueran anormalmente grandes.",
    )
    solution(
        doc,
        "La distribución de z dependería de forma observable del secreto. Muchas firmas podrían aportar "
        "información estadística; por eso ML-DSA impone cotas y repite la muestra cuando es necesario.",
    )

    section(doc, "6. Método 2: SLH-DSA explicado")
    paragraphs(
        doc,
        "SLH-DSA deriva de SPHINCS+ y basa su seguridad principalmente en propiedades de funciones hash. "
        "Combina firmas de un solo uso, esquemas de pocos usos y árboles de Merkle. Su principal ventaja "
        "conceptual es la diversidad matemática: no depende de retículos. A cambio, sus firmas suelen ser "
        "considerablemente mayores que las de ML-DSA.",
        "Cada hoja del árbol compromete una clave pública de un solo uso. La raíz resume todas las hojas "
        "y forma parte de la clave pública global. Para verificar una hoja no hace falta enviar el árbol "
        "completo: basta la firma y el camino de autenticación formado por los nodos hermanos.",
    )
    add_formula(doc, "leafᵢ = H(pkᵢᴼᵀˢ)")
    add_formula(doc, "node = H(left ∥ right)")
    add_formula(doc, "pk_SLH-DSA contiene root(árbol)")
    paragraphs(
        doc,
        "SLH-DSA es stateless: el firmante no necesita recordar qué hoja utilizó entre una firma y la "
        "siguiente. Esa propiedad evita fallos catastróficos de gestión de estado presentes en otros "
        "esquemas hash, aunque exige una construcción más elaborada.",
    )

    section(doc, "7. Ejemplo guiado de árbol de Merkle")
    paragraphs(
        doc,
        "Para poder calcular a mano usamos un hash de juguete. Sumar módulo diecisiete no es una función "
        "hash segura; solo representa la operación de combinar dos hijos.",
    )
    add_formula(doc, "H(a ∥ b) = (a + b) mod 17")
    add_formula(doc, "L₀ = 3,   L₁ = 5,   L₂ = 8,   L₃ = 2")
    add_formula(doc, "N₀ = H(L₀ ∥ L₁) = 8,   N₁ = H(L₂ ∥ L₃) = 10")
    add_formula(doc, "root = H(N₀ ∥ N₁) = 18 mod 17 = 1")
    paragraphs(
        doc,
        "Para autenticar la hoja L₁ se entrega como camino su hermano L₀ y el nodo N₁. El verificador "
        "reconstruye primero N₀ y después la raíz. Si obtiene la raíz pública, la hoja está ligada al árbol.",
    )
    add_formula(doc, "H(L₀ ∥ L₁) = H(3 ∥ 5) = 8")
    add_formula(doc, "H(8 ∥ N₁) = H(8 ∥ 10) = 1 = root")

    section(doc, "8. Ejercicios de SLH-DSA")
    exercise(
        doc,
        4,
        "Camino de autenticación",
        "Verifica la hoja L₂ usando como camino L₃ y N₀.",
    )
    solution(doc, "Primero se reconstruye el nodo derecho y después la raíz:")
    add_formula(doc, "N₁ = H(8 ∥ 2) = 10,   root = H(8 ∥ 10) = 1")

    exercise(
        doc,
        5,
        "Manipulación",
        "Sustituye L₂ por nueve y calcula la nueva raíz. ¿Validaría frente a la raíz pública original?",
    )
    solution(doc, "La nueva raíz es distinta, por lo que la verificación debe fallar:")
    add_formula(doc, "N₁′ = H(9 ∥ 2) = 11,   root′ = H(8 ∥ 11) = 2 ≠ 1")

    section(doc, "9. Python: firma de un documento real")
    paragraphs(
        doc,
        "La aplicación firma bytes canónicos de un JSON. La canonización es parte del contrato: si el "
        "emisor y el verificador serializan el mismo objeto de forma distinta, verificarán secuencias de "
        "bytes diferentes. El mismo ejercicio se ejecuta con ML-DSA y con SLH-DSA si ambos mecanismos "
        "están habilitados.",
    )
    add_code(
        doc,
        r'''
import json

import oqs


def canonical_json(data: dict) -> bytes:
    return json.dumps(
        data,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def sign_and_check(algorithm: str, message: bytes) -> tuple[bytes, bytes]:
    with oqs.Signature(algorithm) as signer:
        public_key = signer.generate_keypair()
        signature = signer.sign(message)

    with oqs.Signature(algorithm) as verifier:
        assert verifier.verify(message, signature, public_key)
    return public_key, signature


invoice = {
    "invoice_id": "F-2026-0007",
    "customer": "ACME",
    "amount": "199.00",
    "currency": "EUR",
}
message = canonical_json(invoice)

enabled = set(oqs.get_enabled_sig_mechanisms())
algorithms = ["ML-DSA-65", "SLH-DSA-SHA2-128s"]

for algorithm in algorithms:
    if algorithm in enabled:
        public_key, signature = sign_and_check(algorithm, message)
        print(algorithm, len(public_key), len(signature))

tampered = canonical_json({**invoice, "amount": "299.00"})
assert tampered != message
''',
    )
    exercise(
        doc,
        6,
        "Python",
        "Guarda la clave pública y la firma devueltas para ML-DSA. Comprueba explícitamente que la firma "
        "no valida sobre tampered. Añade después el campo issued_at, vuelve a firmar y compara tamaños.",
    )
    paragraphs(
        doc,
        "En un proyecto, el sobre firmado debería incluir como mínimo el payload o su referencia, la "
        "firma, el identificador de algoritmo, un key_id y la versión del formato canónico. La clave "
        "privada debe permanecer en un HSM, KMS o módulo protegido cuando el riesgo lo justifique.",
    )

    section(doc, "10. Estado actual a 12 de septiembre de 2026")
    add_table(
        doc,
        ["Algoritmo", "Base", "Estado NIST", "Lectura práctica"],
        [
            ["ML-KEM", "Retículos / Module-LWE", "FIPS 203 final desde agosto de 2024", "KEM principal para migración"],
            ["ML-DSA", "Retículos", "FIPS 204 final desde agosto de 2024", "Firma principal de propósito general"],
            ["SLH-DSA", "Funciones hash", "FIPS 205 final desde agosto de 2024", "Alternativa con diversidad matemática"],
            ["FN-DSA (Falcon)", "Retículos NTRU", "FIPS 206 en desarrollo", "Firmas compactas; implementación compleja"],
            ["HQC-KEM", "Códigos correctores", "Seleccionado; FIPS 207 en desarrollo", "Respaldo no basado en retículos"],
        ],
    )
    paragraphs(
        doc,
        "Los tres primeros estándares están listos para adopción. NIST recomienda iniciar la migración "
        "y publicó en 2025 la guía final SP 800-227 para usar KEM de forma segura. En 2026 también publicó "
        "orientación de criptoagilidad: la migración no consiste solo en cambiar una función, sino en "
        "poder inventariar, sustituir y versionar algoritmos sin rediseñar todo el sistema.",
        "HQC fue elegido en marzo de 2025 como segundo KEM y como alternativa matemática a ML-KEM. El "
        "proceso adicional de firmas pasó a tercera ronda en mayo de 2026. HAWK se retiró en julio, por "
        "lo que continúan ocho candidatos activos: FAEST, MAYO, MQOM, QR-UOV, SDitH, SNOVA, SQIsign y UOV.",
        "Que un algoritmo sea post-cuántico no significa que toda implementación sea segura. Siguen "
        "importando los canales laterales, la generación aleatoria, la validación de entradas, la "
        "protección de claves y el protocolo que combina las primitivas.",
    )

    section(doc, "11. Ejercicio final: migrar un proyecto")
    exercise(
        doc,
        7,
        "Diseño",
        "Una API usa ECDH para establecer sesión y ECDSA para firmar releases. Los datos protegidos deben "
        "seguir siendo confidenciales durante quince años. Propón un plan de cuatro pasos.",
    )
    solution(
        doc,
        "Primero se inventarían algoritmos, claves, certificados, bibliotecas y vida útil de los datos. "
        "Después se probaría ML-KEM en el establecimiento, inicialmente dentro de un protocolo híbrido "
        "revisado. En paralelo se migraría la firma de releases a ML-DSA o SLH-DSA según restricciones de "
        "tamaño. Finalmente se añadirían identificadores y versiones de algoritmo, métricas, rotación, "
        "pruebas de interoperabilidad y un mecanismo de retirada.",
    )
    add_formula(doc, "K_sesión = KDF(K_ECDH ∥ K_ML-KEM, transcripción_autenticada)")

    exercise(
        doc,
        8,
        "Decisión técnica",
        "Elige entre ML-DSA y SLH-DSA para firmar millones de respuestas pequeñas. Indica qué medirías "
        "antes de decidir.",
    )
    solution(
        doc,
        "ML-DSA suele ser el punto de partida por su equilibrio general. Deben medirse tamaño de firma, "
        "latencia de firma y verificación, memoria, ancho de banda, soporte de biblioteca, validación del "
        "módulo y necesidad de diversidad matemática. SLH-DSA puede preferirse cuando esa diversidad pesa "
        "más que el tamaño de firma.",
    )

    section(doc, "12. Ideas clave")
    bullets(
        doc,
        "ML-DSA verifica una respuesta corta ligada al mensaje mediante un reto hash.",
        "SLH-DSA enlaza firmas de un solo uso con una raíz pública mediante árboles hash.",
        "FIPS 203, 204 y 205 son finales; FN-DSA y HQC-KEM siguen en desarrollo.",
        "La tarea inmediata de un proyecto es ganar inventario y criptoagilidad y probar la migración." ,
    )

    section(doc, "13. Fuentes esenciales")
    bullets(
        doc,
        "NIST FIPS 204, ML-DSA: https://csrc.nist.gov/pubs/fips/204/final",
        "NIST FIPS 205, SLH-DSA: https://csrc.nist.gov/pubs/fips/205/final",
        "NIST PQC, algoritmos seleccionados: https://csrc.nist.gov/projects/post-quantum-cryptography/post-quantum-cryptography-standardization/selected-algorithms",
        "NIST IR 8545, selección de HQC: https://csrc.nist.gov/pubs/ir/8545/final",
        "NIST IR 8610, firmas adicionales: https://csrc.nist.gov/pubs/ir/8610/final",
        "NIST CSWP 39upd1, criptoagilidad: https://csrc.nist.gov/pubs/cswp/39/upd1/considerations-for-achieving-crypto-agility/final",
    )
    return doc


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    documents = [
        ("sesion_4_ml_kem_kyber.docx", build_session_4()),
        ("sesion_5_ntru.docx", build_session_5()),
        ("sesion_6_ml_dsa_dilithium.docx", build_session_6()),
    ]
    for filename, document in documents:
        destination = OUT_DIR / filename
        document.save(destination)
        print(f"Generated: {destination}")


if __name__ == "__main__":
    main()
