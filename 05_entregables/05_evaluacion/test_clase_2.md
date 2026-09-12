# Test de conocimientos. Clase 2: Criptografía asimétrica (RSA, ECC y protocolos)

## Instrucciones

Cada pregunta tiene cuatro opciones de respuesta, de las cuales solo una es correcta. Debajo de cada pregunta se indica la respuesta correcta y una breve retroalimentación con la explicación.

## Preguntas

### 1. En criptografía asimétrica, para **cifrar** un mensaje, ¿qué clave se usa para cifrar y cuál para descifrar?

- A) La clave privada cifra y la clave pública descifra
- B) La clave pública cifra y la clave privada descifra
- C) Se usa la misma clave para cifrar y para descifrar
- D) No se necesita ninguna clave si se usa RSA

**Respuesta correcta:** B

**Retroalimentación:** La regla para cifrado es "pública → cifrar, privada → descifrar". Es la regla inversa a la de la firma digital, que usa "privada → firmar, pública → verificar".

### 2. Para **firmar digitalmente** un documento, ¿qué clave utiliza el firmante?

- A) Su clave pública
- B) La clave pública del destinatario
- C) Su clave privada
- D) Una clave simétrica compartida con el destinatario

**Respuesta correcta:** C

**Retroalimentación:** El firmante usa su clave privada para firmar; cualquiera puede verificar la firma con la clave pública correspondiente del firmante.

### 3. ¿En qué se basa fundamentalmente la seguridad de RSA?

- A) En la dificultad de factorizar el producto de dos números primos grandes
- B) En el problema del logaritmo discreto sobre curvas elípticas
- C) En la dificultad de invertir una función hash
- D) En la longitud del canal de comunicación

**Respuesta correcta:** A

**Retroalimentación:** RSA se apoya en que es fácil multiplicar dos primos grandes, pero muy difícil factorizar el resultado si esos primos son suficientemente grandes.

### 4. En el ejemplo numérico de la sesión, Alice cifra el mensaje $m=10$ con la clave pública de Bob $(e,n)=(3,55)$. ¿Qué valor de $c$ obtiene?

- A) $c = 100$
- B) $c = 1000$
- C) $c = 10$
- D) $c = 55$

**Respuesta correcta:** C

**Retroalimentación:** $c = m^e \bmod n = 10^3 \bmod 55 = 1000 \bmod 55 = 10$. En este ejemplo pequeño el cifrado coincide numéricamente con el mensaje original; con primos grandes esto no ocurre.

### 5. ¿En qué problema matemático se basa la seguridad de ECC (Elliptic Curve Cryptography)?

- A) En la factorización de números enteros grandes
- B) En el problema del logaritmo discreto sobre curvas elípticas
- C) En la dificultad de invertir SHA-256
- D) En el problema de aprendizaje con errores (LWE)

**Respuesta correcta:** B

**Retroalimentación:** ECC no se basa en factorización como RSA, sino en que, dados un punto $P$ y $Q = kP$, es muy difícil recuperar $k$: el problema del logaritmo discreto en curvas elípticas.

### 6. Según la comparativa de la sesión, ¿qué tamaño de clave ECC ofrece un nivel de seguridad equivalente a una clave RSA de 2048 bits?

- A) Aproximadamente 224-256 bits
- B) Exactamente 2048 bits también
- C) Aproximadamente 4096 bits
- D) Solo 56 bits

**Respuesta correcta:** A

**Retroalimentación:** ECC alcanza un nivel de seguridad comparable al de RSA-2048 con claves de entre 224 y 256 bits, lo que reduce el consumo de CPU, memoria y ancho de banda.

### 7. ¿Cuál es la principal limitación de Diffie-Hellman "puro", sin ningún mecanismo adicional?

- A) No permite generar un secreto compartido en ningún caso
- B) Es más lento que RSA en todos los escenarios
- C) No autentica a las partes, por lo que es vulnerable a un ataque de intermediario (MITM)
- D) Solo funciona con curvas elípticas

**Respuesta correcta:** C

**Retroalimentación:** Diffie-Hellman permite acordar un secreto sin enviarlo directamente, pero por sí solo no verifica la identidad de las partes. Por eso en la práctica se combina con certificados o firmas.

### 8. ¿Qué es un certificado digital dentro de una infraestructura de clave pública (PKI)?

- A) Un algoritmo de cifrado simétrico
- B) Un documento que vincula una clave pública con la identidad de su propietario, firmado por una autoridad certificadora
- C) Una clave privada protegida por contraseña
- D) Un protocolo de acuerdo de claves alternativo a Diffie-Hellman

**Respuesta correcta:** B

**Retroalimentación:** El certificado digital vincula una clave pública con una identidad y está firmado por una CA de confianza; la cadena de confianza permite verificar ese certificado remontando hasta una CA raíz.

### 9. En una conexión TLS/HTTPS moderna, ¿qué mecanismo se usa habitualmente para el intercambio de claves?

- A) RSA sin relleno (RSA "puro")
- B) ECDH (Diffie-Hellman sobre curva elíptica)
- C) Un MAC compartido de antemano
- D) Un hash SHA-256 del certificado

**Respuesta correcta:** B

**Retroalimentación:** TLS moderno combina un intercambio de claves basado en ECDH, autenticación del servidor mediante certificado y derivación de claves simétricas para cifrar el tráfico con un esquema AEAD como AES-GCM.

### 10. ¿Por qué RSA nunca se usa "en crudo" (sin relleno) en sistemas reales?

- A) Porque la versión pura del algoritmo es determinista y vulnerable a ataques matemáticos conocidos; se necesita un esquema de relleno como OAEP o PSS
- B) Porque RSA sin relleno es ilegal en la mayoría de países
- C) Porque sin relleno RSA no puede generar ninguna clave pública
- D) Porque el relleno hace que RSA deje de depender de la factorización

**Respuesta correcta:** A

**Retroalimentación:** RSA "puro" es determinista y expuesto a ataques conocidos. En la práctica se usa RSA-OAEP para cifrado y RSA-PSS para firmas, que añaden aleatoriedad y protecciones adicionales.
