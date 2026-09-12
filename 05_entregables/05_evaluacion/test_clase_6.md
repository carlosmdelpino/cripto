# Test de conocimientos. Clase 6: ML-DSA, SLH-DSA y estado actual de la estandarización

## Instrucciones

Cada pregunta tiene cuatro opciones de respuesta, de las cuales solo una es correcta. Debajo de cada pregunta se indica la respuesta correcta y una breve retroalimentación con la explicación.

## Preguntas

### 1. ¿Qué diferencia principal hay entre una firma digital y un cifrado?

- A) La firma digital oculta el contenido del mensaje, igual que el cifrado
- B) La firma digital no oculta el mensaje: cualquiera puede verificarla con la clave pública del firmante
- C) Ambos mecanismos son exactamente equivalentes
- D) El cifrado siempre requiere la clave privada del receptor para cifrar

**Respuesta correcta:** B

**Retroalimentación:** La firma no oculta el mensaje: el emisor la calcula con su clave privada y cualquiera puede verificarla con la clave pública, siempre que confíe en que esa clave pertenece realmente al firmante.

### 2. ¿De qué construcción previa deriva ML-DSA?

- A) SPHINCS+
- B) CRYSTALS-Dilithium
- C) CRYSTALS-Kyber
- D) NTRU

**Respuesta correcta:** B

**Retroalimentación:** ML-DSA es la firma digital de NIST basada en retículos derivada de CRYSTALS-Dilithium, y trabaja con vectores de polinomios y secretos pequeños.

### 3. ¿Qué transformación permite a ML-DSA calcular el reto (challenge) de forma no interactiva, mediante un hash que incluye el mensaje?

- A) La transformación de Fiat-Shamir
- B) La transformada cuántica de Fourier
- C) La construcción de un árbol de Merkle
- D) La convolución circular

**Respuesta correcta:** A

**Retroalimentación:** ML-DSA convierte un protocolo de reto-respuesta interactivo en un esquema de firma no interactivo mediante la transformación de Fiat-Shamir, calculando el reto como un hash que incluye el mensaje.

### 4. ¿Para qué sirve el muestreo por rechazo (rejection sampling) en ML-DSA?

- A) Para acelerar el proceso de verificación de la firma
- B) Para evitar que la distribución estadística de las firmas filtre información sobre el secreto
- C) Para generar directamente la clave pública del firmante
- D) Para comprimir el tamaño final de la firma

**Respuesta correcta:** B

**Retroalimentación:** El firmante rechaza y repite el proceso si ciertos valores (como $z$) salen de los límites permitidos, evitando que la distribución observable de las firmas filtre información útil sobre el secreto.

### 5. ¿En qué basa su seguridad SLH-DSA (derivado de SPHINCS+)?

- A) En la factorización de números enteros
- B) En el logaritmo discreto sobre curvas elípticas
- C) En propiedades de funciones hash y árboles de Merkle
- D) En el problema de retículos LWE

**Respuesta correcta:** C

**Retroalimentación:** SLH-DSA no depende de retículos: combina firmas de un solo uso, esquemas de pocos usos y árboles de Merkle, apoyándose principalmente en propiedades de funciones hash.

### 6. ¿Qué significa que SLH-DSA sea "stateless" (sin estado)?

- A) Que carece de clave pública
- B) Que el firmante no necesita recordar qué hoja del árbol utilizó entre una firma y la siguiente
- C) Que no puede verificar ninguna firma una vez generada
- D) Que no utiliza ninguna función hash en su construcción

**Respuesta correcta:** B

**Retroalimentación:** Ser "stateless" evita fallos catastróficos de gestión de estado (como reutilizar una hoja del árbol), presentes en otros esquemas de firma basados en hash con estado.

### 7. Para verificar una hoja de un árbol de Merkle sin transmitir el árbol completo, ¿qué se necesita?

- A) Todas las hojas del árbol completo
- B) La firma y el camino de autenticación formado por los nodos hermanos hasta la raíz
- C) Únicamente la clave privada del firmante
- D) Generar un árbol de Merkle completamente nuevo

**Respuesta correcta:** B

**Retroalimentación:** Basta con la firma y el camino de autenticación (los nodos hermanos necesarios) para que el verificador reconstruya la raíz y la compare con la raíz pública, sin necesitar el árbol completo.

### 8. Según el estado descrito a fecha de 12 de septiembre de 2026, ¿qué estándares de PQC del NIST están ya finalizados?

- A) Únicamente FIPS 203
- B) FIPS 203, FIPS 204 y FIPS 205
- C) FIPS 206 y FIPS 207 exclusivamente
- D) Ninguno; todos siguen en fase de borrador

**Respuesta correcta:** B

**Retroalimentación:** Los tres primeros estándares (FIPS 203 para ML-KEM, FIPS 204 para ML-DSA y FIPS 205 para SLH-DSA) ya están listos para adopción; FN-DSA y HQC-KEM seguían en desarrollo en esa fecha.

### 9. ¿Qué algoritmo fue elegido en marzo de 2025 como segundo mecanismo de encapsulación de claves (KEM) estandarizado, como alternativa matemática a ML-KEM?

- A) NTRU
- B) HQC
- C) SLH-DSA
- D) FN-DSA

**Respuesta correcta:** B

**Retroalimentación:** HQC (basado en códigos correctores de errores, no en retículos) fue elegido en marzo de 2025 como segundo KEM, aportando diversidad matemática frente a ML-KEM.

### 10. Ante una migración donde los datos deben seguir siendo confidenciales durante 15 años, ¿cuál es el primer paso recomendado según el plan de migración de la sesión?

- A) Sustituir directamente ECDSA por SLH-DSA sin ningún análisis previo
- B) Inventariar algoritmos, claves, certificados, bibliotecas y vida útil de los datos
- C) Esperar a que exista un ordenador cuántico capaz de romper RSA
- D) Ignorar el riesgo porque el ataque aún no es viable hoy

**Respuesta correcta:** B

**Retroalimentación:** El primer paso del plan es inventariar algoritmos, claves, certificados, bibliotecas y la vida útil de los datos; después se prueba ML-KEM en un protocolo híbrido y se migra la firma a ML-DSA o SLH-DSA según las restricciones del proyecto.
