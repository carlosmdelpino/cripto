# Sesión 1. Fundamentos de la criptografía

## Índice

- [1. Introducción](#1-introducción)
- [2. Objetivos de la sesión](#2-objetivos-de-la-sesión)
- [3. Objetivos de la seguridad de la información](#3-objetivos-de-la-seguridad-de-la-información)
- [4. ¿Qué es la criptografía?](#4-qué-es-la-criptografía)
- [5. Tipos de criptografía](#5-tipos-de-criptografía)
- [6. Conceptos básicos de la criptografía](#6-conceptos-básicos-de-la-criptografía)
- [7. Fundamentos matemáticos básicos](#7-fundamentos-matemáticos-básicos)
- [8. Métodos criptográficos modernos: RSA y ECC](#8-métodos-criptográficos-modernos-rsa-y-ecc)
- [9. Ejemplos prácticos](#9-ejemplos-prácticos)
- [10. Ejercicios propuestos con soluciones](#10-ejercicios-propuestos-con-soluciones)
- [11. Ejemplo sencillo de cálculo con Python](#11-ejemplo-sencillo-de-cálculo-con-python)
- [12. Importancia de la seguridad en la era digital](#12-importancia-de-la-seguridad-en-la-era-digital)
- [13. Errores habituales en la práctica](#13-errores-habituales-en-la-práctica)
- [14. Conclusiones](#14-conclusiones)
- [15. Bibliografía esencial](#15-bibliografía-esencial)
- [16. Bibliografía recomendada](#16-bibliografía-recomendada)
- [17. Preguntas de reflexión](#17-preguntas-de-reflexión)
- [18. Actividad recomendada para el aula](#18-actividad-recomendada-para-el-aula)

## 1. Introducción

La criptografía es la disciplina que se encarga de proteger la información para que pueda viajar, almacenarse o procesarse sin que terceros no autorizados puedan acceder a su contenido o alterarlo. El término proviene del griego *kryptós* (“oculto”) y *gráphein* (“escribir”), y su historia está estrechamente ligada al desarrollo de la seguridad de la información.

En la práctica, la criptografía aparece en casi todos los servicios digitales que utilizamos: navegación web segura, banca online, autenticación de usuarios, comunicaciones móviles, almacenamiento en la nube y firma de documentos electrónicos. Sin ella, gran parte del ecosistema digital no sería confiable.

**Fecha de referencia:** XX-YY-ZZZZ

---

## 2. Objetivos de la sesión

Al finalizar esta sesión, el estudiante será capaz de:

• comprender qué es la criptografía y por qué es esencial en la seguridad digital.
• identificar los objetivos básicos de la seguridad de la información.
• distinguir entre criptografía simétrica, asimétrica e híbrida.
• reconocer los conceptos de clave, función hash, firma digital y cifrado.
• aplicar razonamientos simples de seguridad a escenarios cotidianos.
• interpretar algunos fundamentos matemáticos que sustentan la criptografía moderna.

---

## 3. Objetivos de la seguridad de la información

La criptografía no solo sirve para ocultar mensajes; también proporciona una base para garantizar atributos esenciales del sistema. Los más importantes son los siguientes:

### 3.1 Confidencialidad

- La confidencialidad busca garantizar que la información solo pueda ser leída por las personas autorizadas.
- Si un atacante intercepta un canal de comunicación, no debería poder entender el contenido.

**Ejemplo**: un correo electrónico con contenido bancario debe llegar a su destinatario sin que un tercero pueda leer su contenido.

### 3.2 Integridad

- La integridad implica que los datos no hayan sido alterados ni manipulados durante la transmisión o almacenamiento.
- Esto permite detectar cambios no autorizados en archivos, mensajes o transacciones.

**Ejemplo**: si un archivo de configuración se modifica sin autorización, el sistema debe detectar que algo ha cambiado.

### 3.3 Autenticación

- La autenticación verifica la identidad de quien envía o recibe la información.
- Permite comprobar si la entidad que parece ser el emisor realmente lo es.

**Ejemplo**: acceder a una aplicación con usuario y contraseña, o verificar que un certificado digital corresponde a un servidor real.

### 3.4 No repudio

- El no repudio evita que una parte niegue haber enviado o recibido un mensaje.
- Es importante en procedimientos legales, transacciones y comunicaciones corporativas.

**Ejemplo**: un cliente no puede reclamar que nunca solicitó una transferencia si esa solicitud fue firmada digitalmente.

> En resumen, la seguridad de la información se apoya en cuatro pilares fundamentales: confidencialidad, integridad, autenticación y no repudio.

### 3.5 Objetivos complementarios

- La disponibilidad es un objetivo general de la seguridad, aunque no sea una propiedad proporcionada directamente por la criptografía.
- El control de acceso no debe confundirse con la criptografía, aunque ambos son pilares de la seguridad global del sistema.

---

## 4. ¿Qué es la criptografía?

La criptografía es el conjunto de técnicas y procedimientos que transforman la información para hacerla incomprensible para quien no conoce la clave o el procedimiento correcto de recuperación.

El modelo clásico de comunicación segura puede resumirse así:

• el emisor convierte el mensaje original en texto cifrado.
• el mensaje se transmite por un canal que puede ser inseguro.
• el receptor aplica la operación inversa con la clave apropiada.
• se recupera el contenido original.

### Esquema general

```text
Mensaje original  ->  Cifrado  ->  Canal de comunicación  ->  Descifrado  ->  Mensaje original
```

- En un sistema fiable, la seguridad depende no solo del algoritmo, sino también de la robustez de la clave y de la forma en que se gestiona.
- La criptografía moderna no consiste solamente en ocultar información, sino en garantizar propiedades de confianza en sistemas adversariales.

### 4.1 Criptografía y seguridad

La criptografía es una herramienta fundamental dentro del marco más amplio de la seguridad informática. No sustituye otros mecanismos, sino que los complementa. Por ejemplo:

• control de acceso.
• autenticación multifactor.
• firewalls.
• monitorización de red.
• educación del usuario.
• gestión de incidentes.

La criptografía actúa como capa de protección para los datos y las comunicaciones.

---

## 5. Tipos de criptografía

La criptografía se clasifica normalmente en tres grandes grupos: simétrica, asimétrica e híbrida.

### 5.1 Criptografía simétrica

• En la criptografía simétrica, el mismo secreto se usa tanto para cifrar como para descifrar.
• Es la opción más eficiente para proteger grandes volúmenes de datos.

**Ventajas:**
- es muy rápida;
- tiene un bajo coste computacional;
- suele ser apropiada para cifrar grandes cantidades de datos.

**Desventajas:**
- la clave debe compartirse antes del intercambio;
- la gestión de claves puede ser complicada;
- si la clave se compromete, todo el sistema queda expuesto.

**Ejemplos típicos**: AES, DES (obsoleto), Blowfish.

**Caso de uso habitual**: cifrado de archivos grandes o tráfico de datos a gran escala.

### 5.2 Criptografía asimétrica

• En la criptografía asimétrica se utiliza un par de claves:
  • una clave pública, que puede distribuirse libremente.
  • una clave privada, que debe mantenerse secreta.
• Esto permite resolver el problema de la distribución de claves que aparece en los sistemas simétricos.

**Ventajas:**
- no requiere compartir la clave privada;
- permite autenticación e intercambio seguro de claves;
- facilita la firma digital.

**Desventajas:**
- suele ser más lenta que la simétrica;
- la gestión de certificados y confianza puede ser más compleja.

**Ejemplos**: RSA, ECC, ElGamal.

**Caso de uso habitual**: firma digital, autenticación y establecimiento de claves seguras.

### 5.3 Criptografía híbrida

• La criptografía híbrida combina ambas opciones.
• Por ejemplo, se usa una clave simétrica para cifrar el contenido y una clave asimétrica para proteger la clave simétrica.

**Ejemplo práctico**: cuando dos interlocutores desean intercambiar un documento confidencial, primero acuerdan una clave simétrica de forma segura mediante un protocolo asimétrico y luego cifran el documento con esa clave.

> Esta es una de las soluciones más habituales en protocolos modernos como TLS/SSL.

### 5.4 Comparación rápida

| Tipo | Claves | Velocidad | Uso principal | Ventaja | Desventaja |
|---|---|---:|---|---|---|
| Simétrica | 1 secreta | Alta | Cifrado de contenido | Rápida | Distribución de claves |
| Asimétrica | 2 (pública y privada) | Media/baja | Intercambio de claves y firma | Sin compartir clave privada | Más lenta |
| Híbrida | Mixta | Alta | Protocolos seguros actuales | Equilibrio entre seguridad y rendimiento | Más compleja |

---

## 6. Conceptos básicos de la criptografía

### 6.1 Texto claro y texto cifrado

• **Texto claro**: información original y legible para un ser humano o para un sistema.
• **Texto cifrado**: resultado del proceso de cifrado, normalmente incomprensible sin la clave correcta.

### 6.2 Clave criptográfica

• Una clave es un valor matemático o secreto que permite realizar el proceso de cifrado y descifrado.
• La seguridad del sistema depende generalmente de la longitud, la calidad y la gestión de la clave.

### 6.3 Algoritmo criptográfico

• Un algoritmo es la función matemática o procedimiento que transforma el mensaje.
• Puede ser simétrico, asimétrico o híbrido.

### 6.4 Función hash

• Una función hash transforma un conjunto de datos de longitud variable en una secuencia fija.
• La salida se conoce como *hash* o *digest*.

**Ejemplo**: SHA-256 genera una suma de 256 bits a partir de cualquier entrada.

**Propiedades esenciales**:
- determinista: la misma entrada siempre produce el mismo hash;
- rápida de calcular;
- resistente a colisiones: es difícil encontrar dos mensajes distintos con el mismo hash;
- no reversible: a partir del hash no suele ser viable recuperar el mensaje original.

**Aplicaciones**:
- comprobación de integridad;
- almacenamiento seguro de contraseñas;
- firma digital;
- verificación de archivos.

### 6.5 Firma digital

- Una firma digital permite asegurar la autenticidad y la integridad de un documento o mensaje.
- Se genera usando la clave privada del emisor y se verifica usando la clave pública asociada.

**Ventajas**:
- autentica al remitente;
- permite verificar que el contenido no ha sido alterado;
- facilita el no repudio.

**Ejemplo**: un contrato firmado digitalmente no puede ser rechazado por el firmante alegando que no lo envió.

---

## 7. Fundamentos matemáticos básicos

La criptografía moderna está profundamente apoyada en conceptos matemáticos. Aunque no necesitamos proponer un tratado completo, sí resulta útil comprender algunos pilares básicos.

### 7.1 Aritmética modular

La aritmética modular consiste en operar con restos de la división. Por ejemplo:

$$
17 \equiv 2 \pmod{5}
$$

porque $17 = 3 \cdot 5 + 2$.

Esto significa que 17 y 2 son congruentes módulo 5.

**Ejemplo simple**:

$$
29 \equiv 9 \pmod{10}
$$

porque 29 al dividir entre 10 deja resto 9.

**Importancia**: la aritmética modular se usa en muchos algoritmos criptográficos, especialmente en RSA, ECC y protocolos de intercambio de claves.

### 7.2 Congruencias

Dos números $a$ y $b$ son congruentes módulo $n$ si tienen el mismo resto al dividirlos entre $n$.

$$
a \equiv b \pmod{n}
$$

**Ejemplo**:

$$
14 \equiv 4 \pmod{10}
$$

ya que $14 = 1 \cdot 10 + 4$.

### 7.3 Números primos

Un número primo es un entero mayor que 1 con exactamente dos divisores: 1 y él mismo. Algunos ejemplos son 2, 3, 5, 7, 11, 13, ...

Los números primos son fundamentales, porque muchos sistemas criptográficos se basan en la dificultad de factorizar números grandes que son producto de dos primos grandes.

**Ejemplo**:

$$
143 = 11 \times 13
$$

La factorización de un número como 143 es sencilla; sin embargo, factorizar un número de cientos de dígitos es un problema computacional muy difícil para un ordenador clásico.

### 7.4 Logaritmo discreto

En algunos protocolos criptográficos, la seguridad se apoya en el problema del logaritmo discreto. En esencia, dado un grupo cíclico y un valor $g^x$, resulta muy difícil calcular $x$ si el número es grande.

Este problema subyace a la seguridad de algunas implementaciones de clave pública.

### 7.5 Un ejemplo sencillo con modulo y exponentes

Supongamos que deseamos calcular:

$$
3^4 \pmod{5}
$$

Primero calculamos:

$$
3^4 = 81
$$

y luego:

$$
81 \equiv 1 \pmod{5}
$$

porque $81 = 16 \cdot 5 + 1$.

Este tipo de operaciones es frecuente en protocolos criptográficos y en algoritmos como RSA.

---

## 8. Métodos criptográficos modernos: RSA y ECC

Dentro de la criptografía asimétrica, dos de los métodos más relevantes son el algoritmo RSA y la criptografía basada en curvas elípticas (ECC). Ambos permiten establecer autenticación, cifrado y firmas digitales, pero se apoyan en problemas matemáticos distintos.

### 8.1 RSA

RSA es uno de los algoritmos más conocidos de la criptografía asimétrica y fue propuesto por Rivest, Shamir y Adleman en 1977. Su seguridad se fundamenta en la dificultad de factorizar un número grande que resulta del producto de dos primos grandes.

La idea básica es la siguiente:

1. Se eligen dos números primos grandes $p$ y $q$.
2. Se calcula $n = p \cdot q$.
3. Se calcula la función totiente de Euler: $\varphi(n) = (p-1)(q-1)$.
4. Se elige un exponente público $e$ tal que $\gcd(e, \varphi(n)) = 1$.
5. Se calcula la clave privada $d$ como el inverso modular de $e$ modulo $\varphi(n)$:

$$
   e \cdot d \equiv 1 \pmod{\varphi(n)}
$$

Una vez generadas las claves, el cifrado y el descifrado se basan en la exponenciación modular:

$$
   c = m^e \pmod{n}
$$

$$
   m = c^d \pmod{n}
$$

donde $m$ es el mensaje, $c$ es el texto cifrado y $n$ es el módulo público. La seguridad de RSA depende de que, aunque la clave pública se conozca, un atacante no pueda recuperar la clave privada sin factorizar $n$.

**Ventajas de RSA**:
- es muy conocido y ampliamente usado;
- permite cifrado y firma digital;
- se usa en muchos sistemas de infraestructura digital.

**Limitaciones**:
- requiere claves más grandes para mantener una seguridad equivalente;
- es computacionalmente más costoso que la criptografía simétrica;
- está siendo reemplazado parcialmente por curvas elípticas en algunos contextos modernos.

### 8.2 ECC (Elliptic Curve Cryptography)

La criptografía basada en curvas elípticas (ECC) utiliza propiedades matemáticas de las curvas elípticas sobre campos finitos. En lugar de depender de la factorización de números grandes como RSA, ECC se apoya en el problema del logaritmo discreto sobre curvas elípticas.

El diseño de ECC se centra en puntos sobre una curva de la forma:

$$
   y^2 = x^3 + ax + b
$$

y en una operación de suma entre puntos de la curva. El número secreto de un usuario se representa como un escalar multiplicado por un punto base $G$:

$$
   Q = kG
$$

donde $k$ es la clave privada y $Q$ es la clave pública. El problema para un atacante es, dado $Q$ y $G$, recuperar $k$; esto es precisamente el problema del logaritmo discreto sobre curvas elípticas.

**Ventajas de ECC**:
- proporciona la misma seguridad que RSA con claves mucho más cortas;
- es más eficiente en dispositivos con pocos recursos, como móviles o sensores;
- se usa en protocolos modernos como TLS, certificados digitales y criptografía de bajo consumo.

**Ejemplo de comparación**:
- una clave RSA de 3072 bits puede ofrecer un nivel de seguridad similar al de una clave ECC de 256 bits;
- por ello ECC es muy atractiva en sistemas móviles, blockchain, IoT y comunicaciones seguras.

### 8.3 Comparación entre RSA y ECC

| Algoritmo | Base matemática | Seguridad relativa | Uso típico | Ventaja principal |
|---|---|---|---|---|
| RSA | Factorización de enteros | Requiere claves grandes | Firmas y cifrado clásico | Muy extendido |
| ECC | Logaritmo discreto sobre curvas elípticas | Claves más cortas para igual seguridad | TLS, móviles, IoT, blockchain | Eficiencia |

### 8.4 Conclusión sobre RSA y ECC

Tanto RSA como ECC son pilares de la criptografía asimétrica moderna. RSA ha sido históricamente muy importante y sigue utilizándose en muchos sistemas; ECC, sin embargo, ofrece un mejor equilibrio entre seguridad y eficiencia, por lo que hoy es muy frecuente en entornos donde el coste computacional y el tamaño de la clave son relevantes.

---

## 9. Ejemplos prácticos

### 8.1 Ejemplo 1: envío seguro de un mensaje

Una empresa quiere enviar un informe confidencial a otra organización. Si usa un enfoque híbrido:

1. genera una clave simétrica;
2. cifra el archivo con esa clave simétrica;
3. cifra la clave simétrica con la clave pública del destinatario;
4. envía ambos elementos por red;
5. el destinatario usa su clave privada para recuperar la clave simétrica y luego descifrar el archivo.

Esto combina rapidez con seguridad en la distribución de claves.

### 8.2 Ejemplo 2: verificación de integridad

Una plataforma de software distribuido por Internet desea saber si un archivo se ha alterado durante la descarga. Para ello:

- calcula el hash del archivo original;
- el usuario calcula el hash del archivo recibido;
- compara ambas cadenas.

Si coinciden, la integridad se mantiene. Si no coinciden, el archivo se ha modificado.

### 8.3 Ejemplo 3: firma digital

Un profesor quiere firmar digitalmente un documento académico. El proceso sería:

1. calcula el hash del documento;
2. cifra ese hash con su clave privada;
3. adjunta la firma al documento;
4. el receptor verifica la firma con la clave pública del profesor.

Si la verificación es correcta, se comprueba la autenticidad del documento y su integridad.

---

## 9. Ejercicios propuestos con soluciones

### Ejercicio 1

Explica la diferencia entre criptografía simétrica y asimétrica.

**Solución orientativa**:
- La criptografía simétrica usa la misma clave para cifrar y descifrar.
- La criptografía asimétrica usa dos claves distintas: una pública y otra privada.
- La simétrica es más rápida, pero requiere compartir la clave de forma segura.
- La asimétrica resuelve la distribución de claves, pero suele ser más lenta.

### Ejercicio 2

Calcula:

$$
23 \pmod{7}
$$

**Solución**:

$$
23 = 3 \cdot 7 + 2
$$

por tanto:

$$
23 \equiv 2 \pmod{7}
$$

### Ejercicio 3

¿Para qué sirve una función hash?

**Solución orientativa**:
- detectar cambios en archivos;
- verificar integridad;
- guardar contraseñas o tokens de manera segura;
- apoyar la firma digital.

### Ejercicio 4

¿En qué situación sería más apropiado usar una criptografía híbrida?

**Solución orientativa**:
- cuando se necesita cifrar grandes cantidades de datos con rapidez y, además, proteger la distribución de la clave de manera segura.

### Ejercicio 5

¿Para qué sirve la firma digital?

**Solución orientativa**:
- autenticar al emisor;
- verificar la integridad del documento;
- proteger contra el no repudio.

---

## 10. Ejemplo sencillo de cálculo con Python

A continuación se muestra una pequeña demostración sencilla en Python para calcular un hash y una operación modular:

```python
import hashlib

mensaje = b'Hola, mundo seguro'
hash_resultado = hashlib.sha256(mensaje).hexdigest()
print('Hash SHA-256:', hash_resultado)

valor = 23
modulo = 7
print('23 mod 7 =', valor % modulo)
```

**Salida esperada**:

```text
Hash SHA-256: <valor generado>
23 mod 7 = 2
```

Este tipo de ejemplos ayuda a entender cómo la matemática y la computación se conectan con la seguridad de la información.

---

## 11. Importancia de la seguridad en la era digital

En la actualidad, la mayoría de los servicios digitales dependen de la criptografía de alguna forma. Por ejemplo:

- las páginas web usan HTTPS para proteger el tráfico;
- los bancos usan autenticación y firma digital;
- los correos electrónicos se cifran para evitar la lectura por terceros;
- los sistemas de identidad gestionan accesos con mecanismos criptográficos.

Sin una base criptográfica sólida, la confianza en los servicios digitales se deteriora rápidamente.

---

## 12. Errores habituales en la práctica

Es útil señalar algunos errores frecuentes que pueden comprometer la seguridad:

- usar contraseñas cortas o previsibles;
- reutilizar la misma clave en múltiples servicios;
- no verificar certificados digitales;
- transmitir claves por canales inseguros;
- usar algoritmos obsoletos;
- almacenar hashes sin sal (salt) cuando se trata de contraseñas.

**La seguridad no depende solo del algoritmo, sino de todo el entorno de su uso.**

---

## 13. Conclusiones

Las tres ideas principales que debe retener el estudiante de esta sesión son:

1. La criptografía es esencial para proteger la confidencialidad, la integridad, la autenticación y el no repudio.  
2. Existen diferentes tipos de criptografía —simétrica, asimétrica e híbrida—, cada uno con ventajas y limitaciones concretas.  
3. La seguridad moderna no se basa solo en conceptos intuitivos, sino también en fundamentos matemáticos y en la correcta gestión de claves y protocolos.

---

## 14. Bibliografía esencial

[1] Stallings, W. *Cryptography and Network Security: Principles and Practice*. Pearson.  
[2] Schneier, B. *Applied Cryptography*. Wiley.  
[3] Katz, J. y Lindell, Y. *Introduction to Modern Cryptography*. Chapman & Hall/CRC.  
[4] Menezes, A., van Oorschot, P. y Vanstone, S. *Handbook of Applied Cryptography*. CRC Press.  
[5] National Institute of Standards and Technology (NIST). *Digital Identity Guidelines* y documentación técnica relacionada con estándares de seguridad y criptografía.

---

## 15. Bibliografía recomendada

- Buchmann, J. A. *Introduction to Cryptography*. Springer.  
- Silverman, J. H. *A Friendly Introduction to Number Theory*. Pearson.  
- Ferguson, N., Schneier, B. y Kohno, T. *Cryptography Engineering*. Wiley.  
- Documentación oficial de TLS, X.509 y PKI para comprender la infraestructura actual de autenticación y confianza digital.

---

## 16. Preguntas de reflexión

1. ¿Por qué la confidencialidad por sí sola no garantiza la seguridad completa de un sistema?  
2. ¿Qué diferencia existe entre ocultar un mensaje y garantizar su integridad?  
3. ¿Qué problema resuelve la criptografía asimétrica frente a la simétrica?  
4. ¿Por qué la gestión de claves es tan crítica en cualquier sistema criptográfico?  
5. ¿Qué consecuencias tendría usar funciones hash débiles o algoritmos obsoletos?  
6. ¿Qué tipos de aplicaciones cotidianas dependen directamente de la criptografía?

---

## 17. Actividad recomendada para el aula

Se propone una actividad breve en parejas:

- cada estudiante elige una aplicación cotidiana (mensajes, banca, redes sociales, almacenamiento en la nube);
- identifica qué objetivo de seguridad es más importante en esa aplicación;
- explica qué tipo de criptografía podría emplearse;
- justifica si requeriría una clave simétrica, asimétrica o híbrida.

La intención es conectar los conceptos teóricos con casos reales del uso cotidiano de la tecnología.

