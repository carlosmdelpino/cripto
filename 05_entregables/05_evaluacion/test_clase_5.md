# Test de conocimientos. Clase 5: NTRU

## Instrucciones

Cada pregunta tiene cuatro opciones de respuesta, de las cuales solo una es correcta. Debajo de cada pregunta se indica la respuesta correcta y una breve retroalimentación con la explicación.

## Preguntas

### 1. En NTRU, ¿cómo se representan los mensajes, las claves y la aleatoriedad?

- A) Como números primos grandes
- B) Como polinomios de coeficientes pequeños
- C) Como puntos sobre una curva elíptica
- D) Como árboles de Merkle

**Respuesta correcta:** B

**Retroalimentación:** NTRU trabaja con polinomios de coeficientes pequeños. La clave pública mezcla dos polinomios secretos mediante una inversa modular.

### 2. ¿Qué operación resulta al multiplicar dos polinomios en el anillo de NTRU (reducido módulo $X^N-1$)?

- A) Una convolución circular
- B) Un logaritmo discreto
- C) Una función hash de un solo sentido
- D) Un producto matricial estándar sin reducción

**Respuesta correcta:** A

**Retroalimentación:** Al fijar un grado $N$ y hacer que los términos que lo superan "vuelvan al principio", el producto de polinomios se convierte en una convolución circular.

### 3. ¿Qué papel cumplen los dos módulos de NTRU, $p$ (pequeño) y $q$ (grande)?

- A) $p$ representa el mensaje y $q$ deja espacio para mezclar mensaje y aleatoriedad sin perder la posibilidad de centrar coeficientes
- B) Ambos módulos son iguales y cumplen exactamente la misma función
- C) $p$ es directamente la clave privada y $q$ la clave pública
- D) Solo se utiliza el módulo $q$; $p$ es irrelevante para el descifrado

**Respuesta correcta:** A

**Retroalimentación:** El módulo pequeño $p$ representa el mensaje; el módulo grande $q$ permite mezclar mensaje y aleatoriedad conservando la posibilidad de centrar los coeficientes durante el descifrado.

### 4. ¿Qué condición debe cumplir el polinomio $f$ en la generación de claves de NTRU?

- A) Debe ser idéntico al polinomio $g$
- B) Debe tener inversa módulo $p$ y módulo $q$
- C) Debe ser un número primo mayor que $q$
- D) Debe valer cero en todos sus coeficientes

**Respuesta correcta:** B

**Retroalimentación:** $f$ debe ser invertible en ambos módulos: debe existir un polinomio cuyo producto con $f$ dé el elemento neutro, tanto módulo $p$ como módulo $q$.

### 5. ¿Cómo se calcula la clave pública $h$ en NTRU a partir de $f$ y $g$?

- A) Multiplicando la inversa de $f$ módulo $q$ por $g$, y ajustando el resultado con el factor $p$
- B) Sumando directamente los coeficientes de $f$ y $g$
- C) $h$ se elige completamente al azar, sin relación con $f$ ni $g$
- D) $h$ es simplemente $f$ reducido módulo $p$

**Respuesta correcta:** A

**Retroalimentación:** La clave pública se calcula como $h = p \cdot (f^{-1}_q \cdot g) \bmod q$, mezclando la inversa de $f$ módulo $q$ con $g$.

### 6. ¿Qué función cumple el polinomio aleatorio $r$ al cifrar un mensaje en NTRU?

- A) Ninguna; es un parámetro opcional que puede omitirse
- B) Hace que dos cifrados del mismo mensaje resulten distintos entre sí
- C) Sustituye por completo a la clave pública $h$
- D) Actúa como la clave privada temporal del receptor

**Respuesta correcta:** B

**Retroalimentación:** El polinomio aleatorio $r$ introduce aleatoriedad en cada cifrado, de forma que cifrar el mismo mensaje dos veces produce ciphertexts distintos.

### 7. ¿Por qué es necesario "centrar" los coeficientes antes de reducir módulo $p$ durante el descifrado?

- A) Es solo una cuestión estética sin efecto en el resultado
- B) Porque un residuo grande módulo $q$ puede representar en realidad un número negativo pequeño
- C) Para acelerar el cálculo computacional
- D) Para introducir más aleatoriedad en el mensaje recuperado

**Respuesta correcta:** B

**Retroalimentación:** Sin centrar, un valor módulo $q$ podría interpretarse erróneamente como un número grande y positivo cuando en realidad representa un número pequeño y negativo, impidiendo recuperar el mensaje correctamente.

### 8. En el ejemplo guiado de la sesión (con $N=4$, $p=3$, $q=17$), ¿qué vector se obtiene como clave pública $h$?

- A) $h = [1,0,0,0]$
- B) $h = [11,7,9,7]$
- C) $h = [9,10,1,14]$
- D) $h = [1,0,2,0]$

**Respuesta correcta:** C

**Retroalimentación:** El documento indica explícitamente `h == [9, 10, 1, 14]`. El vector `[11,7,9,7]` corresponde al ciphertext $c$, y `[1,0,2,0]` es el mensaje recuperado tras el descifrado.

### 9. ¿Por qué el término que contiene $g$ desaparece al reducir módulo $p$ durante el descifrado?

- A) Porque $g$ se elimina explícitamente antes de cifrar el mensaje
- B) Porque ese término contiene el factor $p$, por lo que todos sus coeficientes son cero módulo $p$
- C) Porque $f$ y $g$ son polinomios idénticos
- D) Porque el mensaje se cancela directamente con el polinomio aleatorio $r$

**Respuesta correcta:** B

**Retroalimentación:** La clave pública $h$ incluye un factor $p$ multiplicando a $g$; por eso, al reducir módulo $p$, ese término se anula y solo queda la parte relacionada con el mensaje.

### 10. Según la sesión, ¿cuál es el estado normativo de NTRU frente a ML-KEM?

- A) NTRU sustituyó oficialmente a ML-KEM como estándar NIST
- B) NTRU no fue seleccionado como estándar NIST; ML-KEM es el KEM principal estandarizado y NTRU tiene valor docente e histórico
- C) Ambos algoritmos son matemáticamente idénticos y intercambiables
- D) El NIST prohibió expresamente el uso de NTRU

**Respuesta correcta:** B

**Retroalimentación:** NTRU no fue seleccionado como estándar por el NIST. Sigue disponible en implementaciones como liboqs con valor docente e histórico, pero ML-KEM es el KEM principal estandarizado (FIPS 203).
