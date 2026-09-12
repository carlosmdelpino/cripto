# Test de conocimientos. Clase 3: Introducción a la computación cuántica

## Instrucciones

Cada pregunta tiene cuatro opciones de respuesta, de las cuales solo una es correcta. Debajo de cada pregunta se indica la respuesta correcta y una breve retroalimentación con la explicación.

## Preguntas

### 1. ¿Cómo se representa el estado de un qubit $|\psi\rangle$?

- A) $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$, con $|\alpha|^2+|\beta|^2=1$
- B) $|\psi\rangle = \alpha + \beta$, sin ninguna restricción
- C) $|\psi\rangle$ solo puede valer 0 o 1, igual que un bit clásico
- D) $|\psi\rangle = \alpha \times \beta \times 2$

**Respuesta correcta:** A

**Retroalimentación:** Un qubit puede existir en una combinación (superposición) de $|0\rangle$ y $|1\rangle$, con coeficientes $\alpha$ y $\beta$ cuyas probabilidades al cuadrado suman 1.

### 2. Al aplicar la puerta Hadamard $H$ sobre el estado $|0\rangle$, ¿qué se obtiene?

- A) El estado $|1\rangle$ con probabilidad 1
- B) Una superposición con $P(0)=P(1)=0{,}5$
- C) El estado se destruye y no puede medirse
- D) Un estado entrelazado con otro qubit inexistente

**Respuesta correcta:** B

**Retroalimentación:** $H|0\rangle = \tfrac{1}{\sqrt2}(|0\rangle+|1\rangle)$, es decir, una superposición donde medir da 0 o 1 con la misma probabilidad, 0,5 cada uno.

### 3. Sobre el entrelazamiento cuántico (por ejemplo, el estado de Bell), ¿cuál de las siguientes afirmaciones es correcta?

- A) Permite enviar información más rápido que la luz
- B) Al medir un qubit, el resultado del otro queda determinado al instante, pero esto no permite comunicación más rápida que la luz
- C) Solo puede darse entre qubits situados en el mismo laboratorio físico
- D) Es equivalente a copiar exactamente el estado de un qubit en otro

**Respuesta correcta:** B

**Retroalimentación:** El entrelazamiento correlaciona los resultados de medición de ambos qubits, pero no constituye un canal de comunicación ni viola la relatividad.

### 4. ¿Qué establece el teorema de no clonación?

- A) Que no se puede copiar exactamente un estado cuántico desconocido
- B) Que un qubit no puede medirse nunca
- C) Que dos qubits nunca pueden entrelazarse
- D) Que las puertas cuánticas no pueden encadenarse en un circuito

**Respuesta correcta:** A

**Retroalimentación:** El teorema de no clonación impide crear una copia exacta de un estado cuántico desconocido, a diferencia de los bits clásicos, que se copian trivialmente.

### 5. ¿Qué ventaja ofrece el algoritmo de Grover frente a una búsqueda clásica en una lista desordenada de $N$ elementos?

- A) Resuelve el problema en tiempo constante, sin depender de $N$
- B) Reduce la complejidad de $O(N)$ a $O(\sqrt{N})$: una aceleración cuadrática
- C) Solo funciona si $N$ es un número primo
- D) Rompe RSA y ECC directamente, igual que Shor

**Respuesta correcta:** B

**Retroalimentación:** Grover ofrece una aceleración cuadrática ($O(\sqrt{N})$ frente a $O(N)$). Aplicado a una clave de $n$ bits, reduce el esfuerzo de $2^n$ a $2^{n/2}$, por lo que debilita AES y las funciones hash sin llegar a romperlos.

### 6. ¿Qué logra el algoritmo de Shor que representa una amenaza directa para RSA, ECC y Diffie-Hellman?

- A) Debilita la longitud de clave, obligando a usar el doble de bits
- B) Resuelve en tiempo polinómico la factorización de enteros y el logaritmo discreto
- C) Permite clonar exactamente cualquier estado cuántico
- D) Genera automáticamente nuevas claves privadas

**Respuesta correcta:** B

**Retroalimentación:** Shor resuelve en tiempo polinómico problemas que son intratables para un ordenador clásico (factorización y logaritmo discreto), rompiendo por completo RSA, ECC y Diffie-Hellman.

### 7. En la idea matemática del algoritmo de Shor, ¿qué se busca al factorizar $N = p \times q$?

- A) El máximo común divisor entre $p$ y $q$ directamente
- B) El periodo $r$ de la función $f(x) = a^x \bmod N$
- C) La raíz cuadrada exacta de $N$
- D) El valor de $\varphi(N)$ sin usar ningún otro cálculo

**Respuesta correcta:** B

**Retroalimentación:** Shor reduce la factorización a encontrar el periodo $r$ de $f(x)=a^x \bmod N$; con ese periodo se pueden calcular factores no triviales de $N$ mediante el máximo común divisor.

### 8. En el ejemplo numérico de la sesión con $N=15$ y $a=7$, ¿qué periodo $r$ se obtiene y qué factores de 15 se calculan?

- A) $r=2$; factores 1 y 15
- B) $r=3$; factores 5 y 3 obtenidos por resta directa
- C) $r=4$; factores 3 y 5
- D) $r=8$; factores 7 y 15

**Respuesta correcta:** C

**Retroalimentación:** $7^4 \bmod 15 = 1$, por lo que $r=4$ (par). Con $a^{r/2}=7^2 \bmod 15=4$, se obtiene $p=\gcd(3,15)=3$ y $q=\gcd(5,15)=5$, y $15=3\times5$.

### 9. Según el impacto descrito en la sesión, ¿qué ocurre con AES y con las funciones hash frente a un ordenador cuántico con Grover?

- A) Se rompen igual que RSA y ECC
- B) No se ven afectados en absoluto
- C) Se debilitan (por ejemplo, AES-128 equivale a 64 bits efectivos), pero no se rompen; se recomienda usar claves o salidas más largas
- D) Dejan de ser deterministas

**Respuesta correcta:** C

**Retroalimentación:** A diferencia de RSA/ECC (rotos por Shor), AES y las funciones hash solo se debilitan frente a Grover; se compensa usando AES-256 o salidas hash de 384-512 bits.

### 10. ¿Cuál de las siguientes afirmaciones es un mito, según la sesión?

- A) Hoy no existe un ordenador cuántico capaz de romper RSA con claves reales
- B) El riesgo "harvest now, decrypt later" justifica planificar la migración ya
- C) Ya existen ordenadores cuánticos que rompen RSA en producción
- D) Grover ofrece una aceleración cuadrática, no exponencial

**Respuesta correcta:** C

**Retroalimentación:** Es un mito común: hoy no existen ordenadores cuánticos con suficientes qubits lógicos estables para ejecutar Shor contra claves reales, aunque el riesgo futuro ya obliga a planificar la migración a criptografía post-cuántica.
