# Práctica de la Unidad 1: Fundamentos de la criptografía

## 1. Objetivo de la práctica

La práctica tiene como finalidad que el alumnado comprenda los conceptos básicos de la criptografía y aplique algunos de ellos mediante programación en Python. Se pretende conectar la teoría con la práctica mediante la realización de cálculos simples, la comprobación de integridad mediante hashes y la reflexión sobre la seguridad de la información.

## 2. Descripción general

Durante la práctica, el alumno deberá:

- identificar los objetivos de seguridad de la información;
- diferenciar entre criptografía simétrica y asimétrica;
- aplicar operaciones de aritmética modular;
- calcular funciones hash con Python;
- analizar la relación entre integridad y autenticación;
- redactar conclusiones sobre la utilidad de la criptografía en sistemas reales.

## 3. Enunciado

Una empresa de servicios digitales desea proteger un conjunto de mensajes internos y verificar que los archivos enviados a sus clientes no hayan sido alterados durante la transmisión. El equipo de seguridad propone utilizar conceptos fundamentales de la criptografía para garantizar la confidencialidad e integridad de la información.

Se pide:

1. Explicar qué objetivo de seguridad se está priorizando en cada caso.
2. Diferenciar si el problema se resuelve mejor con criptografía simétrica o asimétrica.
3. Aplicar una operación modular simple a un valor concreto.
4. Calcular un hash SHA-256 de un texto de ejemplo.
5. Comentar qué ocurre si se modifica un carácter del mensaje original.
6. Redactar una conclusión final sobre la relación entre seguridad, integridad y autenticación.

## 4. Tareas a realizar

### Tarea 1. Identificación de objetivos de seguridad

Responde a las siguientes preguntas:

- ¿Qué es la confidencialidad?
- ¿Qué es la integridad?
- ¿Qué es la autenticación?
- ¿Qué es el no repudio?

Explica cómo se relacionan entre sí y cuáles son los más relevantes para el caso planteado.

### Tarea 2. Cálculo modular

Realiza el siguiente cálculo en Python:

- 23 mod 7
- 29 mod 10
- 43 mod 5

Indica el resultado y explica qué significa que dos valores sean congruentes módulo n.

### Tarea 3. Función hash

Utiliza Python para calcular el hash SHA-256 de la cadena:

`mensaje_secreto`

A continuación, responde:

- ¿Qué salida obtienes?
- ¿Qué propiedad de seguridad demuestra este cálculo?
- ¿Qué ocurre si cambias una letra del texto original?

### Tarea 4. Comparación de modelos criptográficos

Explica brevemente la diferencia entre:

- criptografía simétrica;
- criptografía asimétrica;
- criptografía híbrida.

Indica cuál de ellas es más adecuada para:

- cifrar un archivo muy grande;
- enviar una clave secreta de forma segura;
- firmar un contrato digital.

### Tarea 5. Reflexión aplicada

Escribe una pequeña reflexión de 150 a 250 palabras sobre la importancia de la criptografía en aplicaciones cotidianas como:

- banca online;
- correo electrónico;
- acceso a plataformas;
- firma de documentos digitales.

## 5. Requisitos mínimos de entrega

El alumno deberá entregar:

- un notebook con el desarrollo de la práctica;
- una explicación escrita de cada apartado;
- los resultados de los cálculos realizados;
- una conclusión final con tres ideas principales;
- una presentación breve de 5 minutos sobre la práctica en clase.

## 6. Criterios de evaluación

Se valorará:

- claridad conceptual;
- uso correcto de Python;
- rigor en los razonamientos matemáticos;
- capacidad de relacionar teoría y aplicaciones reales;
- calidad de la redacción y de la conclusión final.

## 7. Bibliografía básica

- Stallings, W. *Cryptography and Network Security: Principles and Practice*. Pearson.
- Katz, J. y Lindell, Y. *Introduction to Modern Cryptography*. Chapman & Hall/CRC.
- Schneier, B. *Applied Cryptography*. Wiley.

## 8. Fecha de referencia

XX-YY-ZZZZ
