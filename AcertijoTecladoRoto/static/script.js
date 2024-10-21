// Teclado alterado
const tecladoAlterado = {
    'a': 't', 'b': 'r', 'c': 'y', 'd': 'u', 'e': 'i',
    'f': 'o', 'g': 'p', 'h': 'q', 'i': 'w', 'j': 'e',
    'k': 's', 'l': 'd', 'm': 'f', 'n': 'g', 'o': 'h',
    'p': 'j', 'q': 'k', 'r': 'l', 's': 'z', 't': 'x',
    'u': 'c', 'v': 'v', 'w': 'b', 'x': 'n', 'y': 'm',
    'z': 'a', ' ': ' '  // El espacio no cambia
};

let acertijos = [];
let acertijoActual = 0;
let puntos = 0;

async function cargarAcertijos() {
    const response = await fetch('static/acertijos.json');
    acertijos = await response.json();
    mostrarAcertijo(acertijoActual);
}

function mostrarAcertijo(index) {
    const output = document.getElementById('output');
    const pregunta = acertijos[index].pregunta;
    output.innerHTML += `<p class="info">${pregunta}</p>`;
}

function procesarRespuesta(respuesta) {
    const respuestaCorrecta = acertijos[acertijoActual].respuesta;
    if (respuesta === respuestaCorrecta) {
        puntos += 10; // Incrementar puntos
        mostrarMensaje(`¡Correcto! Puntos: ${puntos}`, 'correct');
        acertijoActual++; // Avanza al siguiente acertijo
        if (acertijoActual < acertijos.length) {
            mostrarAcertijo(acertijoActual);
        } else {
            mostrarMensaje('¡Has completado todos los acertijos!', 'info');
        }
    } else {
        mostrarMensaje('Respuesta incorrecta. Intenta de nuevo.', 'incorrect');
    }
}

function mostrarMensaje(mensaje, tipo) {
    const output = document.getElementById('output');
    const nuevoMensaje = document.createElement('p');
    nuevoMensaje.className = tipo; // Asignar la clase según el tipo
    nuevoMensaje.innerText = mensaje;
    output.appendChild(nuevoMensaje);
}

function alterarTeclado(event) {
    const input = event.target;
    const tecla = event.data;  // Obtiene el último carácter ingresado

    // Verificamos si la tecla está en el mapeo
    if (tecladoAlterado.hasOwnProperty(tecla)) {
        event.preventDefault(); // Prevenir la entrada del carácter original
        
        // Reemplazar solo el último carácter
        const cursorPos = input.selectionStart; // Guardamos la posición del cursor
        const textoAntes = input.value.slice(0, cursorPos - 1); // Texto antes del último carácter
        const textoDespues = input.value.slice(cursorPos); // Texto después del último carácter

        // Reemplazar el texto en el campo de entrada
        input.value = textoAntes + tecladoAlterado[tecla] + textoDespues;
        
        // Actualizar la posición del cursor
        input.selectionStart = input.selectionEnd = cursorPos; // Mantener el cursor en su lugar
    }
}

// Llama a la función al cargar la página
window.onload = cargarAcertijos;
