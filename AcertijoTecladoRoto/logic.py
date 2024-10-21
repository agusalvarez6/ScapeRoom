# Acertijos
primer_acertijo = "¿Cuál es la capital de Francia?"
primer_respuesta_correcta = "paris"

segundo_acertijo = "¿Cuál es el lenguaje de programación de esta aplicación?"
segunda_respuesta_correcta = "python"

# Diccionario para alterar el teclado
teclado_alterado = {
    'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f',
    'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k',
    'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p',
    'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u',
    'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z',
    'z': 'a', ' ': ' '  # El espacio no cambia
}

# Inicializa el historial de mensajes
def inicializar_historial():
    return [primer_acertijo]

# Procesa la respuesta al primer acertijo
def procesar_acertijo(respuesta, historial_mensajes):
    if respuesta:  # Verificar si no es None
        respuesta = respuesta.lower()

        if respuesta == primer_respuesta_correcta:
            historial_mensajes.append(f"{respuesta}")
            historial_mensajes.append("Vulnerabilidad detectada, el teclado ha cambiado.")
            historial_mensajes.append(segundo_acertijo)
            return 1, historial_mensajes  # Avanzar al segundo acertijo (teclado alterado)
        else:
            historial_mensajes.append(f"{respuesta}")
            historial_mensajes.append("Respuesta incorrecta. Intenta de nuevo.")
    return 0, historial_mensajes

# Procesa la entrada con el teclado alterado para el segundo acertijo
def procesar_entrada_alterada(entrada, historial_mensajes):
    if entrada:  # Verificar si no es None
        entrada = entrada.lower()
        # Cambiamos las letras según el teclado alterado
        resultado = ''.join([teclado_alterado.get(letra, letra) for letra in entrada])

        # Comprobar si la entrada alterada corresponde a la respuesta "python"
        if resultado == segunda_respuesta_correcta:
            historial_mensajes.append(entrada)
            historial_mensajes.append("Firewall superado, mejorando medidas de seguridad.")
            return 2, historial_mensajes  # Estado final, juego completado
        else:
            historial_mensajes.append(entrada)
            historial_mensajes.append("Error, código incorrecto. Intenta de nuevo.")
    return 1, historial_mensajes
