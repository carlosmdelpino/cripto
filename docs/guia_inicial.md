# Guía inicial de trabajo

## Tema

Criptografía postcuántica.

## Objetivos

- Entender la amenaza cuántica sobre la criptografía clásica.
- Conocer los algoritmos más relevantes del estándar NIST.
- Construir una base de código para experimentar y documentar.

## Conceptos clave

### 1. ¿Qué es la computación cuántica?

Un ordenador cuántico usa qubits, que permiten aprovechar superposición y entrelazamiento para resolver ciertos problemas de forma más eficiente que los ordenadores clásicos.

### 2. ¿Por qué afecta a la criptografía?

El algoritmo de Shor puede factorizar números grandes y calcular logaritmos discretos eficientemente en un ordenador cuántico, lo que amenaza a RSA y ECC.

### 3. ¿Qué son los algoritmos postcuánticos?

Son esquemas diseñados para resistir ataques tanto clásicos como cuánticos. Los más relevantes son:

- Kyber: KEM.
- Dilithium: firma digital.
- Falcon: firma digital compacta.
- SPHINCS+: firma hash-based.

## Siguiente paso

Vamos a ir ampliando con:

- comparativa entre RSA/ECC y PQC,
- explicación de KEM vs firmas,
- ejemplo de generación de llaves o hashes,
- estudio del estándar NIST.
