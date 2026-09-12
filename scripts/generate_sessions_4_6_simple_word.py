from generate_sessions_4_6_word import (
    OUT_DIR,
    add_code,
    add_formula,
    add_table,
    bullets,
    exercise,
    numbered,
    paragraphs,
    section,
    solution,
    start_document,
)


def build_session_4_simple():
    doc = start_document(
        "Sesión 4. Criptografía post-cuántica: introducción. Versión simplificada",
        "Método principal: ML-KEM explicado con aritmética básica y un flujo de proyecto.",
    )

    section(doc, "1. Qué aprenderemos")
    bullets(
        doc,
        "Por qué se están preparando nuevos algoritmos criptográficos.",
        "Qué es un mecanismo de encapsulación de claves o KEM.",
        "Cuál es la idea del ruido matemático usado por ML-KEM.",
        "Cómo se emplearía ML-KEM para proteger una comunicación real.",
    )
    add_table(
        doc,
        ["Minutos", "Actividad"],
        [
            ["0-6", "Problema que plantea la computación cuántica."],
            ["6-12", "Qué hace un KEM."],
            ["12-20", "Idea matemática y ejemplo sencillo."],
            ["20-26", "Ejercicios."],
            ["26-30", "Python y aplicación en un proyecto."],
        ],
    )

    section(doc, "2. Por qué necesitamos criptografía post-cuántica")
    paragraphs(
        doc,
        "Hoy usamos RSA y criptografía de curva elíptica para proteger muchas conexiones. Un ordenador "
        "cuántico suficientemente grande podría resolver con rapidez los problemas matemáticos que "
        "protegen estos sistemas. Por eso se preparan algoritmos basados en problemas diferentes.",
        "Post-cuántico no significa que necesitemos un ordenador cuántico. Los algoritmos se ejecutan en "
        "ordenadores normales, pero están diseñados para resistir los ataques cuánticos conocidos.",
        "No todas las técnicas post-cuánticas usan las mismas matemáticas. Hay métodos basados en "
        "retículos, códigos correctores y funciones hash. En esta sesión nos centramos en ML-KEM, basado "
        "en retículos.",
    )

    section(doc, "3. Qué hace un KEM")
    paragraphs(
        doc,
        "Un KEM permite que dos participantes obtengan el mismo secreto sin enviarlo directamente. El "
        "servidor publica una clave pública. El cliente la usa para crear un paquete de encapsulación y "
        "un secreto. El servidor abre el paquete con su clave privada y obtiene el mismo secreto.",
    )
    add_formula(doc, "KeyGen() → (clave pública, clave privada)")
    add_formula(doc, "Encaps(clave pública) → (paquete, secreto_cliente)")
    add_formula(doc, "Decaps(clave privada, paquete) → secreto_servidor")
    add_formula(doc, "secreto_cliente = secreto_servidor")
    paragraphs(
        doc,
        "El paquete puede viajar por una red pública. El secreto compartido no se transmite. Después se "
        "transforma en una clave para AES-GCM o ChaCha20-Poly1305, que son los algoritmos que cifran los "
        "datos de la aplicación.",
    )

    section(doc, "4. Matemáticas mínimas: trabajar módulo un número")
    paragraphs(
        doc,
        "Trabajar módulo un número significa quedarse con el resto. Es parecido a un reloj: después del "
        "último valor se vuelve al principio.",
    )
    add_formula(doc, "20 mod 17 = 3")
    paragraphs(
        doc,
        "La idea básica de LWE es multiplicar un valor público por un secreto y añadir un error pequeño. "
        "Ese pequeño error dificulta recuperar el secreto cuando el sistema real tiene muchas dimensiones.",
    )
    add_formula(doc, "b = a·s + e   (mod q)")
    bullets(
        doc,
        "a y b pueden ser públicos.",
        "s es el secreto.",
        "e es un error pequeño.",
        "q es el número usado como módulo.",
    )

    section(doc, "5. Ejemplo guiado")
    paragraphs(doc, "Usamos una sola ecuación para poder calcularla a mano:")
    add_formula(doc, "q = 17,   a = 4,   s = 3,   e = 1")
    add_formula(doc, "b = 4·3 + 1 = 13   (mod 17)")
    paragraphs(
        doc,
        "Sin error, el resultado habría sido doce. El dato público contiene ahora trece. En este ejemplo "
        "minúsculo todavía podemos probar todos los secretos, pero ML-KEM usa grandes conjuntos de "
        "ecuaciones, polinomios y errores aleatorios.",
    )
    add_formula(doc, "resultado sin error = 12,   resultado publicado = 13")

    section(doc, "6. Ejercicios")
    exercise(doc, 1, "Cálculo modular", "Calcula el dato público siguiente:")
    add_formula(doc, "q = 17,   a = 5,   s = 4,   e = 2")
    add_formula(doc, "b = a·s + e   (mod q)")
    solution(doc, "Primero se multiplica, después se suma el error y finalmente se calcula el resto.")
    add_formula(doc, "b = 5·4 + 2 = 22 ≡ 5   (mod 17)")

    exercise(
        doc,
        2,
        "Datos públicos y privados",
        "Clasifica estos elementos: clave pública, clave privada, paquete de encapsulación y secreto compartido.",
    )
    solution(
        doc,
        "La clave pública y el paquete pueden transmitirse. La clave privada y el secreto compartido "
        "deben mantenerse secretos.",
    )

    exercise(
        doc,
        3,
        "Orden del protocolo",
        "Ordena estas acciones: desencapsular, publicar la clave, generar las claves y encapsular.",
    )
    solution(
        doc,
        "El orden es: generar las claves, publicar la clave pública, encapsular y desencapsular.",
    )

    section(doc, "7. Python: ML-KEM con una implementación existente")
    paragraphs(
        doc,
        "Este programa no implementa las matemáticas de ML-KEM. Usa liboqs, una biblioteca creada para "
        "probar algoritmos post-cuánticos, y comprueba que cliente y servidor obtienen el mismo secreto.",
    )
    add_code(
        doc,
        r'''
import oqs


algorithm = "ML-KEM-768"

with oqs.KeyEncapsulation(algorithm) as server:
    public_key = server.generate_keypair()

    with oqs.KeyEncapsulation(algorithm) as client:
        package, secret_client = client.encap_secret(public_key)

    secret_server = server.decap_secret(package)

assert secret_client == secret_server
print("Secreto compartido correctamente")
''',
    )
    exercise(
        doc,
        4,
        "Python",
        "Muestra la longitud de public_key, package y secret_client con len(). Indica cuáles viajarían "
        "por la red y cuál no debería mostrarse ni guardarse en un log.",
    )

    section(doc, "8. Uso en un proyecto")
    numbered(
        doc,
        "El servidor crea y protege su par de claves ML-KEM.",
        "El cliente obtiene una copia auténtica de la clave pública.",
        "Cliente y servidor ejecutan encapsulación y desencapsulación.",
        "Los dos derivan una clave de sesión desde el secreto compartido.",
        "La aplicación cifra sus mensajes con AES-GCM.",
    )
    add_formula(doc, "ML-KEM → secreto → KDF → clave AES-GCM → datos cifrados")
    paragraphs(
        doc,
        "La parte más importante para el proyecto es recordar que ML-KEM establece la clave. No sustituye "
        "al cifrado autenticado, a los certificados ni a la protección de la clave privada.",
    )

    section(doc, "9. Resumen")
    bullets(
        doc,
        "La criptografía post-cuántica se puede usar en ordenadores actuales.",
        "ML-KEM permite acordar un secreto sin enviarlo.",
        "El ruido matemático ayuda a ocultar el secreto.",
        "En un proyecto se usa una biblioteca revisada y después un cifrado simétrico.",
    )
    return doc


def build_session_5_simple():
    doc = start_document(
        "Sesión 5. Métodos de criptografía post-cuántica (II). Versión simplificada",
        "Método principal: NTRU explicado con polinomios cortos y operaciones visuales.",
    )

    section(doc, "1. Qué aprenderemos")
    bullets(
        doc,
        "Representar un polinomio como una lista de números.",
        "Entender qué significa que un producto vuelva al principio.",
        "Seguir los pasos principales de NTRU sin calcular inversas difíciles.",
        "Comprobar un ejemplo mediante Python.",
    )
    add_table(
        doc,
        ["Minutos", "Actividad"],
        [
            ["0-8", "Polinomios como listas."],
            ["8-14", "Idea de NTRU."],
            ["14-22", "Ejemplo guiado."],
            ["22-27", "Ejercicios."],
            ["27-30", "Python y uso real."],
        ],
    )

    section(doc, "2. Polinomios como listas")
    paragraphs(
        doc,
        "Un polinomio puede verse como una lista de coeficientes. La primera posición corresponde al "
        "término sin x, la segunda al coeficiente de x y así sucesivamente.",
    )
    add_formula(doc, "1 − x² ↔ [1, 0, −1, 0]")
    add_formula(doc, "2 + 3x + x³ ↔ [2, 3, 0, 1]")
    paragraphs(
        doc,
        "En el ejemplo de clase solo guardaremos cuatro posiciones. Cuando aparece la cuarta potencia, "
        "esta vuelve a la primera posición. Esto se llama producto circular.",
    )
    add_formula(doc, "x⁴ ≡ 1")
    add_formula(doc, "x·x³ = x⁴ ≡ 1")

    section(doc, "3. Idea sencilla de NTRU")
    paragraphs(
        doc,
        "NTRU crea una clave pública mezclando polinomios privados pequeños. Para cifrar, el emisor "
        "combina la clave pública con un polinomio aleatorio y añade el mensaje. La aleatoriedad hace que "
        "el mismo mensaje pueda producir resultados diferentes.",
    )
    add_formula(doc, "ciphertext = aleatoriedad·clave_pública + mensaje   (mod q)")
    add_formula(doc, "c = r·h + m   (mod q)")
    bullets(
        doc,
        "h es la clave pública.",
        "r es un polinomio aleatorio pequeño.",
        "m es el mensaje convertido en polinomio.",
        "c es el ciphertext que se transmite.",
    )
    paragraphs(
        doc,
        "La clave privada permite deshacer la mezcla. En NTRU real aparece la inversa de un polinomio. "
        "Una inversa es simplemente una operación que deshace otra; el ejemplo escogerá una clave privada "
        "muy sencilla para evitar ese cálculo.",
    )
    add_formula(doc, "3·5 = 15 ≡ 1   (mod 7)   ⇒   5 es el inverso de 3 módulo 7")

    section(doc, "4. Ejemplo guiado")
    paragraphs(
        doc,
        "Trabajamos con cuatro coeficientes. Elegimos una clave privada igual a uno únicamente para que "
        "el cálculo sea accesible. Esta elección no sería segura en un sistema real.",
    )
    add_formula(doc, "N = 4,   p = 3,   q = 17,   f = 1")
    add_formula(doc, "g = 1 + x,   h = p·g = 3 + 3x")
    paragraphs(doc, "Ciframos el mensaje usando una aleatoriedad pequeña:")
    add_formula(doc, "m = 1 − x²,   r = x")
    add_formula(doc, "r·h = x·(3 + 3x) = 3x + 3x²")
    add_formula(doc, "c = r·h + m = 1 + 3x + 2x²")
    paragraphs(
        doc,
        "Como la clave privada del ejemplo es uno, no cambia el ciphertext. Al reducir los coeficientes "
        "módulo tres, la parte creada por la clave pública desaparece. El coeficiente dos representa "
        "menos uno módulo tres.",
    )
    add_formula(doc, "c mod 3 = 1 + 0x + 2x² ≡ 1 − x² = m")

    section(doc, "5. Ejercicios")
    exercise(doc, 1, "Representación", "Convierte el polinomio siguiente en una lista de cuatro valores:")
    add_formula(doc, "2 − x + 3x³")
    solution(doc, "Se escriben en orden los coeficientes de uno, x, x al cuadrado y x al cubo.")
    add_formula(doc, "2 − x + 3x³ ↔ [2, −1, 0, 3]")

    exercise(doc, 2, "Producto circular", "Calcula el producto y usa la regla de la cuarta potencia:")
    add_formula(doc, "(1 + x)(1 + x³)")
    solution(doc, "La cuarta potencia vuelve a la posición constante.")
    add_formula(doc, "1 + x + x³ + x⁴ ≡ 2 + x + x³")

    exercise(
        doc,
        3,
        "Cifrado sencillo",
        "Usa la misma clave pública, pero toma como aleatoriedad uno y como mensaje x.",
    )
    add_formula(doc, "h = 3 + 3x,   r = 1,   m = x")
    solution(doc, "Se multiplica h por uno y después se suma el mensaje.")
    add_formula(doc, "c = 1·(3 + 3x) + x = 3 + 4x")
    add_formula(doc, "c mod 3 = x = m")

    exercise(
        doc,
        4,
        "Conceptos",
        "Indica cuáles son públicos entre f, h, r, m y c. ¿Qué valor debe mantenerse privado?",
    )
    solution(
        doc,
        "h y c pueden ser públicos. En este esquema f es la clave privada. El mensaje m normalmente debe "
        "permanecer confidencial y r no debe reutilizarse ni ser predecible.",
    )

    section(doc, "6. Python: comprobación del ejemplo")
    paragraphs(
        doc,
        "La función siguiente multiplica listas como polinomios circulares. El assert final comprueba que "
        "el mensaje se recupera.",
    )
    add_code(
        doc,
        r'''
N = 4


def multiply(a: list[int], b: list[int], modulus: int) -> list[int]:
    return [
        sum(a[i] * b[(k - i) % N] for i in range(N)) % modulus
        for k in range(N)
    ]


p, q = 3, 17
h = [3, 3, 0, 0]
r = [0, 1, 0, 0]
message = [1, 0, -1, 0]

mixed = multiply(r, h, q)
ciphertext = [(a + b) % q for a, b in zip(mixed, message)]
recovered = [value % p for value in ciphertext]

assert ciphertext == [1, 3, 2, 0]
assert recovered == [1, 0, 2, 0]  # 2 equivale a -1 módulo 3
''',
    )
    exercise(
        doc,
        5,
        "Python",
        "Sustituye r por [1, 0, 0, 0] y message por [0, 1, 0, 0]. Comprueba que el resultado coincide "
        "con el ejercicio 3.",
    )

    section(doc, "7. Cómo se usaría realmente")
    paragraphs(
        doc,
        "NTRU real se usa mediante una implementación revisada, normalmente como KEM. El programa recibe "
        "una clave pública, produce un paquete y obtiene un secreto compartido. Después el proyecto sigue "
        "el mismo patrón que con ML-KEM: derivar una clave y cifrar los datos con AES-GCM.",
        "NTRU es importante histórica y didácticamente, pero no es el KEM principal estandarizado por "
        "NIST. Para una migración normativa general, el punto de partida actual es ML-KEM.",
    )
    add_formula(doc, "NTRU-KEM → secreto compartido → KDF → AES-GCM")

    section(doc, "8. Resumen")
    bullets(
        doc,
        "NTRU representa datos y claves mediante polinomios pequeños.",
        "Los polinomios pueden verse como listas de coeficientes.",
        "La aleatoriedad hace que el cifrado no sea siempre igual.",
        "El ejemplo de clase explica el mecanismo, pero no es seguro para producción.",
    )
    return doc


def build_session_6_simple():
    doc = start_document(
        "Sesión 6. Métodos de criptografía post-cuántica (III). Estado actual. Versión simplificada",
        "Firmas ML-DSA y SLH-DSA con ejemplos pequeños y una guía básica de migración.",
    )

    section(doc, "1. Qué aprenderemos")
    bullets(
        doc,
        "Diferenciar una firma digital de un cifrado.",
        "Comprender una verificación simplificada de ML-DSA.",
        "Entender cómo un árbol de hashes ayuda a verificar SLH-DSA.",
        "Conocer qué algoritmos post-cuánticos están ya estandarizados.",
    )
    add_table(
        doc,
        ["Minutos", "Actividad"],
        [
            ["0-5", "Firma frente a cifrado y KEM."],
            ["5-15", "ML-DSA: explicación y ejemplo."],
            ["15-22", "SLH-DSA: explicación y ejemplo."],
            ["22-26", "Python."],
            ["26-30", "Estado actual y migración."],
        ],
    )

    section(doc, "2. Qué aporta una firma digital")
    paragraphs(
        doc,
        "Una firma digital no oculta un documento. Sirve para comprobar quién lo firmó y si se ha "
        "modificado. El firmante usa su clave privada y los demás verifican con la clave pública.",
    )
    add_formula(doc, "firma = Sign(clave_privada, mensaje)")
    add_formula(doc, "Verify(clave_pública, mensaje, firma) → válida o inválida")
    add_table(
        doc,
        ["Herramienta", "Pregunta que responde"],
        [
            ["KEM", "¿Cómo obtenemos la misma clave de sesión?"],
            ["Cifrado", "¿Cómo ocultamos el contenido?"],
            ["Firma", "¿Quién creó el contenido y ha sido modificado?"],
        ],
    )

    section(doc, "3. Método 1: ML-DSA")
    paragraphs(
        doc,
        "ML-DSA, antes conocido como Dilithium, es una firma basada en retículos. El firmante crea una "
        "respuesta que depende del mensaje, de un valor temporal y de su secreto. El verificador combina "
        "la respuesta con la clave pública para reconstruir un resultado esperado.",
        "El sistema real trabaja con vectores y polinomios. Usaremos una sola ecuación con números pequeños "
        "para ver la idea sin entrar en esas estructuras.",
    )
    add_formula(doc, "clave pública:   t = A·s   (mod q)")
    add_formula(doc, "respuesta:   z = y + c·s")
    add_formula(doc, "verificación:   A·z − c·t ?= A·y   (mod q)")

    section(doc, "4. Ejemplo guiado de ML-DSA")
    add_formula(doc, "q = 17,   A = 4,   secreto s = 3")
    add_formula(doc, "t = 4·3 = 12   (mod 17)")
    paragraphs(doc, "El firmante elige un valor temporal y calcula el valor que compromete:")
    add_formula(doc, "y = 2,   w = A·y = 4·2 = 8")
    paragraphs(doc, "El hash del mensaje produce, en este ejemplo inventado, el reto dos:")
    add_formula(doc, "c = H(m, w) = 2")
    add_formula(doc, "z = y + c·s = 2 + 2·3 = 8")
    paragraphs(doc, "El verificador usa únicamente valores públicos y la firma:")
    add_formula(doc, "A·z − c·t = 4·8 − 2·12 = 32 − 24 = 8 = w")
    paragraphs(
        doc,
        "La igualdad muestra la idea de la verificación. ML-DSA real añade ruido, hashes, límites y "
        "repeticiones para evitar que las firmas revelen la clave privada.",
    )

    section(doc, "5. Ejercicios de ML-DSA")
    exercise(
        doc,
        1,
        "Mensaje modificado",
        "Supón que el nuevo mensaje produce el reto tres. Comprueba la misma respuesta z.",
    )
    add_formula(doc, "A = 4,   z = 8,   c = 3,   t = 12,   q = 17")
    solution(doc, "El resultado ya no coincide con w, por lo que la firma falla.")
    add_formula(doc, "4·8 − 3·12 = −4 ≡ 13   (mod 17),   13 ≠ 8")

    exercise(
        doc,
        2,
        "Uso",
        "¿Usarías una firma para ocultar una factura o para demostrar que no se ha modificado?",
    )
    solution(
        doc,
        "La firma demuestra origen e integridad. Para ocultar la factura se necesita además cifrado.",
    )

    section(doc, "6. Método 2: SLH-DSA")
    paragraphs(
        doc,
        "SLH-DSA, antes conocido como SPHINCS+, construye firmas a partir de funciones hash. Muchas claves "
        "pequeñas se organizan en árboles. La raíz del árbol se publica y un camino de nodos permite "
        "demostrar que una hoja pertenece al árbol sin enviarlo completo.",
        "Su base matemática es diferente de ML-DSA. Esta diversidad es útil como alternativa, aunque las "
        "firmas de SLH-DSA suelen ocupar más espacio.",
    )
    add_formula(doc, "nodo_padre = H(nodo_izquierdo ∥ nodo_derecho)")

    section(doc, "7. Ejemplo guiado de árbol")
    paragraphs(
        doc,
        "Usamos una suma como hash de juguete. No sería segura, pero permite practicar la estructura del árbol.",
    )
    add_formula(doc, "H(a ∥ b) = (a + b) mod 17")
    add_formula(doc, "hojas = [3, 5, 8, 2]")
    add_formula(doc, "nodo₀ = H(3 ∥ 5) = 8")
    add_formula(doc, "nodo₁ = H(8 ∥ 2) = 10")
    add_formula(doc, "raíz = H(8 ∥ 10) = 18 mod 17 = 1")
    paragraphs(
        doc,
        "Para comprobar la hoja cinco basta conocer su hermana, que vale tres, y el nodo de la otra rama, "
        "que vale diez. Con esos dos valores el verificador reconstruye la raíz pública uno.",
    )

    section(doc, "8. Ejercicios de SLH-DSA")
    exercise(
        doc,
        3,
        "Hoja modificada",
        "Cambia la tercera hoja de ocho a nueve y calcula la nueva raíz.",
    )
    solution(doc, "Cambian el nodo derecho y la raíz. La prueba ya no coincide con la clave pública.")
    add_formula(doc, "nodo₁′ = H(9 ∥ 2) = 11,   raíz′ = H(8 ∥ 11) = 2")
    add_formula(doc, "raíz′ = 2 ≠ 1 = raíz_pública")

    exercise(
        doc,
        4,
        "Comparación",
        "¿Qué método ofrece una base matemática diferente de los retículos: ML-DSA o SLH-DSA?",
    )
    solution(doc, "SLH-DSA, porque su construcción se basa principalmente en funciones hash.")

    section(doc, "9. Python: firmar un mensaje")
    paragraphs(
        doc,
        "La misma función puede probar los dos algoritmos. Solo se ejecutará un algoritmo si está "
        "habilitado en la instalación local de liboqs.",
    )
    add_code(
        doc,
        r'''
import oqs


message = b"invoice_id=7;amount=199.00;currency=EUR"
algorithms = ["ML-DSA-65", "SLH-DSA-SHA2-128s"]
enabled = set(oqs.get_enabled_sig_mechanisms())

for algorithm in algorithms:
    if algorithm not in enabled:
        continue

    with oqs.Signature(algorithm) as signer:
        public_key = signer.generate_keypair()
        signature = signer.sign(message)

    with oqs.Signature(algorithm) as verifier:
        assert verifier.verify(message, signature, public_key)
        assert not verifier.verify(message + b"!", signature, public_key)

    print(algorithm, "firma válida", len(signature), "bytes")
''',
    )
    exercise(
        doc,
        5,
        "Python",
        "Cambia el importe antes de verificar. Explica por qué la firma original deja de ser válida y "
        "compara el tamaño de las firmas disponibles.",
    )

    section(doc, "10. Estado actual, explicado de forma breve")
    add_table(
        doc,
        ["Algoritmo", "Para qué sirve", "Estado a septiembre de 2026"],
        [
            ["ML-KEM", "Establecer claves", "Estándar final FIPS 203"],
            ["ML-DSA", "Firmar", "Estándar final FIPS 204"],
            ["SLH-DSA", "Firmar", "Estándar final FIPS 205"],
            ["FN-DSA", "Firmar", "Estándar FIPS 206 en desarrollo"],
            ["HQC-KEM", "Establecer claves", "Seleccionado; FIPS 207 en desarrollo"],
        ],
    )
    paragraphs(
        doc,
        "Los tres primeros ya tienen estándares finales y son el punto de partida para aprender y probar "
        "migraciones. Esto no significa reemplazar mañana todo el software sin análisis. Primero hay que "
        "saber dónde se usa criptografía, qué datos necesitan protección duradera y qué bibliotecas ofrecen "
        "implementaciones adecuadas.",
    )

    section(doc, "11. Ejercicio final de proyecto")
    exercise(
        doc,
        6,
        "Elegir la herramienta",
        "Asigna una herramienta a cada necesidad: establecer una clave de sesión, ocultar datos y firmar "
        "una actualización de software.",
    )
    solution(
        doc,
        "ML-KEM establece la clave, AES-GCM oculta y autentica los datos, y ML-DSA o SLH-DSA firma la actualización.",
    )
    add_formula(doc, "ML-KEM → clave de sesión")
    add_formula(doc, "AES-GCM → datos cifrados")
    add_formula(doc, "ML-DSA o SLH-DSA → actualización firmada")

    section(doc, "12. Resumen")
    bullets(
        doc,
        "Una firma demuestra origen e integridad; no oculta el mensaje.",
        "ML-DSA está basado en retículos.",
        "SLH-DSA está basado principalmente en funciones hash.",
        "ML-KEM, ML-DSA y SLH-DSA ya cuentan con estándares finales de NIST.",
        "La migración comienza con inventario, pruebas y capacidad para cambiar algoritmos.",
    )
    return doc


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    documents = [
        ("sesion_4_version_simple.docx", build_session_4_simple()),
        ("sesion_5_version_simple.docx", build_session_5_simple()),
        ("sesion_6_version_simple.docx", build_session_6_simple()),
    ]
    for filename, document in documents:
        destination = OUT_DIR / filename
        document.save(destination)
        print(f"Generated: {destination}")


if __name__ == "__main__":
    main()
