# Test de conocimientos. Clase 4: Introducción a la criptografía post-cuántica y ML-KEM/Kyber

## Instrucciones

Cada pregunta tiene cuatro opciones de respuesta, de las cuales solo una es correcta. Debajo de cada pregunta se indica la respuesta correcta y una breve retroalimentación con la explicación.

## Preguntas

### 1. ¿Qué cambia realmente en la criptografía post-cuántica respecto a la criptografía clásica?

- A) Se necesitan ordenadores cuánticos para poder cifrar
- B) Cambia el problema matemático en el que se apoya la seguridad, manteniendo ordenadores y redes clásicos
- C) Desaparece la necesidad de usar claves
- D) Solo cambia el lenguaje de programación utilizado

**Respuesta correcta:** B

**Retroalimentación:** La criptografía post-cuántica se ejecuta en ordenadores y redes clásicos. Lo que cambia es que se eligen problemas matemáticos para los que no se conoce un ataque eficiente, ni clásico ni cuántico.

### 2. ¿Qué describe el escenario "recoger ahora, descifrar después" (*harvest now, decrypt later*)?

- A) Guardar hoy tráfico cifrado para intentar descifrarlo en el futuro con un ordenador cuántico
- B) Un modo de operación del cifrado simétrico
- C) Un tipo de firma digital post-cuántica
- D) Un protocolo de intercambio de claves ya estandarizado por el NIST

**Respuesta correcta:** A

**Retroalimentación:** La urgencia de migrar a PQC no depende solo de cuándo exista un ordenador cuántico suficientemente grande: un atacante puede almacenar hoy datos cifrados y descifrarlos años después, lo que afecta especialmente a datos con vida confidencial larga.

### 3. Según la tabla de familias de métodos post-cuánticos de la sesión, ¿en qué familia se agrupan ML-KEM, ML-DSA y NTRU?

- A) Códigos
- B) Retículos
- C) Funciones hash
- D) Isogenias

**Respuesta correcta:** B

**Retroalimentación:** ML-KEM, ML-DSA y NTRU pertenecen a la familia de retículos (vectores cortos y ecuaciones con ruido). Los códigos incluyen HQC y Classic McEliece; las funciones hash incluyen SLH-DSA.

### 4. ¿A qué estándar NIST corresponde ML-KEM?

- A) FIPS 205
- B) FIPS 204
- C) FIPS 203
- D) FIPS 206

**Respuesta correcta:** C

**Retroalimentación:** ML-KEM (derivado de CRYSTALS-Kyber) está estandarizado en NIST FIPS 203, "Module-Lattice-Based Key-Encapsulation Mechanism Standard".

### 5. En un mecanismo de encapsulación de claves (KEM), ¿qué elemento NO debe viajar por la red?

- A) ek, la clave pública de encapsulación
- B) c, el texto de encapsulación
- C) K, el secreto compartido
- D) Ninguno de los anteriores; todos son públicos

**Respuesta correcta:** C

**Retroalimentación:** ek y c pueden transmitirse por la red; dk (clave privada) y K (secreto compartido) deben protegerse. Ambos extremos obtienen K mediante operaciones distintas sin que viaje directamente por el canal.

### 6. En el problema LWE (Learning With Errors), ¿qué papel cumple el vector $e$?

- A) Es la clave pública completa del sistema
- B) Es un vector de error pequeño y aleatorio que impide tratar el sistema como uno lineal exacto
- C) Es el mensaje cifrado final que se transmite
- D) Es el módulo $q$ utilizado en las operaciones

**Respuesta correcta:** B

**Retroalimentación:** LWE añade un vector de error pequeño a un sistema lineal ($b = As+e$). El receptor legítimo aprovecha su estructura, pero un atacante ve ecuaciones que no encajan exactamente, lo que dificulta recuperar el secreto $s$.

### 7. ¿Qué estructura matemática utiliza específicamente ML-KEM (Module-LWE) en lugar de simples vectores de enteros?

- A) Números primos gigantes sin estructura adicional
- B) Polinomios que operan dentro de un anillo cociente
- C) Curvas elípticas sobre cuerpos finitos
- D) Árboles de Merkle con funciones hash

**Respuesta correcta:** B

**Retroalimentación:** ML-KEM usa Module-LWE: sus componentes son polinomios y la multiplicación se realiza en un anillo cociente, lo que acelera el cálculo y reduce el tamaño de las claves.

### 8. ¿Qué relación existe entre un KEM como ML-KEM y un cifrado autenticado como AES-GCM?

- A) El KEM cifra directamente archivos completos y AES-GCM deja de ser necesario
- B) El KEM establece un secreto compartido que después se usa, vía una función de derivación (KDF), para cifrar con AES-GCM u otro AEAD
- C) Ambos mecanismos son exactamente equivalentes y sustituibles entre sí
- D) AES-GCM sustituye por completo al KEM en cualquier protocolo híbrido

**Respuesta correcta:** B

**Retroalimentación:** Un KEM no cifra un archivo completo: produce el mismo secreto compartido en ambos extremos. Ese secreto se deriva con una KDF (por ejemplo HKDF) y se usa para cifrar con un AEAD como AES-GCM o ChaCha20-Poly1305.

### 9. ¿Cómo se compensa, según la sesión, el efecto del algoritmo de Grover sobre la criptografía simétrica?

- A) No es posible compensarlo de ninguna forma
- B) Usando claves suficientemente largas, ya que la ventaja de Grover es solo cuadrática
- C) Sustituyendo AES por RSA en todos los sistemas
- D) No es necesario compensarlo porque Grover no afecta a la criptografía simétrica

**Respuesta correcta:** B

**Retroalimentación:** Grover ofrece solo una ventaja cuadrática sobre la búsqueda exhaustiva, por lo que basta con aumentar el tamaño de clave (por ejemplo, usar AES-256) para mantener el nivel de seguridad deseado.

### 10. En el ejemplo de Python de la sesión, ¿qué se deriva del secreto compartido (`shared_secret`) mediante HKDF antes de cifrar el mensaje?

- A) Una clave simétrica para usar con AES-GCM
- B) Un nuevo par de claves RSA
- C) Un certificado digital X.509
- D) Un nonce que se reutiliza en cada mensaje

**Respuesta correcta:** A

**Retroalimentación:** El secreto compartido obtenido mediante ML-KEM se pasa por HKDF para derivar una clave simétrica, que se usa junto con un nonce aleatorio (no reutilizado) para cifrar con AES-GCM.
