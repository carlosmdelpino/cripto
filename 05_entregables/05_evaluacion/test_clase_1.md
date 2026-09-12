# Test de conocimientos. Clase 1: Fundamentos de la criptografía

## Instrucciones

Cada pregunta tiene cuatro opciones de respuesta, de las cuales solo una es correcta. Debajo de cada pregunta se indica la respuesta correcta y una breve retroalimentación con la explicación.

## Preguntas

### 1. En el modelo de amenaza de Alice, Bob y Eve, ¿qué representa Eve?

- A) La autoridad certificadora que valida las claves de Alice y Bob
- B) Un atacante que puede escuchar, modificar, inyectar o eliminar mensajes del canal
- C) La clave privada compartida entre Alice y Bob
- D) El protocolo TLS que protege la comunicación

**Respuesta correcta:** B

**Retroalimentación:** Eve representa al atacante (pasivo o activo) del modelo de amenaza. Un atacante pasivo solo escucha; uno activo puede además interceptar, modificar, repetir o suplantar mensajes.

### 2. ¿Qué ocurre exactamente en un ataque de intermediario (MITM)?

- A) Eve rompe matemáticamente el algoritmo de cifrado utilizado
- B) Alice y Bob creen comunicarse directamente entre sí, pero Eve controla el canal y puede suplantar a ambos
- C) El mensaje se autodestruye tras ser leído por el destinatario
- D) Bob deja de recibir cualquier mensaje de Alice

**Respuesta correcta:** B

**Retroalimentación:** El MITM no rompe el algoritmo: explota la falta de autenticación. Por eso cifrar un mensaje no basta si no se autentica también a los interlocutores.

### 3. ¿Qué objetivo de seguridad responde a la pregunta "¿ha sido modificado el mensaje?"

- A) Confidencialidad
- B) Disponibilidad
- C) Integridad
- D) No repudio

**Respuesta correcta:** C

**Retroalimentación:** La integridad garantiza que el contenido no cambia durante la transmisión o el almacenamiento. La confidencialidad responde a "¿quién puede leerlo?" y el no repudio a "¿puede negarse la autoría?".

### 4. Según la sesión, ¿de qué depende el no repudio además de la criptografía?

- A) Únicamente de la velocidad del canal de comunicación
- B) Del color o formato en que se presente la clave pública
- C) Del protocolo, la gestión de claves y el contexto legal
- D) De usar exclusivamente algoritmos simétricos

**Respuesta correcta:** C

**Retroalimentación:** El no repudio no es una propiedad puramente matemática: depende también de cómo se gestionan las claves, del protocolo utilizado y del marco legal que da validez a la prueba criptográfica.

### 5. ¿Qué necesita un MAC (Message Authentication Code) para funcionar, a diferencia de una firma digital?

- A) Un par de claves pública y privada
- B) Un certificado emitido por una autoridad certificadora
- C) Una clave secreta compartida entre emisor y receptor
- D) Una función hash que sea reversible

**Respuesta correcta:** C

**Retroalimentación:** El MAC autentica integridad y origen usando una clave secreta que comparten emisor y receptor. La firma digital, en cambio, usa un par de claves pública/privada y permite verificación por terceros sin compartir secretos.

### 6. ¿Cuál de las siguientes afirmaciones sobre hash y cifrado es correcta?

- A) El hash es reversible y el cifrado no
- B) El cifrado es reversible con la clave adecuada; el hash no es reversible en la práctica
- C) Ambos mecanismos son reversibles de la misma forma
- D) Ninguno de los dos utiliza una clave en ningún caso

**Respuesta correcta:** B

**Retroalimentación:** El cifrado permite recuperar el mensaje original con la clave correcta. Una función hash produce una huella digital de longitud fija que no debe poder invertirse para recuperar la entrada original.

### 7. ¿Qué aporta un esquema de cifrado autenticado o AEAD, como AES-GCM?

- A) Solamente confidencialidad
- B) Solamente integridad, sin confidencialidad
- C) Confidencialidad e integridad/autenticidad de forma conjunta
- D) Solamente no repudio

**Respuesta correcta:** C

**Retroalimentación:** AEAD (Authenticated Encryption with Associated Data) combina en un solo mecanismo la protección del contenido (confidencialidad) y la detección de modificaciones (integridad y autenticidad).

### 8. ¿Qué riesgo existe si se reutiliza el mismo nonce con la misma clave en un esquema como AES-GCM?

- A) Ninguno, los nonces son un detalle sin importancia práctica
- B) Se compromete gravemente la seguridad del cifrado autenticado
- C) El mensaje se cifra automáticamente el doble de rápido
- D) La clave pública del destinatario queda expuesta

**Respuesta correcta:** B

**Retroalimentación:** La correcta gestión de nonces, IVs y aleatoriedad es tan importante como el algoritmo elegido. Reutilizar un nonce con la misma clave en GCM compromete la confidencialidad y la autenticidad del cifrado.

### 9. En el protocolo Diffie-Hellman, tras el intercambio de $A = g^a \bmod p$ y $B = g^b \bmod p$, ¿qué valor final comparten Alice y Bob?

- A) $K = a + b$
- B) $K = p / g$
- C) $K = g^{ab} \bmod p$
- D) $K = g \bmod (a \times b)$

**Respuesta correcta:** C

**Retroalimentación:** Alice calcula $K = B^a \bmod p$ y Bob calcula $K = A^b \bmod p$; ambos resultados equivalen a $K = g^{ab} \bmod p$, el secreto compartido, sin haberlo transmitido directamente por el canal.

### 10. En el ejemplo didáctico de RSA de esta sesión, con $p=5$ y $q=11$, ¿cuáles son los valores de $n$ y $\varphi(n)$?

- A) $n = 16$, $\varphi(n) = 55$
- B) $n = 55$, $\varphi(n) = 40$
- C) $n = 40$, $\varphi(n) = 55$
- D) $n = 55$, $\varphi(n) = 55$

**Respuesta correcta:** B

**Retroalimentación:** $n = p \times q = 5 \times 11 = 55$ y $\varphi(n) = (p-1)(q-1) = 4 \times 10 = 40$. Con estos valores se eligió $e=3$ y se calculó $d=27$ como inverso modular de $e$ módulo $\varphi(n)$.
