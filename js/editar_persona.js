// Procedimiento para traer los datos del registro a editar
// Ej: "id=9&nombre=bulbasaur"
let cadena = location.search; // Cadena con los símbolos & y =

// Crear un objeto URLSearchParams con la cadena
// El objeto URLSearchParams en JavaScript es una interfaz que proporciona métodos y propiedades para trabajar con las cadenas de consulta (query strings) en URLs.
// Facilitando la obtención de parámetros y valores individuales
let datos = new URLSearchParams(cadena);

// Crear un objeto para almacenar los nombres de las variables y sus valores
let resultado = {};

// Iterar sobre los parámetros y guardar los nombres y valores en el objeto resultado
for (const [nombre, valor] of datos) {
    resultado[nombre] = valor;
}

console.log(resultado); 

// Procedimiento para mostrar los datos a editar en el formulario de edición
document.getElementById("id").value = resultado["id"]
document.getElementById("nombre").value = resultado["nombre"]
document.getElementById("email").value = resultado["email"]
document.getElementById("telefono").value = resultado["telefono"]

function modificar() {
    let id = document.getElementById("id").value
    let nombreForm = document.getElementById("nombre").value
    let emailForm = document.getElementById("email").value
    let telefonoForm = document.getElementById("telefono").value
    let persona = {
        nombre: nombreForm,
        email: emailForm,
        telefono: telefonoForm
    }
    let url = "http://localhost:5000/update/"+id
    var options = {
        body: JSON.stringify(persona),
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        // el navegador seguirá automáticamente las redirecciones y devolverá el recurso final al que se ha redirigido.
        redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("modificado")
            alert("Registro modificado")
            //Puedes utilizar window.location.href para obtener la URL actual, redirigir a otras páginas
            window.location.href = "./personas.html";  
        })
        .catch(err => {
            //this.errored = true
            console.error(err);
            alert("Error al modificar")
        })      
}