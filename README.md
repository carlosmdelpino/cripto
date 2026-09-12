# Criptografía Postcuántica

Material docente para la asignatura **"Introducción a la criptografía: de los fundamentos a la criptografía post-cuántica"**: documentación de clase, notebooks, presentaciones y documentos Word para 6 sesiones, además de un pequeño módulo Python de apoyo conceptual.

## Programa de la asignatura

El contenido está organizado en 6 sesiones (ver el índice completo en [01_documentacion/02_clases/01_indice_sesiones/indice_sesiones.md](01_documentacion/02_clases/01_indice_sesiones/indice_sesiones.md)):

| # | Sesión | Contenido principal | Estado de los entregables |
|---|---|---|---|
| 1 | Fundamentos de la criptografía | Confidencialidad/integridad/autenticación, primitivas (cifrado, hash, MAC, firma), simétrica vs asimétrica, aritmética modular | ✅ md, docx, pptx, notebook |
| 2 | Criptografía asimétrica y seguridad en Internet | RSA, ECC, Diffie-Hellman, TLS/HTTPS, certificados y PKI | ✅ md, docx, pptx, notebook (incluye ruptura de un LFSR) |
| 3 | Introducción a la computación cuántica | Qubits, superposición, entrelazamiento, puertas cuánticas, Deutsch-Jozsa, Grover y Shor (con ejemplo numérico de factorización) | ✅ md, docx, pptx — versión condensada para clase de 30 min |
| 4 | Criptografía post-cuántica: introducción y ML-KEM/Kyber | Amenaza cuántica, familias PQC, LWE/Module-LWE, ML-KEM (FIPS 203) | ⚠️ docx (versión completa + versión simple). Falta md, pptx y notebook |
| 5 | Métodos post-cuánticos (II): NTRU | Anillos de polinomios, convolución, cifrado/descifrado NTRU paso a paso | ⚠️ docx (versión completa + versión simple). Falta md, pptx y notebook |
| 6 | Métodos post-cuánticos (III): firmas y estado actual | ML-DSA/Dilithium, SLH-DSA/SPHINCS+, estándares NIST FIPS 204/205/206/207, criptoagilidad | ⚠️ docx (versión completa + versión simple). Falta md, pptx y notebook |

**Leyenda:** ✅ completo · ⚠️ en progreso.

## Estructura del repositorio

```
01_documentacion/       Contenido docente en Markdown (fuente de verdad de cada sesión)
├── 01_presentacion/    (vacío, reservado)
└── 02_clases/          Índice de sesiones + sesion_1/2/3_*.md
02_multimedia/          Imágenes, diagramas y bibliografía de apoyo (en preparación)
03_recursos/            Recursos adicionales de presentación/clase (en preparación)
04_plantillas/          Plantillas para documento de clase, caso práctico y test (en preparación)
05_entregables/         Entregables generados a partir de la documentación
├── 01_notebooks/       Jupyter notebooks por sesión (sesiones 1 y 2)
├── 02_word/            Documentos Word finales por sesión (sesiones 1-6)
├── 02_word_original/   Copias de seguridad de versiones anteriores de algunos Word
├── 03_practicas/       Prácticas por unidad (unidad_1: enunciado, notebook, resumen)
├── 03_resumenes/       Resúmenes por clase (en preparación)
├── 04_casos/           Casos prácticos con enunciado y solución (en preparación)
├── 04_tests/           Tests de evaluación por unidad (unidad_1 disponible)
├── 05_evaluacion/      Evaluación y tests de la asignatura (en preparación)
└── 06_presentaciones/  Presentaciones PowerPoint por sesión (sesiones 1-3)
docs/                   Guía inicial de trabajo
examples/               Script de demostración (basic_demo.py)
scripts/                Generadores Python de los Word/PowerPoint a partir del contenido
src/pqc/                Módulo Python con utilidades y conceptos básicos de PQC
```

Cada carpeta de `05_entregables/` y `01_documentacion/` tiene su propio `README.md` con el detalle de la estructura prevista.

## Cómo se generan los entregables

El contenido de cada sesión se redacta primero en Markdown (`01_documentacion/02_clases/sesion_N_*.md`) y después se transcribe a un script Python que genera el Word y/o PowerPoint correspondiente con `python-docx` / `python-pptx`, evitando mantener el contenido duplicado a mano:

| Script | Genera |
|---|---|
| `scripts/generate_session1_word.py` / `generate_session1_presentation.py` | Word y PPTX de la Sesión 1 |
| `scripts/generate_session2_word.py` / `generate_session2_presentation.py` | Word y PPTX de la Sesión 2 |
| `scripts/generate_session3_word.py` / `generate_session3_presentation.py` | Word y PPTX de la Sesión 3 (versión de 30 min) |
| `scripts/generate_sessions_4_6_word.py` | Word completo de las Sesiones 4, 5 y 6 |
| `scripts/generate_sessions_4_6_simple_word.py` | Versión simplificada del Word de las Sesiones 4, 5 y 6 |
| `scripts/generate_unit1_materials.py` | Materiales de la práctica y el test de la Unidad 1 |

Para regenerar un entregable, ejecuta el script correspondiente desde la raíz del repositorio, por ejemplo:

```powershell
py -3 scripts\generate_session3_word.py
py -3 scripts\generate_session3_presentation.py
```

## Código base en Python (`src/pqc`)

Módulo mínimo de apoyo conceptual, sin dependencias externas de PQC reales:

- `ALGORITHMS`: descripción breve de Kyber, Dilithium, Falcon y SPHINCS+.
- `SECURITY_LEVELS`: equivalencia de los niveles NIST (1/3/5) con bits de seguridad clásica.
- `compare_security()`: puntos clave sobre la amenaza cuántica.
- `hash_bytes()` / `generate_demo_seed()`: utilidades de hashing para ejemplos didácticos.

Demo de uso:

```bash
python examples/basic_demo.py
```

## Requisitos e instalación

- Python 3.10+
- Dependencias en `requirements.txt` (`cryptography`, `python-docx`, `python-pptx`)

```powershell
pip install -r requirements.txt
```

Para ejecutar y validar los notebooks (`.ipynb`) se recomienda además tener `jupyter`/`nbconvert` instalado.

## Pendiente / próximos pasos

- Redactar el `.md` fuente y generar `pptx`/notebook de las Sesiones 4, 5 y 6.
- Completar `03_resumenes/`, `04_casos/` y `05_evaluacion/` (por ahora solo contienen el `README.md` de estructura prevista).
- Revisar y, si procede, retirar las copias de `05_entregables/02_word_original/` una vez confirmado que ya no son necesarias.
