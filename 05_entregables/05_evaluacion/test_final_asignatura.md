# Test final de la asignatura: de los fundamentos de la criptografía a la criptografía post-cuántica

## Instrucciones

Este test integra las seis sesiones de la asignatura. Cada pregunta tiene cuatro opciones de respuesta, de las cuales solo una es correcta. Debajo de cada pregunta se indica la respuesta correcta y una breve retroalimentación con la explicación.

## Preguntas

### 1. (Sesión 1) ¿Cuál de los siguientes objetivos de seguridad NO es proporcionado directamente por la criptografía?

- A) Confidencialidad
- B) Integridad
- C) Disponibilidad
- D) Autenticación

**Respuesta correcta:** C

**Retroalimentación:** La disponibilidad es un objetivo general de la seguridad de la información, pero no una propiedad que proporcione directamente la criptografía, a diferencia de la confidencialidad, la integridad y la autenticación.

### 2. (Sesión 1 y 2) En criptografía asimétrica, ¿qué clave usa el firmante para firmar un mensaje y qué clave usa el verificador para comprobar la firma?

- A) El firmante usa su clave pública y el verificador usa su propia clave privada
- B) El firmante usa su clave privada y el verificador usa la clave pública del firmante
- C) Ambos usan la misma clave simétrica compartida
- D) El firmante usa la clave privada del verificador

**Respuesta correcta:** B

**Retroalimentación:** La regla de la firma digital es "privada firma, pública verifica"; es la regla opuesta a la del cifrado con clave pública ("pública cifra, privada descifra").

### 3. (Sesión 2) ¿En qué problema matemático se apoya fundamentalmente la seguridad de RSA?

- A) El logaritmo discreto sobre curvas elípticas
- B) La dificultad de factorizar el producto de dos primos grandes
- C) El problema de aprendizaje con errores (LWE)
- D) La construcción de árboles de Merkle

**Respuesta correcta:** B

**Retroalimentación:** RSA se basa en que es fácil multiplicar dos primos grandes, pero muy difícil factorizar el resultado si esos primos son suficientemente grandes.

### 4. (Sesión 2) ¿Qué ventaja principal ofrece ECC frente a RSA?

- A) Un nivel de seguridad equivalente con claves mucho más pequeñas
- B) Es inmune a cualquier ataque cuántico, a diferencia de RSA
- C) No necesita ningún tipo de clave privada
- D) Sustituye completamente a las funciones hash

**Respuesta correcta:** A

**Retroalimentación:** ECC ofrece un nivel de seguridad comparable al de RSA con claves mucho más pequeñas (por ejemplo, ~224-256 bits frente a 2048 bits de RSA), lo que mejora el rendimiento en dispositivos con recursos limitados.

### 5. (Sesión 3) ¿Qué logra el algoritmo de Shor sobre RSA, ECC y Diffie-Hellman?

- A) Los debilita ligeramente, obligando a duplicar el tamaño de clave
- B) Los rompe por completo, resolviendo en tiempo polinómico la factorización y el logaritmo discreto
- C) No tiene ningún efecto sobre ellos
- D) Solo afecta a las funciones hash utilizadas en las firmas

**Respuesta correcta:** B

**Retroalimentación:** Shor resuelve en tiempo polinómico problemas intratables clásicamente, rompiendo completamente la criptografía asimétrica basada en factorización y logaritmo discreto (RSA, ECC, Diffie-Hellman).

### 6. (Sesión 3) ¿Cómo afecta el algoritmo de Grover a AES y a las funciones hash?

- A) Las rompe igual que Shor rompe RSA
- B) No las afecta en absoluto
- C) Las debilita mediante una aceleración cuadrática, sin llegar a romperlas si se usan tamaños de clave/salida suficientes
- D) Las convierte en algoritmos deterministas

**Respuesta correcta:** C

**Retroalimentación:** Grover ofrece solo una ventaja cuadrática ($O(\sqrt{N})$), por lo que AES y las funciones hash se debilitan pero no se rompen, compensándose con claves o salidas más largas (AES-256, hashes de 384-512 bits).

### 7. (Sesión 4) ¿Qué cambia realmente al pasar de la criptografía clásica a la post-cuántica?

- A) Se necesita hardware cuántico para poder cifrar y descifrar
- B) Cambia el problema matemático subyacente, pero se sigue operando con ordenadores y redes clásicos
- C) Deja de ser necesario usar ninguna clave
- D) Solo cambia el lenguaje de programación empleado

**Respuesta correcta:** B

**Retroalimentación:** La criptografía post-cuántica funciona en ordenadores y redes clásicos; lo que cambia es la elección de problemas matemáticos sin ataque eficiente conocido, ni clásico ni cuántico.

### 8. (Sesión 4) ¿En qué familia de métodos post-cuánticos se agrupan ML-KEM, ML-DSA y NTRU?

- A) Códigos correctores de errores
- B) Retículos
- C) Funciones hash
- D) Isogenias

**Respuesta correcta:** B

**Retroalimentación:** ML-KEM, ML-DSA y NTRU pertenecen a la familia de retículos, basada en vectores cortos y ecuaciones con ruido. HQC y Classic McEliece pertenecen a la familia de códigos; SLH-DSA a la de funciones hash.

### 9. (Sesión 4) En el problema LWE (Learning With Errors), ¿qué papel cumple el vector de error $e$?

- A) Es la clave pública completa
- B) Impide que el sistema $b = As + e$ pueda resolverse como un sistema lineal exacto
- C) Es el mensaje cifrado final
- D) Sustituye completamente al secreto $s$

**Respuesta correcta:** B

**Retroalimentación:** El error pequeño y aleatorio $e$ hace que un atacante vea ecuaciones que no encajan exactamente, mientras que el receptor legítimo, que conoce la estructura, sí puede recuperar la información.

### 10. (Sesión 5) ¿Cómo se representan los mensajes, claves y aleatoriedad en NTRU?

- A) Como números primos grandes
- B) Como polinomios de coeficientes pequeños, con productos calculados mediante convolución circular
- C) Como puntos sobre una curva elíptica
- D) Como árboles de Merkle con hojas hash

**Respuesta correcta:** B

**Retroalimentación:** NTRU trabaja en un anillo de polinomios: el producto de dos polinomios se reduce a una convolución circular, y la clave pública mezcla dos polinomios secretos mediante una inversa modular.

### 11. (Sesión 5) ¿Cuál es el estado normativo de NTRU frente a ML-KEM en el ecosistema NIST actual?

- A) NTRU sustituyó a ML-KEM como estándar principal
- B) NTRU no fue seleccionado como estándar NIST; ML-KEM (FIPS 203) es el KEM principal estandarizado
- C) Ambos algoritmos están prohibidos por el NIST
- D) Solo se puede usar uno de los dos, nunca ambos en el mismo proyecto

**Respuesta correcta:** B

**Retroalimentación:** NTRU conserva valor docente e histórico y sigue disponible en implementaciones como liboqs, pero no fue seleccionado como estándar; ML-KEM es el KEM principal estandarizado por el NIST.

### 12. (Sesión 6) ¿De qué construcción deriva ML-DSA y en qué transformación se apoya para calcular el reto de forma no interactiva?

- A) Deriva de SPHINCS+ y se apoya en árboles de Merkle
- B) Deriva de CRYSTALS-Dilithium y se apoya en la transformación de Fiat-Shamir
- C) Deriva de NTRU y se apoya en convolución circular
- D) Deriva de ML-KEM y se apoya en Module-LWE únicamente

**Respuesta correcta:** B

**Retroalimentación:** ML-DSA deriva de CRYSTALS-Dilithium y usa la transformación de Fiat-Shamir para calcular el reto como un hash que incluye el mensaje, evitando así un protocolo interactivo.

### 13. (Sesión 6) ¿En qué se basa la seguridad de SLH-DSA y qué característica clave lo distingue de ML-DSA?

- A) Se basa en retículos, igual que ML-DSA
- B) Se basa en propiedades de funciones hash y árboles de Merkle, y es "stateless" (no requiere recordar el estado entre firmas)
- C) Se basa en la factorización de enteros grandes
- D) Requiere un ordenador cuántico para firmar

**Respuesta correcta:** B

**Retroalimentación:** A diferencia de ML-DSA (basado en retículos), SLH-DSA se apoya en funciones hash y árboles de Merkle, y su diseño "stateless" evita fallos de gestión de estado presentes en otros esquemas de firma basados en hash.

### 14. (Sesión 6) A fecha de 12 de septiembre de 2026, ¿qué describe mejor el estado de la estandarización PQC del NIST?

- A) FIPS 203, 204 y 205 son finales; HQC fue elegido como segundo KEM y FN-DSA/HQC-KEM siguen en desarrollo
- B) Ningún estándar de PQC ha sido finalizado todavía
- C) Solo existe un estándar, FIPS 203, y el resto se han cancelado
- D) El proceso de estandarización terminó por completo, sin candidatos activos restantes

**Respuesta correcta:** A

**Retroalimentación:** Los tres primeros estándares (ML-KEM, ML-DSA y SLH-DSA) ya están finalizados. HQC fue elegido como segundo KEM en marzo de 2025, y siguen activos varios candidatos adicionales de firma (FAEST, MAYO, MQOM, QR-UOV, SDitH, SNOVA, SQIsign, UOV).

### 15. (Integradora) ¿Por qué es importante empezar ya la migración hacia criptografía post-cuántica aunque hoy no exista un ordenador cuántico capaz de romper RSA?

- A) Por el riesgo de "recoger ahora, descifrar después" sobre datos con vida confidencial larga, y porque la migración exige inventario y criptoagilidad, no un cambio inmediato de un día para otro
- B) Porque ya existen ataques cuánticos prácticos y verificados contra AES-256
- C) Porque el NIST obliga legalmente a todos los países a migrar de inmediato
- D) Porque la criptografía clásica ha dejado de funcionar en cualquier escenario actual

**Respuesta correcta:** A

**Retroalimentación:** El riesgo "harvest now, decrypt later" afecta hoy a datos que deben seguir siendo confidenciales durante años. Además, migrar requiere primero inventariar algoritmos y claves, y ganar criptoagilidad, un proceso que lleva tiempo y conviene iniciar cuanto antes.
