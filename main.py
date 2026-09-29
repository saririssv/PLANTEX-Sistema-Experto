import tkinter as tk
from tkinter import ttk, messagebox
import os
from PIL import Image, ImageTk, ImageOps
 
try:
    from PIL import Image, ImageTk
    PILLOW_DISPONIBLE = True
except ImportError:
    PILLOW_DISPONIBLE = False


# ============================================================
# COLORES
# ============================================================

NARANJA = "#D97761"
NARANJA_OSCURO = "#C85F49"
NARANJA_CLARO = "#F8E8E2"
CREMA = "#FFF8F5"
BLANCO = "#FFFFFF"
TEXTO = "#3E3030"
VERDE = "#5E8C61"
VERDE_OSCURO = "#456B49"
GRIS = "#777777"
BORDE = "#E2C8C0"


# ============================================================
# BASE DE CONOCIMIENTO
# ============================================================

hechos = {
    "hojas_amarillas": False,
    "tierra_humeda": False,
    "tierra_seca": False,
    "poca_luz": False,
    "hojas_caidas": False,
    "manchas_hojas": False,
    "presencia_plagas": False,
    "crecimiento_lento": False,
    "bordes_secos": False,
    "tallo_debil": False
}


# ============================================================
# REGLAS
# ============================================================

reglas = [

    {
        "nombre": "Regla 1",
        "condiciones": [
            "hojas_amarillas",
            "tierra_humeda"
        ],
        "resultado": "Exceso de riego"
    },

    {
        "nombre": "Regla 2",
        "condiciones": [
            "tierra_seca",
            "hojas_caidas"
        ],
        "resultado": "Falta de agua"
    },

    {
        "nombre": "Regla 3",
        "condiciones": [
            "poca_luz",
            "crecimiento_lento"
        ],
        "resultado": "Falta de luz"
    },

    {
        "nombre": "Regla 4",
        "condiciones": [
            "presencia_plagas",
            "manchas_hojas"
        ],
        "resultado": "Presencia de plagas"
    },

    {
        "nombre": "Regla 5",
        "condiciones": [
            "tierra_seca",
            "bordes_secos"
        ],
        "resultado": "Falta de humedad"
    },

    {
        "nombre": "Regla 6",
        "condiciones": [
            "tallo_debil",
            "crecimiento_lento"
        ],
        "resultado": "Debilidad de la planta"
    },

    {
        "nombre": "Regla 7",
        "condiciones": [
            "hojas_amarillas",
            "hojas_caidas"
        ],
        "resultado": "Estrés por riego"
    },

    {
        "nombre": "Regla 8",
        "condiciones": [
            "crecimiento_lento",
            "poca_luz",
            "tierra_seca"
        ],
        "resultado": "Condiciones de cuidado inadecuadas"
    }
]


# ============================================================
# PREGUNTAS
# ============================================================

preguntas = [

    (
        "¿Las hojas de la planta están amarillas?",
        "hojas_amarillas"
    ),

    (
        "¿La tierra se encuentra húmeda?",
        "tierra_humeda"
    ),

    (
        "¿La tierra se encuentra seca?",
        "tierra_seca"
    ),

    (
        "¿La planta recibe poca luz?",
        "poca_luz"
    ),

    (
        "¿La planta tiene hojas caídas?",
        "hojas_caidas"
    ),

    (
        "¿La planta presenta manchas en las hojas?",
        "manchas_hojas"
    ),

    (
        "¿Se observa presencia de plagas?",
        "presencia_plagas"
    ),

    (
        "¿La planta presenta un crecimiento lento?",
        "crecimiento_lento"
    ),

    (
        "¿Los bordes de las hojas están secos?",
        "bordes_secos"
    ),

    (
        "¿El tallo de la planta se encuentra débil?",
        "tallo_debil"
    )
]


# ============================================================
# RECOMENDACIONES
# ============================================================

recomendaciones = {

    "Exceso de riego":
        "Reduce la frecuencia de riego y verifica que la maceta tenga un buen drenaje.",

    "Falta de agua":
        "Aumenta moderadamente el riego y revisa la humedad de la tierra.",

    "Falta de luz":
        "Coloca la planta en un lugar con mayor iluminación, evitando cambios bruscos.",

    "Presencia de plagas":
        "Revisa cuidadosamente las hojas y aplica un tratamiento adecuado contra las plagas.",

    "Falta de humedad":
        "Aumenta la humedad ambiental y evita que la tierra permanezca demasiado seca.",

    "Debilidad de la planta":
        "Mejora la iluminación, el riego y las condiciones generales de crecimiento.",

    "Estrés por riego":
        "Revisa la frecuencia de riego y comprueba tanto la humedad como el drenaje.",

    "Condiciones de cuidado inadecuadas":
        "Revisa iluminación, riego y humedad para mejorar las condiciones de crecimiento.",

    "No se identificaron problemas":
        "No se detectaron condiciones asociadas a los problemas registrados.",

    "No se pudo determinar el problema":
        "Los datos ingresados no coinciden con ninguna regla específica."
}


# ============================================================
# VARIABLES DEL SISTEMA
# ============================================================

indice_pregunta = 0
reglas_activadas = []
regla_seleccionada = None


# ============================================================
# MOTOR DE INFERENCIA
# ============================================================

# ------------------------------------------------------------
# FASE 1: EQUIPARACIÓN
# ------------------------------------------------------------

def equiparacion():

    reglas_coincidentes = []

    for regla in reglas:

        cumple = True

        for condicion in regla["condiciones"]:

            if hechos.get(condicion) is not True:

                cumple = False
                break

        if cumple:

            reglas_coincidentes.append(regla)

    return reglas_coincidentes


# ------------------------------------------------------------
# FASE 2: RESOLUCIÓN DE CONFLICTOS
# ------------------------------------------------------------

def resolucion_conflictos(reglas_coincidentes):

    if not reglas_coincidentes:

        return None

    regla_ganadora = max(
        reglas_coincidentes,
        key=lambda regla: len(regla["condiciones"])
    )

    return regla_ganadora


# ------------------------------------------------------------
# FASE 3: EJECUCIÓN
# ------------------------------------------------------------

def ejecucion(regla):

    if regla is None:
        if not any(hechos.values()):
            return "No se identificaron problemas"
        return "Información insuficiente para determinar el problema"

    return regla["resultado"]


# ============================================================
# CARGAR ENCABEZADO
# ============================================================

def cargar_imagen_header():

    ruta = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "plantex_header.png"
    )

    # Verificar que exista
    if not os.path.exists(ruta):

        print("ERROR: No se encontró:")
        print(ruta)

        return None

    # Verificar Pillow
    if not PILLOW_DISPONIBLE:

        print("ERROR: Pillow no está instalada.")
        print("Ejecute: pip install pillow")

        return None

    try:

        # Abrir imagen
        imagen = Image.open(ruta).convert("RGB")

        # Tamaño del encabezado
        ancho_header = 950
        alto_header = 145

        ancho_original, alto_original = imagen.size

        # Calcular escala para cubrir todo el encabezado
        escala_ancho = ancho_header / ancho_original
        escala_alto = alto_header / alto_original

        escala = max(
            escala_ancho,
            escala_alto
        )

        nuevo_ancho = int(
            ancho_original * escala
        )

        nuevo_alto = int(
            alto_original * escala
        )

        # Redimensionar manteniendo proporción
        imagen = imagen.resize(
            (nuevo_ancho, nuevo_alto),
            Image.Resampling.LANCZOS
        )

        # Recorte centrado
        izquierda = max(
            0,
            (nuevo_ancho - ancho_header) // 2
        )

        arriba = max(
            0,
            (nuevo_alto - alto_header) // 2
        )

        derecha = izquierda + ancho_header
        abajo = arriba + alto_header

        imagen = imagen.crop(
            (
                izquierda,
                arriba,
                derecha,
                abajo
            )
        )

        return ImageTk.PhotoImage(imagen)

    except Exception as error:

        print(
            "ERROR al cargar el encabezado:",
            error
        )

        return None

    # ============================================================
# MOSTRAR PREGUNTA
# ============================================================

imagen_pregunta = None


def mostrar_pregunta():

    global indice_pregunta
    global imagen_pregunta

    if indice_pregunta >= len(preguntas):

        finalizar_interaccion()

        return

    texto, hecho = preguntas[indice_pregunta]

    # ========================================================
    # CARGAR IMAGEN DE LA PREGUNTA
    # ========================================================

    ruta_imagen = os.path.join(
        os.path.dirname(
            os.path.abspath(__file__)
        ),
        "hojas_amarillas.png"
    )

    if os.path.exists(ruta_imagen):

        # Cargar imagen conservando transparencia
        imagen = Image.open(
            ruta_imagen
        ).convert("RGBA")

        # Crear fondo color crema
        fondo = Image.new(
            "RGBA",
            imagen.size,
            "#FFF5EF"
        )

        # Combinar imagen con el fondo
        fondo.alpha_composite(imagen)

        # Convertir ahora sí a RGB
        imagen = fondo.convert("RGB")

        # Ajustar imagen sin deformarla
        imagen = ImageOps.contain(
            imagen,
            (210, 170),
            method=Image.Resampling.LANCZOS
        )

        imagen_pregunta = ImageTk.PhotoImage(
            imagen
        )

        pregunta_imagen_label.config(
            image=imagen_pregunta,
            text=""
        )

        # Mantener referencia de la imagen
        pregunta_imagen_label.image = imagen_pregunta

    else:

        pregunta_imagen_label.config(
            image="",
            text="🌱",
            font=("Segoe UI Emoji", 50),
            fg=VERDE
        )

    # ========================================================
    # ACTUALIZAR TEXTO DE LA PREGUNTA
    # ========================================================

    pregunta_label.config(
        text=texto
    )

    numero_label.config(
        text=f"Pregunta {indice_pregunta + 1} de {len(preguntas)}"
    )

    progreso["value"] = indice_pregunta

    porcentaje = int(
        (indice_pregunta / len(preguntas)) * 100
    )

    progreso_label.config(
        text=f"{porcentaje}% completado"
    )

    estado_label.config(
        text="Seleccione una respuesta"
    )

    boton_si.config(
        state="normal"
    )

    boton_no.config(
        state="normal"
    )


    # ========================================================
    # MOSTRAR TEXTO DE LA PREGUNTA
    # ========================================================

    pregunta_label.config(
        text=texto
    )

    numero_label.config(
        text=(
            f"Pregunta "
            f"{indice_pregunta + 1} "
            f"de "
            f"{len(preguntas)}"
        )
    )

    # ========================================================
    # PROGRESO
    # ========================================================

    progreso["value"] = indice_pregunta

    porcentaje = int(
        (
            indice_pregunta /
            len(preguntas)
        ) * 100
    )

    progreso_label.config(
        text=f"{porcentaje}% completado"
    )

    # ========================================================
    # ESTADO
    # ========================================================

    estado_label.config(
        text="Seleccione una respuesta"
    )

    # ========================================================
    # BOTONES
    # ========================================================

    boton_si.config(
        state="normal"
    )

    boton_no.config(
        state="normal"
    )


# ============================================================
# RESPONDER
# ============================================================

def responder(valor):

    global indice_pregunta

    _, nombre_hecho = preguntas[
        indice_pregunta
    ]

    hechos[nombre_hecho] = valor

    indice_pregunta += 1

    mostrar_pregunta()


# ============================================================
# FINALIZAR INTERACCIÓN
# ============================================================

def finalizar_interaccion():

    boton_si.config(
        state="disabled"
    )

    boton_no.config(
        state="disabled"
    )

    pregunta_label.config(
        text="Analizando la información ingresada..."
    )

    numero_label.config(
        text="Procesando base de conocimiento"
    )

    progreso["value"] = 10

    progreso_label.config(
        text="100% completado"
    )

    ventana.after(
        500,
        realizar_inferencia
    )


# ============================================================
# REALIZAR INFERENCIA
# ============================================================

def realizar_inferencia():

    global reglas_activadas
    global regla_seleccionada

    # FASE 1
    reglas_activadas = equiparacion()

    # FASE 2
    regla_seleccionada = resolucion_conflictos(
        reglas_activadas
    )

    # FASE 3
    diagnostico = ejecucion(
        regla_seleccionada
    )

    mostrar_resultado(
        diagnostico
    )


# ============================================================
# MOSTRAR RESULTADO
# ============================================================

def mostrar_resultado(diagnostico):

    pregunta_card.pack_forget()

    resultado_card.pack(
        fill="both",
        expand=True,
        padx=0,
        pady=5
    )

    # ========================================================
    # DIAGNÓSTICO
    # ========================================================

    resultado_label.config(
        text=diagnostico
    )

    # ========================================================
    # RECOMENDACIÓN
    # ========================================================

    recomendacion_label.config(
        text=recomendaciones.get(
            diagnostico,
            "Revise las condiciones de la planta."
        )
    )

    # ========================================================
    # REGLA ACTIVADA
    # ========================================================

    if regla_seleccionada:

        regla_texto = (
            f"{regla_seleccionada['nombre']}\n"
            f"{len(regla_seleccionada['condiciones'])} "
            f"condiciones cumplidas"
        )

    else:

        regla_texto = (
            "Ninguna regla específica"
        )

    reglas_label.config(
        text=regla_texto
    )

    
    # ========================================================
    # MOTOR DE INFERENCIA
    # ========================================================

    cantidad_reglas = len(reglas_activadas)

    if cantidad_reglas == 0:

        texto_fase1 = (
            "1. Equiparación\n"
            "No se encontraron reglas compatibles."
        )

    else:

        texto_fase1 = (
            "1. Equiparación\n"
            f"{cantidad_reglas} regla(s) compatible(s)."
        )


    if regla_seleccionada:

        texto_fase2 = (
            "2. Resolución de conflictos\n"
            f"Se seleccionó {regla_seleccionada['nombre']}."
        )

    else:

        texto_fase2 = (
            "2. Resolución de conflictos\n"
            "No se seleccionó ninguna regla."
        )


    texto_fase3 = (
        "3. Ejecución\n"
        f"Diagnóstico: {diagnostico}"
    )


    fases_label.config(
        text=(
            f"{texto_fase1}\n\n"
            f"{texto_fase2}\n\n"
            f"{texto_fase3}"
        )
    )

# ============================================================
# REINICIAR
# ============================================================

def reiniciar():

    global indice_pregunta
    global reglas_activadas
    global regla_seleccionada

    indice_pregunta = 0

    reglas_activadas = []

    regla_seleccionada = None

    # Limpiar hechos
    for clave in hechos:

        hechos[clave] = False

    resultado_card.pack_forget()

    pregunta_card.pack(
        fill="both",
        expand=True,
        padx=0,
        pady=8
    )

    mostrar_pregunta()


# ============================================================
# SALIR
# ============================================================

def salir():

    respuesta = messagebox.askyesno(
        "Salir",
        "¿Desea cerrar PLANTEX?"
    )

    if respuesta:

        ventana.destroy()


# ============================================================
# VENTANA PRINCIPAL
# ============================================================

ventana = tk.Tk()

ventana.title(
    "PLANTEX - Sistema experto"
)

ventana.geometry(
    "950x700"
)

ventana.resizable(
    False, False)

ventana.configure(
    bg=CREMA
)


# ============================================================
# ESTILOS
# ============================================================

style = ttk.Style()

try:

    style.theme_use("clam")

except:

    pass


style.configure(
    "PLANTEX.Horizontal.TProgressbar",

    troughcolor="#F1D8D0",

    background=NARANJA,

    bordercolor="#F1D8D0",

    lightcolor=NARANJA,

    darkcolor=NARANJA,

    thickness=8
)


# ============================================================
# HEADER
# ============================================================

header = tk.Frame(
    ventana,
    bg=NARANJA,
    height=145
)

header.pack(
    fill="x",
    side="top"
)

header.pack_propagate(False)


# Cargar imagen
imagen_header = cargar_imagen_header()


if imagen_header is not None:

    # Mostrar imagen
    header_label = tk.Label(
        header,
        image=imagen_header,
        bg=NARANJA,
        bd=0,
        highlightthickness=0
    )

    header_label.pack(
        fill="both",
        expand=True
    )

    # IMPORTANTE:
    # conservar referencia para evitar
    # que Tkinter elimine la imagen
    header_label.image = imagen_header


else:

    # Si no se pudo cargar la imagen,
    # mostrar aviso visual.

    header_label = tk.Label(
        header,
        text=(
            "PLANTEX\n"
            "Sistema experto para el diagnóstico de plantas"
        ),
        font=("Segoe UI", 24, "bold"),
        fg=BLANCO,
        bg=NARANJA,
        justify="center"
    )

    header_label.pack(
        expand=True
    )


# ============================================================
# CONTENIDO
# ============================================================

contenido = tk.Frame(
    ventana,
    bg=CREMA
)

contenido.pack(
    fill="both",
    expand=True,
    padx=35,
    pady=12
)


# ============================================================
# TÍTULO
# ============================================================

titulo_seccion = tk.Label(
    contenido,
    text="Diagnóstico de la planta",
    font=("Segoe UI", 19, "bold"),
    fg=TEXTO,
    bg=CREMA
)

titulo_seccion.pack(
    anchor="w"
)


# ============================================================
# INFORMACIÓN
# ============================================================

info_frame = tk.Frame(
    contenido,
    bg=CREMA
)

info_frame.pack(
    fill="x",
    pady=(3, 8)
)


numero_label = tk.Label(
    info_frame,
    text="Pregunta 1 de 10",
    font=("Segoe UI", 10, "bold"),
    fg=NARANJA_OSCURO,
    bg=CREMA
)

numero_label.pack(
    side="left"
)


progreso_label = tk.Label(
    info_frame,
    text="0% completado",
    font=("Segoe UI", 10),
    fg=GRIS,
    bg=CREMA
)

progreso_label.pack(
    side="right"
)


# ============================================================
# BARRA DE PROGRESO
# ============================================================

progreso = ttk.Progressbar(
    contenido,

    style="PLANTEX.Horizontal.TProgressbar",

    orient="horizontal",

    mode="determinate",

    maximum=10,

    value=0
)

progreso.pack(
    fill="x",
    pady=(0, 8)
)


# ============================================================
# ESTADO
# ============================================================

estado_label = tk.Label(
    contenido,
    text="Seleccione una respuesta",
    font=("Segoe UI", 10),
    fg=GRIS,
    bg=CREMA
)

estado_label.pack(
    anchor="w",
    pady=(0, 5)
)


# ============================================================
# TARJETA DE LA PREGUNTA
# ============================================================

pregunta_card = tk.Frame(
    contenido,
    bg=BLANCO,
    highlightbackground=BORDE,
    highlightthickness=1
)

pregunta_card.pack(
    fill="both",
    expand=True,
    pady=5
)


# ============================================================
# PARTE SUPERIOR: IMAGEN + PREGUNTA
# ============================================================

pregunta_superior = tk.Frame(
    pregunta_card,
    bg=BLANCO
)

pregunta_superior.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=(18, 5)
)


# ============================================================
# CONTENEDOR DE LA IMAGEN
# ============================================================

imagen_frame = tk.Frame(
    pregunta_superior,
    bg="#FFF5EF",
    width=220,
    height=170,
    highlightbackground=BORDE,
    highlightthickness=1
)

imagen_frame.pack(
    side="left",
    padx=(5, 30)
)

imagen_frame.pack_propagate(False)


pregunta_imagen_label = tk.Label(
    imagen_frame,
    bg="#FFF5EF",
    bd=0
)

pregunta_imagen_label.pack(
    fill="both",
    expand=True
)


# ============================================================
# CONTENEDOR DEL TEXTO
# ============================================================

texto_frame = tk.Frame(
    pregunta_superior,
    bg=BLANCO
)

texto_frame.pack(
    side="left",
    fill="both",
    expand=True
)


pregunta_label = tk.Label(
    texto_frame,
    text="",
    font=("Segoe UI", 19, "bold"),
    fg=TEXTO,
    bg=BLANCO,
    wraplength=450,
    justify="left"
)

pregunta_label.pack(
    fill="both",
    expand=True,
    anchor="center"
)


# ============================================================
# ZONA EXCLUSIVA PARA LOS BOTONES
# ============================================================

botones_frame = tk.Frame(
    pregunta_card,
    bg=BLANCO,
    height=75
)

botones_frame.pack(
    fill="x",
    pady=(0, 18)
)

botones_frame.pack_propagate(False)


# ============================================================
# BOTÓN SÍ
# ============================================================

boton_si = tk.Button(
    botones_frame,
    text="✓  SÍ",
    font=("Segoe UI", 12, "bold"),
    bg=VERDE,
    fg="white",
    activebackground="#4F8052",
    activeforeground="white",
    relief="flat",
    bd=0,
    width=12,
    height=2,
    cursor="hand2",
    command=lambda: responder(True)
)

boton_si.pack(
    side="left",
    padx=8,
    expand=True
)


# ============================================================
# BOTÓN NO
# ============================================================

boton_no = tk.Button(
    botones_frame,
    text="✕  NO",
    font=("Segoe UI", 12, "bold"),
    bg="#C96B5B",
    fg="white",
    activebackground="#A95749",
    activeforeground="white",
    relief="flat",
    bd=0,
    width=12,
    height=2,
    cursor="hand2",
    command=lambda: responder(False)
)

boton_no.pack(
    side="left",
    padx=8,
    expand=True
)

# ============================================================
# TARJETA DE RESULTADO
# ============================================================

resultado_card = tk.Frame(
    contenido,
    bg=BLANCO,
    highlightbackground=BORDE,
    highlightthickness=1
)


# ============================================================
# TÍTULO DEL RESULTADO
# ============================================================

resultado_titulo = tk.Label(
    resultado_card,
    text="Resultado del diagnóstico",
    font=("Segoe UI", 19, "bold"),
    fg=TEXTO,
    bg=BLANCO
)

resultado_titulo.pack(
    pady=(10, 8)
)


# ============================================================
# DIAGNÓSTICO
# ============================================================

diagnostico_frame = tk.Frame(
    resultado_card,
    bg="#F9E9E4",
    highlightbackground=BORDE,
    highlightthickness=1,
    height=82
)

diagnostico_frame.pack(
    fill="x",
    padx=30,
    pady=(0, 8)
)

diagnostico_frame.pack_propagate(False)


tk.Label(
    diagnostico_frame,
    text="DIAGNÓSTICO",
    font=("Segoe UI", 10, "bold"),
    fg=NARANJA_OSCURO,
    bg="#F9E9E4"
).pack(
    pady=(7, 0)
)


# IMPORTANTE:
# Este nombre debe ser resultado_label porque
# mostrar_resultado() utiliza resultado_label.

resultado_label = tk.Label(
    diagnostico_frame,
    text="",
    font=("Segoe UI", 17, "bold"),
    fg=TEXTO,
    bg="#F9E9E4"
)

resultado_label.pack(
    pady=(1, 4)
)


# ============================================================
# RECOMENDACIÓN
# ============================================================

recomendacion_frame = tk.Frame(
    resultado_card,
    bg="#F8F6F4",
    highlightbackground=BORDE,
    highlightthickness=1,
    height=72
)

recomendacion_frame.pack(
    fill="x",
    padx=30,
    pady=(0, 8)
)

recomendacion_frame.pack_propagate(False)


tk.Label(
    recomendacion_frame,
    text="RECOMENDACIÓN",
    font=("Segoe UI", 10, "bold"),
    fg=VERDE,
    bg="#F8F6F4"
).pack(
    pady=(6, 0)
)


recomendacion_label = tk.Label(
    recomendacion_frame,
    text="",
    font=("Segoe UI", 10),
    fg=TEXTO,
    bg="#F8F6F4",
    wraplength=800,
    justify="center"
)

recomendacion_label.pack(
    fill="both",
    expand=True,
    pady=(1, 3)
)


# ============================================================
# INFORMACIÓN DEL MOTOR
# ============================================================

info_resultado = tk.Frame(
    resultado_card,
    bg=BLANCO
)

info_resultado.pack(
    fill="x",
    padx=30,
    pady=(0, 5)
)


# ============================================================
# REGLA ACTIVADA
# ============================================================

reglas_box = tk.Frame(
    info_resultado,
    bg=CREMA,
    highlightbackground=BORDE,
    highlightthickness=1,
    height=72
)

reglas_box.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(0, 5)
)

reglas_box.pack_propagate(False)


tk.Label(
    reglas_box,
    text="REGLA ACTIVADA",
    font=("Segoe UI", 9, "bold"),
    fg=NARANJA_OSCURO,
    bg=CREMA
).pack(
    pady=(6, 1)
)


# IMPORTANTE:
# Este nombre debe ser reglas_label porque
# mostrar_resultado() utiliza reglas_label.

reglas_label = tk.Label(
    reglas_box,
    text="",
    font=("Segoe UI", 9),
    fg=TEXTO,
    bg=CREMA,
    justify="center",
    wraplength=400
)

reglas_label.pack(
    fill="both",
    expand=True,
    pady=(0, 3)
)


# ============================================================
# MOTOR DE INFERENCIA
# ============================================================

fases_box = tk.Frame(
    info_resultado,
    bg=CREMA,
    highlightbackground=BORDE,
    highlightthickness=1,
    height=72
)

fases_box.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(5, 0)
)

fases_box.pack_propagate(False)


tk.Label(
    fases_box,
    text="MOTOR DE INFERENCIA",
    font=("Segoe UI", 9, "bold"),
    fg=NARANJA_OSCURO,
    bg=CREMA
).pack(
    pady=(6, 1)
)


# IMPORTANTE:
# Este nombre debe ser fases_label porque
# mostrar_resultado() utiliza fases_label.

fases_label = tk.Label(
    fases_box,
    text="",
    font=("Segoe UI", 9),
    fg=TEXTO,
    bg=CREMA,
    justify="center"
)

fases_label.pack(
    fill="both",
    expand=True,
    pady=(0, 3)
)


# ============================================================
# BOTONES INFERIORES
# ============================================================

botones_finales = tk.Frame(
    contenido,
    bg=CREMA
)

botones_finales.pack(
    fill="x",
    pady=(8, 0)
)


boton_reiniciar = tk.Button(

    botones_finales,

    text="↻  Nuevo diagnóstico",

    command=lambda: reiniciar(),

    font=(
        "Segoe UI",
        10,
        "bold"
    ),

    bg=NARANJA,

    fg=BLANCO,

    activebackground=NARANJA_OSCURO,

    activeforeground=BLANCO,

    bd=0,

    padx=18,

    pady=7,

    cursor="hand2"
)

boton_reiniciar.pack(
    side="left"
)


boton_salir = tk.Button(

    botones_finales,

    text="Salir",

    command=lambda: salir(),

    font=(
        "Segoe UI",
        10
    ),

    bg="#E7D8D3",

    fg=TEXTO,

    activebackground="#D8C6C0",

    bd=0,

    padx=22,

    pady=7,

    cursor="hand2"
)

boton_salir.pack(
    side="right"
)


# ============================================================
# INICIAR
# ============================================================

mostrar_pregunta()

ventana.mainloop()