/*
Maria Alvarez Hernandez ID: 4-0239-0850
Luis Alonso Calderon Achio ID: 1-1702-0626
Enrique Diaz Delgado ID: 1-1725-0124
Derian Sibaja Chavarria ID 4-0232-0842
*/
const URL_SERVER = "https://servidordjango.herokuapp.com/api/pruebas"

function enviarAfirmacion() {
	let caja = document.getElementById('afirmacion')
    let data = {afirmacion: caja.value}
	
	fetch(URL_SERVER, {
		method: "POST",
		credentials: "same-origin",
		headers: {
			"Accept": "application/json",
			"Content-Type": "application/json"
		},
		body: JSON.stringify(data)
	}).then(response => response.json())
	.then(data => atenderRespuesta(data))
	.catch(response => alert(response));
}

function atenderRespuesta(data){
	if(data.msg == "prueba with this afirmacion already exists."){
		alert("Ya se había realizado una prueba con esta afirmación. Mostrando resultado anterior...");
		dibujarPruebaEspecifica(data.afirmacion)
	} else if (data.msg == "Failed to parse"){
		alert("Ha fallado el parseo de la fórmula. Verifique que se escribió correctamente");
	} else {
		crearTree(data,'diagrama');
		$("#myModal").modal()
	}
}


//text
function dibujarPruebaEspecifica(afirm){
	let urlSolic = `${URL_SERVER}/${afirm}`
	
	fetch(urlSolic, {
		method: "GET",
		credentials: "same-origin",
		headers: {
			"Accept": "application/json",
			"Content-Type": "application/json"
		},
	}).then(response => response.json())
	.then(data => crearTree(data,'diagrama'))
	.then(d => $("#myModal").modal())
	.catch(response => alert(response));
}


function asignarBotonesHistorial(){
	let tabla = document.getElementById("tabla-historial")
	
	for(fil of tabla.children){
		let afir = fil.children[0].innerText;
		console.log(afir)
		let but = document.createElement("button");
		but.innerHTML = "Consultar Árbol"
		but.classList.add("btn-primary");
		but.classList.add("btn");
		but.classList.add("btn-md");
		let celd = document.createElement("td");
		but.addEventListener("click", e =>
			dibujarPruebaEspecifica(afir)
		)
		celd.appendChild(but)
		fil.appendChild(celd)
	}
}

asignarBotonesHistorial();