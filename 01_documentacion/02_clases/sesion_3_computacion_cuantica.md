# Sesión 3. Introducción a la computación cuántica

*Qubits, superposición, entrelazamiento y el impacto cuántico sobre la criptografía actual*

*(Versión reducida — sesión de 30 minutos)*

## Índice

- [1. Introducción y objetivos](#1-introducción-y-objetivos)
- [2. Qubits y superposición](#2-qubits-y-superposición)
- [3. Entrelazamiento y medición](#3-entrelazamiento-y-medición)
- [4. Puertas cuánticas y circuitos básicos](#4-puertas-cuánticas-y-circuitos-básicos)
- [5. Computación clásica frente a computación cuántica](#5-computación-clásica-frente-a-computación-cuántica)
- [6. De Deutsch-Jozsa a Grover](#6-de-deutsch-jozsa-a-grover)
- [7. El algoritmo de Shor](#7-el-algoritmo-de-shor)
- [8. Impacto en la criptografía actual](#8-impacto-en-la-criptografía-actual)
- [9. Mitos y errores comunes](#9-mitos-y-errores-comunes)
- [10. Conclusiones y hacia la criptografía post-cuántica](#10-conclusiones-y-hacia-la-criptografía-post-cuántica)
- [11. Bibliografía y preguntas de reflexión](#11-bibliografía-y-preguntas-de-reflexión)

---

## 1. Introducción y objetivos

En las sesiones anteriores vimos que la seguridad de RSA y ECC depende de problemas matemáticos difíciles **para un ordenador clásico**: factorizar números grandes y calcular logaritmos discretos. La computación cuántica es un modelo de cálculo distinto, basado en la mecánica cuántica, que resuelve estos problemas de forma radicalmente más eficiente, y por eso amenaza directamente a la criptografía actual.

Al finalizar esta sesión el estudiante podrá:

- explicar qué es un qubit y las nociones de superposición, entrelazamiento y medición;
- identificar las puertas cuánticas básicas y su función en un circuito;
- explicar con detalle matemático cómo el algoritmo de Shor rompe RSA y ECC;
- entender por qué la criptografía simétrica y el hash se debilitan (no se rompen) frente a Grover;
- situar esta amenaza en el camino hacia la criptografía post-cuántica.

---

## 2. Qubits y superposición

Un bit clásico vale 0 o 1. Un **qubit** se representa como:

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \qquad |\alpha|^2 + |\beta|^2 = 1
$$

Puede existir en una combinación de $|0\rangle$ y $|1\rangle$ a la vez: la **superposición**. Por ejemplo, la puerta Hadamard sobre $|0\rangle$ produce:

$$
H|0\rangle = \tfrac{1}{\sqrt{2}}\big(|0\rangle + |1\rangle\big) \;\Rightarrow\; P(0) = P(1) = 0.5
$$

Con $n$ qubits se pueden representar hasta $2^n$ combinaciones a la vez, pero medir colapsa el resultado a uno solo: la ventaja cuántica está en diseñar la interferencia para que la respuesta correcta sea la más probable, no en "probar todo a la vez".

---

## 3. Entrelazamiento y medición

El **entrelazamiento** correlaciona dos o más qubits de forma que no pueden describirse por separado. El **estado de Bell**:

$$
|\Phi^+\rangle = \tfrac{1}{\sqrt{2}}\big(|00\rangle + |11\rangle\big)
$$

hace que, al medir un qubit, el resultado del otro quede determinado al instante, sin importar la distancia (aunque **no** permite comunicación más rápida que la luz).

**Medir** un qubit colapsa su estado de forma irreversible, con probabilidades $P(0)=|\alpha|^2$ y $P(1)=|\beta|^2$. El **teorema de no clonación** impide copiar exactamente un estado cuántico desconocido.

---

## 4. Puertas cuánticas y circuitos básicos

| Puerta | Efecto |
|---|---|
| X (NOT cuántico) | Invierte $\lvert0\rangle$ y $\lvert1\rangle$ |
| H (Hadamard) | Crea superposición |
| Z | Cambia la fase del estado $\lvert1\rangle$ |
| CNOT | Invierte el 2º qubit según el 1º (crea entrelazamiento) |

Un circuito cuántico encadena puertas y termina con una medición. Aplicar H y después CNOT sobre dos qubits genera el estado de Bell descrito arriba.

---

## 5. Computación clásica frente a computación cuántica

| Aspecto | Computación clásica | Computación cuántica |
|---|---|---|
| Unidad básica | Bit (0 o 1) | Qubit (superposición de 0 y 1) |
| Determinismo | Determinista | Probabilístico (la medición da un resultado con cierta probabilidad) |
| Copia de estados | Trivial | Prohibida por el teorema de no clonación |
| Ventaja principal | Universalidad y madurez tecnológica | Muy superior en problemas concretos (factorización, búsqueda) |

No es un "superordenador universal más rápido para todo": su ventaja se limita a problemas con una estructura matemática concreta.

---

## 6. De Deutsch-Jozsa a Grover

- **Deutsch-Jozsa (1992)**: distingue si una función $f(x)$ es constante o equilibrada con una única evaluación, mientras que un algoritmo clásico determinista podría necesitar varias. Su relevancia es más histórica/conceptual que práctica.
- **Grover (1996)**: búsqueda en una lista desordenada de $N$ elementos con complejidad $O(\sqrt{N})$, frente a $O(N)$ en el caso clásico (**aceleración cuadrática**). Aplicado a una clave de $n$ bits, reduce el esfuerzo de $2^n$ a $2^{n/2}$: por eso amenaza a AES y a las funciones hash, sin llegar a romperlos.

---

## 7. El algoritmo de Shor

El algoritmo de Shor (1994) es el más relevante para la criptografía: resuelve en **tiempo polinómico** la factorización de enteros y el logaritmo discreto (incluido en curvas elípticas), la base matemática de RSA, ECC y Diffie-Hellman.

**Idea matemática.** Factorizar $N = p \times q$ se reduce a encontrar el **periodo** $r$ de la función:

$$
f(x) = a^x \bmod N, \qquad \text{con } 1 < a < N,\ \gcd(a, N) = 1
$$

es decir, el menor $r>0$ tal que $a^r \equiv 1 \pmod{N}$. Si $r$ es par y $a^{r/2} \not\equiv -1 \pmod{N}$, entonces:

$$
a^r - 1 = \big(a^{r/2}-1\big)\big(a^{r/2}+1\big) \equiv 0 \pmod{N}
$$

por lo que $p=\gcd(a^{r/2}-1,\, N)$ y $q=\gcd(a^{r/2}+1,\, N)$ son factores no triviales de $N$.

**Pasos del algoritmo:**

1. Elegir $a$ aleatorio, $1<a<N$, con $\gcd(a,N)=1$.
2. *(Parte cuántica)* Calcular el periodo $r$ de $f(x)=a^x \bmod N$ mediante superposición y la transformada cuántica de Fourier, en tiempo polinómico — un ordenador clásico necesitaría un esfuerzo exponencial para el mismo cálculo.
3. Si $r$ es impar o $a^{r/2}\equiv -1 \pmod{N}$, repetir con otro $a$.
4. Si no, calcular $p=\gcd(a^{r/2}-1, N)$ y $q=\gcd(a^{r/2}+1, N)$: son los factores de $N$.

**Ejemplo numérico con $N=15$, $a=7$:**

| $x$ | $7^x \bmod 15$ |
|---|---|
| 1 | 7 |
| 2 | 4 |
| 3 | 13 |
| 4 | **1** ← periodo $r=4$ (par) |

$$
a^{r/2} = 7^2 \bmod 15 = 4 \qquad (4 \ne 14 \equiv -1 \pmod{15},\ \text{cumple la condición})
$$

$$
p = \gcd(4-1,\,15) = \gcd(3,15) = 3 \qquad q = \gcd(4+1,\,15) = \gcd(5,15) = 5
$$

$$
15 = 3 \times 5
$$

Con $N=15$ este cálculo también es viable a mano; la ventaja cuántica aparece cuando $N$ tiene cientos de dígitos (como en una clave RSA real): encontrar $r$ de forma clásica es inviable, pero el algoritmo cuántico lo hace en tiempo polinómico.

> Nota: hoy no existe un ordenador cuántico con suficientes qubits estables para ejecutar Shor contra claves reales, pero el riesgo ("harvest now, decrypt later": guardar tráfico cifrado hoy para descifrarlo en el futuro) ya obliga a planificar la migración.

---

## 8. Impacto en la criptografía actual

| Algoritmo | Base matemática | Efecto cuántico |
|---|---|---|
| RSA | Factorización de enteros | Roto por Shor (tiempo polinómico) |
| ECC / Diffie-Hellman | Logaritmo discreto | Roto por Shor (tiempo polinómico) |
| AES | Confusión y difusión | Debilitado por Grover (128→64 bits efectivos); usar AES-256 |
| SHA-256 / SHA-3 | Funciones hash | Debilitado por Grover; usar salidas de 384-512 bits |

En resumen: la criptografía asimétrica clásica (RSA, ECC, Diffie-Hellman) se rompe por completo; la simétrica y el hash se debilitan pero no se rompen, ajustando el tamaño de clave.

---

## 9. Mitos y errores comunes

- **"Prueban todas las soluciones a la vez"**: la medición colapsa a un único resultado; la ventaja viene de la interferencia, no de "probarlo todo".
- **"El entrelazamiento permite comunicación instantánea"**: genera correlaciones, no un canal de comunicación.
- **"Ya existen ordenadores cuánticos que rompen RSA"**: no, aún no existen con suficientes qubits lógicos estables.
- **"Hace obsoleta toda la criptografía"**: solo la basada en factorización/logaritmo discreto; la simétrica y el hash se ajustan aumentando el tamaño de clave.

---

## 10. Conclusiones y hacia la criptografía post-cuántica

La computación cuántica es un modelo de cálculo distinto: Shor rompe RSA/ECC/Diffie-Hellman en tiempo polinómico, mientras que Grover debilita (sin romper) AES y las funciones hash. Aunque hoy no existe un ordenador cuántico capaz de ejecutar Shor contra claves reales, el riesgo a medio/largo plazo y el "harvest now, decrypt later" justifican empezar ya la migración hacia la **criptografía post-cuántica (PQC)**: algoritmos basados en retículos, códigos correctores de errores o funciones hash, actualmente en proceso de estandarización por el NIST, que se estudiarán en las próximas sesiones.

---

## 11. Bibliografía y preguntas de reflexión

**Bibliografía**

- Nielsen, M. A. y Chuang, I. L. *Quantum Computation and Quantum Information*. Cambridge University Press.
- Shor, P. W. *Algorithms for quantum computation: discrete logarithms and factoring*. Proceedings of the 35th Annual Symposium on Foundations of Computer Science, 1994.
- Grover, L. K. *A fast quantum mechanical algorithm for database search*. STOC, 1996.
- National Institute of Standards and Technology (NIST). Documentación del proceso de estandarización de criptografía post-cuántica.

**Preguntas de reflexión**

1. ¿Por qué encontrar el periodo $r$ de $a^x \bmod N$ permite factorizar $N$?
2. ¿Por qué el algoritmo de Shor rompe RSA/ECC mientras que Grover solo debilita AES?
3. ¿Por qué el riesgo cuántico afecta hoy a datos cifrados aunque el ataque solo sea viable en el futuro?
