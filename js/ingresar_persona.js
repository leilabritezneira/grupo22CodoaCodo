function guardar() {
    let nombre_ingresado = document.getElementById("nombre").value
    let email_ingresado = document.getElementById("email").value
    let telefono_ingresado = document.getElementById("telefono").value

    console.log(nombre_ingresado, email_ingresado, telefono_ingresado);

    let enviar_persona = {
        nombre: nombre_ingresado,
        email: email_ingresado,
        telefono: telefono_ingresado
    }
    console.log(enviar_persona);
    
    let url = "http://localhost:5000/registro"
    var options = {
        body: JSON.stringify(enviar_persona),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Se ha registrado correctamente!")
            // Devuelve el href (URL) de la página actual
            window.location.href = "./personas.html";  
            
        })
        .catch(err => {
            //this.errored = true
            alert("No se pudo realizar el registro, intenta nuevamente!")
            console.error(err);
        })
}