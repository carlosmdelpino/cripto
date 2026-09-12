2. Cambios prioritarios

2.1. Añadir el modelo de amenaza

Antes de estudiar algoritmos, introducir:

Alice, Bob y Eve.

Canal inseguro.

Atacante pasivo: escucha.

Atacante activo: modifica, inyecta, elimina o repite mensajes.

Ataques de intermediario (MITM).

Objetivos del atacante.

Modelo de capacidades del atacante.

Seguridad computacional frente a seguridad absoluta.

Ejemplo que falta: MITM

Alice quiere comunicarse con Bob.

Alice  <------>  Eve  <------>  Bob

Alice cree hablar con Bob y Bob cree hablar con Alice, pero Eve controla el canal.

Esto permite explicar por qué cifrar no basta: también hay que autenticar las claves o las identidades.

3. Mejorar la sección de objetivos de seguridad

Actualmente aparecen confidencialidad, integridad, autenticación y no repudio. fileciteturn0file0L29-L55

Conviene separar conceptos que a menudo se mezclan:

Objetivo

Pregunta

Confidencialidad

¿Quién puede leer el mensaje?

Integridad

¿Ha sido modificado?

Autenticación de entidad

¿Con quién estoy hablando?

Autenticación de mensaje

¿Quién generó este mensaje?

No repudio

¿Puede atribuirse una firma de forma jurídicamente/técnicamente verificable?

Importante

No presentar el no repudio como una propiedad puramente criptográfica. Una firma digital proporciona mecanismos técnicos de autenticidad e integridad, pero el no repudio depende también del protocolo, gestión de claves, contexto legal y evidencias disponibles.

También añadir:

disponibilidad como objetivo general de seguridad, aunque no sea una propiedad proporcionada directamente por la criptografía;

control de acceso, que tampoco debe confundirse con criptografía.

4. Corregir y ampliar la definición de criptografía

La definición actual está demasiado centrada en «hacer incomprensible» la información. fileciteturn0file0L57-L75

Una definición moderna debería dejar claro que la criptografía no consiste solamente en ocultar información.

Añadir

La criptografía estudia técnicas matemáticas y protocolos destinados a proporcionar propiedades de seguridad como confidencialidad, integridad, autenticación y autenticidad, incluso cuando los sistemas se comunican a través de canales controlados por un atacante.

Esto permite introducir posteriormente:

cifrado;

MAC;

hash;

firmas digitales;

intercambio de claves;

protocolos criptográficos.

5. Añadir una sección fundamental: primitivas criptográficas

Esta sección debería aparecer antes de hablar de «criptografía híbrida».

Primitivas

5.1. Cifrado

Transforma:

M + K -> C

y permite recuperar el mensaje con la clave correspondiente.

5.2. Funciones hash

M -> H(M)

Sirven para construir mecanismos de integridad y otras primitivas.

5.3. MAC

Este concepto falta y es muy importante.

Un MAC permite comprobar:

integridad;

autenticidad de un mensaje para alguien que comparte la clave.

Ejemplo conceptual:

M + K -> MAC

El receptor calcula el MAC sobre el mensaje recibido y comprueba si coincide.

Ejemplos modernos:

HMAC-SHA-256;

CMAC;

Poly1305.

5.4. Firmas digitales

Permiten verificar que un mensaje fue firmado con la clave privada correspondiente y que no ha sido modificado.

5.5. Intercambio/acuerdo de claves

Introducir Diffie-Hellman como una primitiva/protocolo para establecer un secreto compartido sin transmitir directamente ese secreto.

6. Añadir una distinción crucial: hash ≠ cifrado

El temario afirma correctamente que un hash no debe permitir recuperar el original, pero conviene reforzar la diferencia. fileciteturn0file0L206-L230

Añadir una tabla:

Mecanismo

¿Se puede recuperar el mensaje?

¿Usa clave?

Uso principal

Cifrado

Sí

Sí

Confidencialidad

Hash

No

No

Integridad / construcción de primitivas

MAC

No

Sí

Integridad + autenticidad

Firma

No

Sí, par pública/privada

Autenticidad + integridad

Ejemplo práctico

"Hola" -> SHA-256 -> digest

No significa que el digest sea una versión cifrada de "Hola".

7. Corregir la explicación de firmas digitales

Actualmente se dice que el emisor «cifra el hash con su clave privada». fileciteturn0file0L196-L200

Esta explicación es útil como primera intuición histórica, pero es técnicamente demasiado simplificada.

Mejor explicar:

Una firma digital es una operación criptográfica que se calcula sobre un mensaje (normalmente utilizando un hash) con la clave privada. La verificación se realiza con la clave pública correspondiente.

Después aclarar:

RSA-PSS;

Ed25519;

ECDSA.

Evitar enseñar que una firma digital es simplemente «cifrar con la privada», porque ese modelo mental genera errores posteriormente.

8. Mejorar la sección de criptografía simétrica

La sección explica bien la idea básica, pero falta una distinción esencial: cifrado por bloques, modos de operación y cifrado autenticado. fileciteturn0file0L107-L130

Añadir

AES

Explicar que AES es un cifrado por bloques, no un sistema completo para cifrar arbitrariamente un flujo de datos.

Después introducir:

ECB;

CBC;

CTR;

GCM.

Muy importante: ECB

Mostrar visualmente por qué ECB es problemático: bloques iguales producen bloques cifrados iguales.

No es necesario implementar el ataque; basta con mostrar el concepto.

Cifrado autenticado (AEAD)

Este debería ser uno de los conceptos centrales del curso.

Ejemplo:

AES-GCM

Proporciona:

confidencialidad;

integridad;

autenticidad del ciphertext.

También mencionar:

ChaCha20-Poly1305.

Idea conceptual:

clave + nonce + mensaje
        |
       AEAD
        |
 ciphertext + tag

El nonce debe tratarse con especial cuidado y no reutilizarse con la misma clave en esquemas como GCM.

9. Añadir nonce, IV y aleatoriedad

Este tema falta y es fundamental para entender criptografía práctica.

Explicar:

clave;

nonce;

IV;

salt;

random/secure random.

No son intercambiables.

Ejemplo

Dos veces:

AES-GCM(K, nonce, "Hola")

no deberían utilizar el mismo nonce bajo la misma clave.

La idea importante para el alumno:

Una implementación criptográfica segura depende tanto del algoritmo como de cómo se generan y gestionan claves, nonces y demás parámetros.

Esto conecta directamente con la afirmación del temario de que un algoritmo robusto puede resultar inseguro por una mala gestión de claves. fileciteturn0file0L73-L76

10. Ampliar la criptografía asimétrica

La explicación de clave pública/privada es correcta como introducción. fileciteturn0file0L132-L156

Pero conviene introducir una separación:

Cifrado de clave pública

mensaje -> clave pública del receptor
mensaje recuperado -> clave privada

Firma

mensaje -> clave privada del emisor
verificación -> clave pública

Acuerdo de claves

Alice + Bob -> secreto compartido

Esto evita que el alumno piense que RSA/ECC tienen una única operación de «cifrar/descifrar».

11. Añadir Diffie-Hellman

Es probablemente la ausencia más importante del temario actual.

Ejemplo conceptual

Alice y Bob acuerdan públicamente:

p, g

Alice escoge a y calcula:

A = g^a mod p

Bob escoge b:

B = g^b mod p

Intercambian A y B.

Alice calcula:

K = B^a mod p

Bob calcula:

K = A^b mod p

Ambos obtienen:

K = g^(ab) mod p

Eve conoce p, g, A y B, pero no conoce directamente a ni b.

Después

Explicar que Diffie-Hellman por sí solo no autentica a Alice ni a Bob, por lo que sigue siendo vulnerable a MITM.

Esta combinación:

Diffie-Hellman + autenticación

es una excelente forma de introducir protocolos reales.

12. Replantear RSA

La sección actual contiene las ecuaciones esenciales de RSA. fileciteturn0file0L276-L291

Para una introducción, añadir primero un ejemplo pequeño y totalmente calculado.

Ejemplo didáctico

Elegir:

p = 5
q = 11

n = p × q = 55

φ(n) = (5-1)(11-1) = 40

Elegir:

e = 3

Buscar d tal que:

e × d ≡ 1 (mod 40)

Por ejemplo:

3 × 27 = 81 ≡ 1 (mod 40)

Por tanto:

clave pública = (55, 3)
clave privada = 27

Usar después un mensaje pequeño para demostrar:

c = m^e mod n
m = c^d mod n

Advertencia importante

Dejar claro que este RSA es solo educativo.

No se debe implementar RSA «a mano» para uso real. En sistemas reales se utilizan esquemas de padding seguros, por ejemplo:

RSA-OAEP para cifrado;

RSA-PSS para firmas.

13. Mejorar la parte de ECC

El temario introduce correctamente la idea:

Q = kG

y el problema del logaritmo discreto en curvas elípticas. fileciteturn0file0L293-L305

Para una introducción no hace falta desarrollar toda la teoría de curvas, pero sí conviene explicar:

qué significa un campo finito;

qué es un punto de una curva;

suma de puntos;

multiplicación escalar;

problema del logaritmo discreto;

diferencia entre ECDH y ECDSA;

Ed25519 como alternativa moderna basada en curvas.

También conviene evitar presentar «ECC» como un único algoritmo. Es una familia de técnicas.

14. Mejorar considerablemente la parte matemática

La sección matemática actual es demasiado corta para sostener RSA, Diffie-Hellman y ECC. Incluye modularidad, primos y logaritmo discreto, pero faltan varias herramientas. fileciteturn0file0L232-L259

Módulo matemático recomendado

Nivel 1 — imprescindible

Aritmética modular

a ≡ b (mod n)

Operaciones:

(a+b) mod n
(a-b) mod n
(a×b) mod n

Ejemplos:

23 mod 7 = 2

17 ≡ 2 (mod 5)

Ya presentes en el temario. fileciteturn0file0L239-L247

Potenciación modular

a^b mod n

Introducir exponenciación rápida (square-and-multiply).

Esto es muy importante porque aparece constantemente en criptografía.

Nivel 2 — teoría de números

Añadir:

divisibilidad;

números primos;

factorización;

máximo común divisor;

algoritmo de Euclides;

algoritmo de Euclides extendido;

inverso modular;

función φ de Euler;

teorema de Euler;

pequeño teorema de Fermat.

Ejemplo de inverso modular

Buscar:

7^-1 mod 26

Como:

7 × 15 = 105 ≡ 1 mod 26

entonces:

7^-1 ≡ 15 mod 26

Esto prepara directamente al alumno para RSA.

Nivel 3 — grupos

Introducir de forma intuitiva:

conjunto;

operación;

grupo;

grupo abeliano;

elemento identidad;

inverso;

orden de un elemento;

grupo cíclico;

generador.

No hace falta convertir el curso en álgebra abstracta, pero sí dar suficiente base para entender Diffie-Hellman y ECC.

Nivel 4 — campos finitos

Introducir:

Z_n;

Z_p;

campos finitos;

operaciones en campos;

idea de GF(p).

Para ECC, esto es especialmente útil.

Nivel 5 — complejidad

Añadir una introducción breve a:

tiempo polinómico;

fuerza bruta;

exponencial;

problemas computacionalmente difíciles;

seguridad de n bits;

complejidad de ataques.

Esto permite explicar por qué:

"difícil matemáticamente"

no significa:

"imposible"

sino normalmente:

"computacionalmente inviable con los recursos considerados"

15. Añadir teoría de probabilidades y aleatoriedad

No hace falta un bloque matemático enorme, pero sí:

probabilidad básica;

distribución uniforme;

entropía;

entropía de una contraseña;

generación de números aleatorios criptográficamente seguros.

Ejemplo

Comparar:

random()

con un generador criptográficamente seguro.

La idea importante es:

En criptografía, «parece aleatorio» no es suficiente.

16. Añadir contraseñas y derivación de claves

Actualmente aparecen buenas prácticas de contraseñas, pero no se explica cómo se almacenan correctamente. fileciteturn0file0L394-L409

Añadir:

password hashing;

salt;

KDF;

PBKDF2;

scrypt;

Argon2id.

Ejemplo

No:

password -> SHA-256 -> guardar

Sí:

password + salt
       |
      KDF
       |
 password hash

Explicar por qué un hash rápido como SHA-256 no está diseñado para almacenar contraseñas.

17. Añadir ataques clásicos y modernos

El temario necesita una sección de «cómo se rompe un sistema».

Introducir:

fuerza bruta;

diccionario;

análisis de frecuencia;

replay attack;

MITM;

nonce reuse;

mala generación aleatoria;

filtración de claves;

side channels, solo como introducción;

errores de implementación.

Ejemplo especialmente didáctico: reutilización de clave/nonce

Mostrar que incluso un algoritmo fuerte puede fallar cuando se utiliza incorrectamente.

18. Añadir criptografía clásica como introducción histórica

Antes de AES/RSA puede ser útil incluir muy brevemente:

cifrado César;

sustitución;

transposición;

Vigenère.

Pero con una advertencia explícita:

Estos algoritmos son históricos y no deben utilizarse para proteger información real.

Ejercicio

Romper un César mediante fuerza bruta y analizar frecuencias.

Esto proporciona una transición excelente desde criptografía clásica hacia criptografía moderna.

19. Añadir protocolos reales

El temario termina demasiado cerca de los algoritmos.

El alumno debería ver cómo se combinan:

hash
MAC
AEAD
DH
firmas
certificados

en protocolos reales.

Caso principal: HTTPS/TLS

Explicar de forma simplificada:

Cliente
   |
   | ClientHello
   v
Servidor
   |
   | certificado
   | negociación
   | acuerdo de claves
   v
Secreto compartido
   |
   v
Cifrado autenticado

No hace falta enseñar el protocolo completo, pero sí responder:

¿Cómo puede mi navegador saber que realmente está hablando con el servidor correcto?

Esto conduce naturalmente a certificados y PKI.

20. Añadir certificados y PKI

Falta por completo.

Introducir:

certificado digital;

autoridad certificadora (CA);

clave pública;

identidad;

cadena de confianza;

certificado raíz;

expiración;

revocación, a nivel conceptual.

Ejemplo

Cuando visitas:

https://ejemplo.com

el navegador no confía simplemente porque el servidor diga:

«Esta es mi clave pública».

Necesita una cadena de confianza.

21. Añadir un laboratorio práctico con Python

La sección Python actual es útil, pero demasiado pequeña: solo calcula SHA-256 y 23 % 7. fileciteturn0file0L357-L376

Propondría convertirla en un pequeño laboratorio progresivo.

Laboratorio 1 — Modularidad

print(23 % 7)
print(pow(3, 4, 5))

Laboratorio 2 — Hash

import hashlib

mensaje = b"Hola, mundo seguro"
print(hashlib.sha256(mensaje).hexdigest())

Modificar un carácter y comparar los hashes.

Laboratorio 3 — Inverso modular

print(pow(7, -1, 26))

Laboratorio 4 — HMAC

Usar hmac y hashlib.

Objetivo:

mensaje + clave -> MAC

Modificar el mensaje y comprobar que la verificación falla.

Laboratorio 5 — AEAD

Usar una biblioteca criptográfica para experimentar con AES-GCM o ChaCha20-Poly1305.

Demostrar qué ocurre al modificar el ciphertext.

Laboratorio 6 — RSA educativo

Implementar únicamente las operaciones matemáticas con números pequeños.

Después comparar con una biblioteca real.

Laboratorio 7 — MITM conceptual

Construir una simulación sencilla de Diffie-Hellman sin autenticación para demostrar por qué el protocolo necesita autenticación.

22. Añadir una sección «Nunca hagas esto»

Muy recomendable para un curso introductorio.

No utilizar

DES;

3DES en nuevos diseños;

MD5;

SHA-1 para seguridad criptográfica;

ECB para cifrado general;

RSA «casero» sin padding;

contraseñas almacenadas directamente;

claves derivadas de contraseñas sin KDF;

PRNG no criptográfico para generar claves;

reutilización incorrecta de nonces.

Regla de oro

No diseñes tu propio algoritmo criptográfico.

Y añadir:

En aplicaciones reales, utiliza primitivas y protocolos bien revisados mediante bibliotecas criptográficas mantenidas.

23. Reordenación recomendada del curso

Propongo este orden:

Módulo 1 — Introducción

¿Qué es la criptografía?

Objetivos de seguridad.

Modelo de amenaza.

Alice, Bob y Eve.

Ataques pasivos y activos.

Módulo 2 — Matemáticas

Divisibilidad.

Primos.

MCD.

Euclides.

Aritmética modular.

Inverso modular.

Exponenciación modular.

Fermat y Euler.

Grupos y grupos cíclicos.

Logaritmo discreto.

Introducción a campos finitos.

Módulo 3 — Criptografía simétrica

Cifrados por bloques.

AES.

Modos de operación.

Nonces e IV.

Cifrado autenticado.

AES-GCM.

ChaCha20-Poly1305.

Módulo 4 — Hashes y autenticación

Funciones hash.

Preimagen.

Segunda preimagen.

Colisiones.

SHA-2/SHA-3.

HMAC.

Password hashing.

Salt y KDF.

Módulo 5 — Criptografía asimétrica

Clave pública/privada.

RSA.

OAEP.

RSA-PSS.

Diffie-Hellman.

ECDH.

ECC.

ECDSA/Ed25519.

Módulo 6 — Firmas y PKI

Firmas digitales.

Certificados.

CA.

Cadena de confianza.

PKI.

Módulo 7 — Protocolos

MITM.

Replay.

TLS/HTTPS.

Criptografía híbrida.

Gestión de claves.

Módulo 8 — Práctica

Python.

Hash.

HMAC.

AES-GCM.

RSA.

Diffie-Hellman.

Firma digital.

Simulación de ataques.

24. Cambios concretos en ejemplos

El temario actual ya tiene tres ejemplos de envío seguro, integridad y firma. fileciteturn0file0L307-L327

Añadiría estos:

Ejemplo A — ¿Por qué no basta con cifrar?

Alice cifra:

mensaje -> cifrado -> Bob

Eve no puede leerlo, pero puede modificarlo.

Conclusión:

confidencialidad ≠ integridad

Ejemplo B — MAC

Alice -- mensaje + MAC --> Bob

Eve modifica el mensaje.

Bob recalcula el MAC:

MAC recibido != MAC calculado

El mensaje se rechaza.

Ejemplo C — MITM

Mostrar que Diffie-Hellman sin autenticación no evita que Eve establezca dos secretos distintos:

Alice <-> Eve
Eve   <-> Bob

Ejemplo D — contraseña

Comparar:

SHA-256(password)

frente a:

Argon2id(password, salt)

Ejemplo E — nonce

Mostrar conceptualmente por qué reutilizar un nonce con la misma clave puede destruir la seguridad de ciertos esquemas AEAD.

25. Ejercicios nuevos

Matemáticas

Calcular 37 mod 9.

Calcular 7^20 mod 13.

Encontrar x tal que 7x ≡ 1 mod 26.

Aplicar Euclides a 252 y 105.

Encontrar un inverso modular usando Euclides extendido.

Calcular φ(55).

Verificar el pequeño teorema de Fermat con números pequeños.

Resolver un ejemplo pequeño de Diffie-Hellman.

Criptografía

Explicar por qué un hash no proporciona confidencialidad.

Explicar por qué un MAC necesita una clave.

Diferenciar MAC y firma digital.

Explicar por qué ECB es inseguro para muchos usos.

Explicar qué problema resuelve Diffie-Hellman.

Explicar por qué Diffie-Hellman necesita autenticación.

Explicar qué papel desempeña una CA.

Identificar vulnerabilidades en un protocolo deliberadamente mal diseñado.

26. Qué sintetizar del documento actual

Hay varias secciones que se pueden fusionar porque repiten conceptos.

Fusionar

«Criptografía simétrica» + parte de «Criptografía híbrida»

La explicación de que la simétrica es rápida y la asimétrica sirve para intercambio de claves aparece repetida varias veces. fileciteturn0file0L78-L105 fileciteturn0file0L158-L176

Reducirlo a:

Simétrica -> datos
Asimétrica -> claves/autenticación
Híbrida -> combinación

y después dedicar el tiempo ganado a AEAD y gestión de claves.

«Conceptos básicos» + «Funciones hash»

Se pueden convertir en una introducción general a primitivas criptográficas y después desarrollar hash, MAC y firma por separado.

«Ejemplos prácticos» + «Importancia de la seguridad digital»

La parte de importancia puede reducirse considerablemente y utilizar el espacio para casos prácticos.

27. Correcciones conceptuales importantes

27.1. «Mayor longitud de clave = mayor seguridad»

La afirmación actual es cierta solo de forma aproximada. fileciteturn0file0L128-L130

Mejor:

La seguridad depende de la combinación entre algoritmo, tamaño de clave, implementación, protocolo, generación y gestión de claves y modelo de amenaza.

Una clave enorme no arregla un algoritmo defectuoso.

27.2. Hash «unidireccional»

Evitar presentar «unidireccional» como una propiedad absoluta.

Mejor hablar de:

resistencia a preimagen;

resistencia a segunda preimagen;

resistencia a colisiones.

27.3. Integridad mediante hash

Un hash publicado junto con un archivo no garantiza por sí mismo que el archivo no haya sido manipulado.

Un atacante podría modificar tanto:

archivo
hash

Por eso, para autenticidad/integridad frente a un atacante activo, se necesitan mecanismos como:

MAC;

firma digital;

canal autenticado.

Este es un punto didáctico muy importante.

28. Proyecto final recomendado

Para cerrar el curso, propondría un proyecto:

«Construir una mini-comunicación segura»

El alumno debe implementar, utilizando bibliotecas estándar:

1. Generación de claves
2. Acuerdo de clave
3. Cifrado AEAD
4. Autenticación
5. Integridad
6. Verificación de mensajes

Y explicar:

¿Qué protege cada mecanismo?
¿Qué ocurriría si eliminamos cada componente?

No se debe pedir al alumno que diseñe una criptografía nueva.

29. Estructura pedagógica final

La idea central que debería atravesar todo el curso es:

PROBLEMA
   ↓
¿Qué puede hacer el atacante?
   ↓
OBJETIVO
   ↓
¿Qué propiedad necesitamos?
   ↓
PRIMITIVA
   ↓
¿Cómo la implementamos correctamente?
   ↓
PROTOCOLO
   ↓
¿Qué puede salir mal?

Por ejemplo:

Quiero enviar un archivo secreto
        ↓
Necesito confidencialidad
        ↓
Cifrado
        ↓
AES-GCM
        ↓
Clave + nonce gestionados correctamente
        ↓
¿Cómo obtiene Bob la clave?
        ↓
Acuerdo de claves / criptografía híbrida
        ↓
¿Cómo sé que Bob es realmente Bob?
        ↓
Autenticación / certificados

Este enfoque hará que el curso sea mucho más sólido que una simple sucesión de algoritmos.

30. Prioridad de incorporación

Si el tiempo es limitado, priorizar en este orden:

Imprescindible

Modelo de amenazas.

Hash vs cifrado.

MAC.

AEAD.

Nonces/IV.

Diffie-Hellman.

MITM.

Inverso modular y Euclides extendido.

Exponenciación modular.

Contraseñas + salt + KDF.

Firmas correctamente explicadas.

Certificados/PKI.

TLS como caso integrador.

Segundo nivel

Grupos.

Campos finitos.

ECDH.

Ed25519.

Ataques de replay.

Side channels.

Criptografía post-cuántica, como introducción final.

Prescindible en una primera edición

Desarrollo profundo de DES.

Desarrollo matemático completo de ECC.

Implementación manual de RSA real.

Demostraciones formales largas.

Historia extensa de la criptografía.

Conclusión

El temario actual es una buena introducción conceptual, pero está más cerca de una introducción general a «qué es la criptografía» que de una introducción completa a la criptografía moderna aplicada. Ya cubre una base útil de objetivos de seguridad, simétrica/asimétrica, hashes, RSA/ECC, modularidad y ejemplos. fileciteturn0file0L1-L25

Los mayores saltos de calidad serían añadir modelo de amenazas → MAC → AEAD → nonces → Diffie-Hellman → autenticación/PKI → TLS, y reforzar las matemáticas con Euclides extendido, inversos modulares, exponenciación rápida, Euler/Fermat, grupos y campos finitos.

Con esos cambios, el curso dejaría de ser principalmente descriptivo y pasaría a enseñar al alumno cómo pensar criptográficamente, que es el objetivo más valioso de una asignatura de introducción.