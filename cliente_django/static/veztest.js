
function crearTree(obj,elemID){
	  var options = {
      format: 'svg'
      // format: 'png-image-element'
    }

    var image = Viz(treeJson(obj), options);
    var main = document.getElementById(elemID);

    main.innerHTML = image;		// SVG
    //main.appendChild(image);	// PNG
	
}



function treeJson(jsn){
	var cAxiom=0;
	var cUnable=0;
	var svg='digraph Tree {';
	for( var i=0 ; i < Object.keys(jsn.inferencias).length;i++) {
		
		if(jsn.inferencias[i].regla == "Axiom"){
			cAxiom++;
			svg = svg +'"'+ jsn.inferencias[i].deduccionVieja+ '"->"Axioma'+ cAxiom + '"[label ="('+jsn.inferencias[i].reglaPosIzq+','+jsn.inferencias[i].reglaPosDer+')"];';
		}else if(jsn.inferencias[i].regla == "Unable to prove"){
			cUnable++;
			svg = svg +'"'+ jsn.inferencias[i].deduccionVieja+ '"->"Unable to prove '+ cUnable + '"[label ="('+jsn.inferencias[i].reglaPosIzq+','+jsn.inferencias[i].reglaPosDer+')"];';
		
		}
		else{
			svg = svg +'"'+ jsn.inferencias[i].deduccionVieja+ '"->"'+ jsn.inferencias[i].deduccionNueva + '"[label ="'+jsn.inferencias[i].regla+'('+jsn.inferencias[i].reglaPosIzq+','+jsn.inferencias[i].reglaPosDer+')"];';
		}
	}
	svg+='"'+jsn.afirmacion + '"[shape=invtriangle, style=filled, color=seagreen1]';
	if(cAxiom>0){
		for ( var j = 1; j<= cAxiom; j++){
		    svg+='"Axioma'+j+ '"[ style=filled, color=cyan]';	
		}
	}
	if(cUnable>0){
		for ( var k = 1; k<= cUnable; k++){
		    svg+='"Unable to prove '+k+ '"[ style=filled, color=tomato1]';	
		}
	}
	svg+='}';
	return svg;
}