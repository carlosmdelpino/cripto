"""Funciones y conceptos básicos para estudiar criptografía postcuántica."""

from __future__ import annotations

from hashlib import sha256
from typing import Dict, List

SECURITY_LEVELS: Dict[str, str] = {
    "NIST Level 1": "equivalente a 128 bits de seguridad clásica",
    "NIST Level 3": "equivalente a 192 bits de seguridad clásica",
    "NIST Level 5": "equivalente a 256 bits de seguridad clásica",
}

ALGORITHMS: Dict[str, str] = {
    "Kyber": "KEM basado en retículos",
    "Dilithium": "firma digital basada en retículos",
    "Falcon": "firma digital compacta basada en retículos",
    "SPHINCS+": "firma digital hash-based",
}


def compare_security() -> List[str]:
    """Devuelve una comparación breve entre seguridad clásica y postcuántica."""
    return [
        "La criptografía clásica depende de problemas como factorización y logaritmo discreto.",
        "La computación cuántica puede romper algunos de esos supuestos con algoritmos como Shor.",
        "Los algoritmos postcuánticos buscan resistencia frente a ataques con computadores cuánticos.",
    ]


def hash_bytes(data: bytes) -> str:
    """Genera un resumen SHA-256 de una entrada en bytes."""
    return sha256(data).hexdigest()


def generate_demo_seed(label: str, salt: bytes = b"") -> str:
    """Genera una semilla demostrativa para experimentos educativos."""
    payload = label.encode("utf-8") + salt
    return sha256(payload).hexdigest()
