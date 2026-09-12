# Índice de contenidos por sesión

## Asignatura
Introducción a la criptografía: de los fundamentos a la criptografía post-cuántica

## Sesión 1. Fundamentos de la criptografía

### 1. Introducción a la criptografía
- Definición y objetivos
- Confidencialidad, integridad, autenticación y no repudio
- Diferencia entre seguridad y criptografía

### 2. Conceptos básicos
- Mensaje, texto claro y texto cifrado
- Clave criptográfica
- Cifrado y descifrado
- Funciones hash
- Firma digital

### 3. Criptografía simétrica y asimétrica
- Principios de funcionamiento
- Ventajas y desventajas
- Casos de uso habituales

### 4. Fundamentos matemáticos básicos
- Congruencias
- Aritmética modular
- Números primos
- Logaritmos discretos

### 5. Ejemplos prácticos
- Envío seguro de un mensaje
- Verificación de integridad mediante hash
- Uso de claves públicas y privadas

### 6. Conclusiones
- Importancia de la criptografía en la seguridad digital

### 7. Bibliografía esencial
- Stallings, W. (Criptografía y seguridad de redes)
- Schneier, B. (Applied Cryptography)

---

## Sesión 2. Criptografía moderna y seguridad en Internet

### 1. Evolución histórica de la criptografía
- Criptografía clásica
- Criptografía moderna
- Cambios provocados por la informática

### 2. Sistemas criptográficos modernos
- RSA
- ECC (Elliptic Curve Cryptography)
- Diferencias entre seguridad y rendimiento

### 3. Seguridad en Internet
- HTTPS y TLS
- Autenticación de servidores y clientes
- Certificados digitales

### 4. Protocolos de seguridad
- SSL/TLS
- SSH
- VPN y comunicaciones seguras

### 5. Aplicaciones reales
- Comercio electrónico
- Bancos y servicios financieros
- Redes sociales y plataformas digitales

### 6. Ejercicios prácticos
- Comparación RSA vs ECC
- Análisis de un certificado digital
- Estudio de un canal seguro

### 7. Conclusiones
- La seguridad en Internet depende de mecanismos criptográficos robustos

### 8. Bibliografía esencial
- Stallings, W.
- Ferguson, N., Schneier, B. y Kohno, T.

---

## Sesión 3. Introducción a la computación cuántica

### 1. Conceptos básicos de mecánica cuántica
- Qubit
- Superposición
- Entrelazamiento
- Medición

### 2. Diferencia entre computación clásica y cuántica
- Modelo clásico
- Modelo cuántico
- Ventajas teóricas de la computación cuántica

### 3. Algoritmos cuánticos relevantes
- Algoritmo de Deutsch-Jozsa
- Algoritmo de Grover
- Algoritmo de Shor

### 4. Impacto de la computación cuántica en la criptografía
- Problemas que resuelve más eficientemente
- Amenaza a RSA y ECC
- Importancia de la investigación en seguridad post-cuántica

### 5. Ejemplos matemáticos y conceptuales
- Cambio de perspectiva computacional
- Simulación básica de operaciones cuánticas

### 6. Conclusiones
- La computación cuántica no solo cambia el cálculo, sino también la seguridad

### 7. Bibliografía esencial
- Nielsen, M. A. y Chuang, I. L.
- Preskill, J.

---

## Sesión 4. Criptografía post-cuántica: introducción. Métodos de criptografía post-cuántica (II)

### 1. Introducción y amenaza cuántica
- Qué significa criptografía post-cuántica
- Impacto de Shor sobre RSA, Diffie-Hellman y ECC
- Impacto cuadrático de Grover sobre la búsqueda exhaustiva
- Riesgo de «recoger ahora, descifrar después»

### 2. Familias de métodos
- Retículos
- Códigos correctores
- Firmas basadas en hash
- Otras líneas de investigación

### 3. Método principal: ML-KEM / Kyber
- Qué hace un KEM y qué datos son públicos o secretos
- Base matemática de LWE y Module-LWE
- Generación de claves, encapsulación y desencapsulación
- Derivación de una clave simétrica

### 4. Ejemplo y ejercicios
- Cálculo completo de una muestra LWE pequeña
- Encapsulación didáctica de un bit
- Ejercicios resueltos de cálculo y razonamiento

### 5. Python y proyecto real
- ML-KEM con una implementación existente
- Derivación con HKDF y cifrado con AES-GCM
- Estructura de un sobre híbrido y gestión de claves

### 6. Fuentes esenciales
- NIST FIPS 203
- NIST SP 800-227
- Open Quantum Safe / liboqs-python

---

## Sesión 5. Métodos de criptografía post-cuántica (II)

### 1. Método principal: NTRU
- Idea de retículo expresada mediante polinomios cortos
- Papel de la clave privada y del polinomio aleatorio
- Diferencia entre ejemplo didáctico y parámetros seguros

### 2. Base matemática
- Anillos de polinomios y reducción por $x^N - 1$
- Convolución circular
- Coeficientes módulo $p$ y módulo $q$
- Inversos de polinomios

### 3. NTRU paso a paso
- Generación de claves $f$, $g$ y $h$
- Cifrado con aleatoriedad
- Centrado de coeficientes
- Descifrado con la inversa de $f$

### 4. Ejemplo y ejercicios
- Ejemplo completo con $N = 4$, $p = 3$ y $q = 17$
- Cálculo de clave pública, ciphertext y mensaje recuperado
- Ejercicios resueltos de convolución, cifrado y centrado

### 5. Python y proyecto real
- Implementación didáctica completa de la convolución y el descifrado
- Uso experimental de NTRU mediante liboqs
- Posición actual de NTRU frente al estándar ML-KEM

### 6. Fuentes esenciales
- Hoffstein, Pipher y Silverman
- NTRU Round 3 Submission Package
- NIST PQC Standardization Project

---

## Sesión 6. Métodos de criptografía post-cuántica (III). Estado actual

### 1. Firmas post-cuánticas
- Diferencia entre firma, KEM y cifrado autenticado
- Autenticidad, integridad y verificación pública

### 2. Método 1: ML-DSA / Dilithium
- Retículos y clave pública con ruido
- Reto-respuesta y transformación Fiat-Shamir
- Muestreo por rechazo
- Ejemplo y ejercicios resueltos de verificación

### 3. Método 2: SLH-DSA / SPHINCS+
- Firmas de un solo uso y árboles de Merkle
- Camino de autenticación y raíz pública
- Ejemplo y ejercicios resueltos con un árbol pequeño

### 4. Python y proyecto real
- Firma de JSON canónico con implementaciones existentes
- Verificación de ML-DSA y SLH-DSA
- Formato del sobre firmado y protección de la clave privada

### 5. Estado actual a 12 de septiembre de 2026
- FIPS 203, 204 y 205 como estándares finales
- FN-DSA / FIPS 206 y HQC-KEM / FIPS 207 en desarrollo
- Tercera ronda de firmas adicionales de NIST
- Inventario criptográfico, protocolos híbridos y criptoagilidad

### 6. Ejercicio final
- Plan de migración de una API con ECDH y ECDSA
- Criterios para elegir entre ML-DSA y SLH-DSA

### 7. Fuentes esenciales
- NIST FIPS 204 y FIPS 205
- NIST IR 8545 e IR 8610
- NIST SP 800-227 y guía de criptoagilidad

---
