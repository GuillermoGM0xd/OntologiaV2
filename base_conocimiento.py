"""
Estructuras utilizadas:
  - Diccionarios : individuo -> conjunto de predicados verdaderos (HECHOS)
  - Tuplas       : vínculos (sujeto, relación, objeto) y reglas
"""

# ==========
# PREDICADOS
# ==========
PREDICADOS_BASE = {
    # Notas de la bióloga
    "TienePelo": "x tiene pelo",
    "DaLeche": "x da leche a sus crías",
    "TienePlumas": "x tiene plumas",
    "Vuela": "x vuela",
    "PoneHuevos": "x pone huevos",
    "ComeCarne": "x come carne",
    "TienePezunas": "x tiene pezuñas",
    "ColorLeonado": "x es de color leonado",
    "TieneManchas": "x tiene manchas oscuras",
    "TieneRayas": "x tiene rayas negras",
    "CuelloLargo": "x tiene el cuello largo",
    "Nada": "x nada",
    "BlancoYNegro": "x es de color blanco y negro",
    "VuelaMuyBien": "x vuela muy bien",
    # Entrevistas
    "TamanoPequeno": "x es de tamaño pequeño",
    "MechonesEnOrejas": "x tiene mechones de pelo en las orejas",
    "ViveConHumanos": "x vive con humanos",
    "ViveEnEstadoSalvaje": "x vive en estado salvaje",
    "TieneHocicoGrande": "x tiene hocico grande",
    "VidaSalvajeEnManada": "x vive en manada en estado salvaje",
}

PREDICADOS_DERIVADOS = {
    "Mamifero": "x es un mamífero",
    "Ave": "x es un ave",
    "Carnivoro": "x es carnívoro",
    "Ungulado": "x es ungulado",
    "Guepardo": "x es un guepardo",
    "Tigre": "x es un tigre",
    "Jirafa": "x es una jirafa",
    "Cebra": "x es una cebra",
    "Pinguino": "x es un pingüino",
    "Albatros": "x es un albatros",
    "Gato": "x es un gato",
    "Caracal": "x es un caracal",
    "Perro": "x es un perro",
    "Lobo": "x es un lobo",
}

# ======
# HECHOS 
# ======
HECHOS = {
    # --- Entrevista 1 ---
    "miGato": {
        "TienePelo",          # pelaje que varía
        "ComeCarne",          # felino
        "TamanoPequeno",
        "ViveConHumanos",     # vive mayormente domesticado
        # No tiene alas, no pone huevos, no tiene mechones en las orejas
    },
    "elCaracal": {
        "TienePelo",
        "ComeCarne",          # felino
        "TamanoPequeno",      # tamaño parecido al del gato
        "MechonesEnOrejas",   # mechones negros en la punta de las orejas
        "ViveEnEstadoSalvaje",
    },
    # --- Entrevista 2 ---
    "miPerro": {
        "TienePelo",
        "DaLeche",            # mamífero porque da leche y no pone huevos
        "ComeCarne",
        "ViveConHumanos",     # doméstico
    },
    "elLobo": {
        "TienePelo",
        "DaLeche",
        "ComeCarne",
        "TieneHocicoGrande",
        "ViveEnEstadoSalvaje",
        "VidaSalvajeEnManada",
    },
    # --- Ejemplos de las notas de la bióloga ---
    "ejGuepardo": {"TienePelo", "ComeCarne", "ColorLeonado", "TieneManchas"},
    "ejTigre": {"TienePelo", "ComeCarne", "TieneRayas"},
    "ejJirafa": {"TienePelo", "TienePezunas", "CuelloLargo", "TieneManchas"},
    "ejCebra": {"TienePelo", "TienePezunas", "TieneRayas"},
    "ejPinguino": {"TienePlumas", "Nada", "BlancoYNegro"},
    "ejAlbatros": {"TienePlumas", "Vuela", "VuelaMuyBien", "PoneHuevos"},
}

# =================================================
# REGLAS  (tuplas: (id, [condiciones], conclusión))
# =================================================
REGLAS = [
    # --- Notas de la bióloga (reglas 1-12) ---
    (1,  ["TienePelo"], "Mamifero"),
    (2,  ["DaLeche"], "Mamifero"),
    (3,  ["TienePlumas"], "Ave"),
    (4,  ["Vuela", "PoneHuevos"], "Ave"),
    (5,  ["Mamifero", "ComeCarne"], "Carnivoro"),
    (6,  ["Mamifero", "TienePezunas"], "Ungulado"),
    (7,  ["Carnivoro", "ColorLeonado", "TieneManchas"], "Guepardo"),
    (8,  ["Carnivoro", "TieneRayas"], "Tigre"),
    (9,  ["Ungulado", "CuelloLargo", "TieneManchas"], "Jirafa"),
    (10, ["Ungulado", "TieneRayas"], "Cebra"),
    (11, ["Ave", "Nada", "BlancoYNegro"], "Pinguino"),
    (12, ["Ave", "VuelaMuyBien"], "Albatros"),
    # --- Entrevista 1 (reglas nuevas) ---
    (13, ["Carnivoro", "TamanoPequeno", "~MechonesEnOrejas"], "Gato"),
    (14, ["Carnivoro", "MechonesEnOrejas", "ViveEnEstadoSalvaje"], "Caracal"),
    # --- Entrevista 2 (reglas nuevas) ---
    (15, ["TieneHocicoGrande"], "Lobo"),
    (16, ["Carnivoro", "VidaSalvajeEnManada"], "Lobo"),
]

# ===============================================
# ONTOLOGÍA  (tuplas: (sujeto, relación, objeto))
# ===============================================
VINCULOS = [
    #Taxonomía (es_un)
    ("Mamifero", "es_un", "Animal"),
    ("Ave", "es_un", "Animal"),
    ("Carnivoro", "es_un", "Mamifero"),
    ("Ungulado", "es_un", "Mamifero"),
    ("Guepardo", "es_un", "Carnivoro"),
    ("Tigre", "es_un", "Carnivoro"),
    ("Gato", "es_un", "Carnivoro"),
    ("Caracal", "es_un", "Carnivoro"),
    ("Lobo", "es_un", "Carnivoro"),
    ("Perro", "es_un", "Mamifero"),
    ("Jirafa", "es_un", "Ungulado"),
    ("Cebra", "es_un", "Ungulado"),
    ("Pinguino", "es_un", "Ave"),
    ("Albatros", "es_un", "Ave"),
    #Instancias (instancia_de)
    ("miGato", "instancia_de", "Gato"),
    ("elCaracal", "instancia_de", "Caracal"),
    ("miPerro", "instancia_de", "Perro"),
    ("elLobo", "instancia_de", "Lobo"),
    #Confusiones entre especies
    ("Gato", "se_confunde_con", "Caracal"),
    ("Perro", "se_confunde_con", "Lobo"),
]

#Rasgo que permite distinguir cada par confundible
DISTINCION = {
    ("Gato", "Caracal"): {
        "Gato": ["TamanoPequeno", "orejas lisas", "ViveConHumanos"],
        "Caracal": ["MechonesEnOrejas", "orejas grandes",
                    "patas traseras largas y musculosas", "ViveEnEstadoSalvaje"],
        "observar": "Mechones negros en la punta de las orejas => Caracal; "
                    "patas traseras notablemente más largas => no es gato.",
    },
    ("Perro", "Lobo"): {
        "Perro": ["ViveConHumanos", "pelaje sin patrón fijo"],
        "Lobo": ["TieneHocicoGrande", "cráneo grande y firme",
                 "VidaSalvajeEnManada"],
        "observar": "Observar el hocico: el lobo lo tiene y el cráneo más "
                    "grande y firme.",
    },
}

#Sinónimos: predicados de las entrevistas que dependen de las especies
ESPECIES_DECLARADAS = {"miPerro": "Perro"}

# ===================================================
# MOTOR DE INFERENCIA (encadenamiento hacia adelante)
# ===================================================
def cumple(condicion, conocidos):
    """Evalúa una condición (con negación opcional '~') sobre los hechos."""
    if condicion.startswith("~"):
        return condicion[1:] not in conocidos
    return condicion in conocidos

def inferir(individuo):
    """Devuelve (hechos_derivados, trazas) para un individuo."""
    conocidos = set(HECHOS[individuo])
    trazas = []
    cambio = True
    while cambio:
        cambio = False
        for id_regla, condiciones, conclusion in REGLAS:
            if conclusion in conocidos:
                continue
            if all(cumple(c, conocidos) for c in condiciones):
                conocidos.add(conclusion)
                trazas.append((id_regla, condiciones, conclusion))
                cambio = True
    # Especies declaradas explícitamente (conocimiento del dominio)
    if individuo in ESPECIES_DECLARADAS:
        conocidos.add(ESPECIES_DECLARADAS[individuo])
    derivados = conocidos - set(HECHOS[individuo])
    return derivados, trazas

def ancestros(clase):
    """Todas las superclases de una clase siguiendo las tuplas 'es_un'."""
    resultado = []
    for sujeto, rel, objeto in VINCULOS:
        if sujeto == clase and rel == "es_un":
            resultado.append(objeto)
            resultado.extend(ancestros(objeto))
    return resultado

def confundibles(clase):
    """Clases con las que se puede confundir (relación simétrica)."""
    otras = []
    for sujeto, rel, objeto in VINCULOS:
        if rel == "se_confunde_con":
            if sujeto == clase:
                otras.append(objeto)
            elif objeto == clase:
                otras.append(sujeto)
    return otras

# ======
# PRUEBA
# ======
if __name__ == "__main__":
    print("=" * 60)
    print(" INFERENCIA SOBRE LOS INDIVIDUOS")
    print("=" * 60)
    for ind in HECHOS:
        derivados, trazas = inferir(ind)
        print(f"\n{ind}")
        print(f"  Hechos base : {sorted(HECHOS[ind])}")
        print(f"  Derivado    : {sorted(derivados)}")
        for id_r, cond, concl in trazas:
            print(f"    Regla {id_r:>2}: {' ^ '.join(cond)} -> {concl}")

    print("\n" + "=" * 60)
    print(" VÍNCULOS")
    print("=" * 60)
    for especie in ("Gato", "Caracal", "Perro", "Lobo"):
        print(f"{especie}: ancestros = {ancestros(especie)}, "
              f"se confunde con = {confundibles(especie)}")

    print("\n" + "=" * 60)
    print(" CÓMO DISTINGUIRLOS")
    print("=" * 60)
    for (a, b), info in DISTINCION.items():
        print(f"{a} vs {b}: {info['observar']}")
