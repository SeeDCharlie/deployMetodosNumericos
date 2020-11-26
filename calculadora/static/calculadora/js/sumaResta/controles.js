$( "#btnOkUno" ).on( "click", function() {
    $('#matrizUno').empty();
    var rows = $('#rowsUno').val();
    var cols = $('#colsUno').val();
    if(rows == ""){
        alert("Digite el numero de filas y columnas correcto !!!");
    }else{
        createMatrix(rows, cols, "matrizUno");
    }
    
});
$( "#btnOkDos" ).on( "click", function() {
    $('#matrizDos').empty(); 
    var rows = $('#rowsDos').val();
    var cols = $('#colsDos').val();
    if(rows == ""){
        alert("Digite el numero de filas y columnas correcto !!!");
    }else{
        createMatrix(rows, cols, "matrizDos");
    }
    
});
$( "#btnOkTres" ).on( "click", function() {
    $('#matrizTres').empty(); 
    var rows = $('#rowsTres').val();
    var cols = $('#colsTres').val();
    if(rows == "" || cols == ""){
        alert("Digite el numero de filas y columnas correcto !!!");
    }else{
        createMatrix(rows, cols, "matrizTres");
    }
    
});
//--------------------------------------------------------------------------------------------------------
$( "#btnDeleteOne" ).on( "click", function() {
    $('#matrizUno').empty(); 
});
$( "#btnDeleteTwo" ).on( "click", function() {
    $('#matrizDos').empty();    
});
$( "#btnDeleteTres" ).on( "click", function() {
    $('#matrizTres').empty();    
});
//
//--------------------------------------------------------------------------------------------------------
$( "#btnMaInversa" ).on( "click", function() {
    var rows = $('#rowsTres').val();
    var cols = $('#colsTres').val();

    if(rows == "" || cols == "" ){
        alert("NO se han creado las matrices ");
    }else{
        if(rows == cols){
            $('#nameOperaUno').empty();
            $('#nameOperaUno').append("Inversa de una matriz");
            var datos = JSON.stringify({
                mUno: getMatrix('matrizTres')
            }); 
            calcMa('btnMaInversa',datos,'matrixResultDos');
        }else{
            alert("la matriz debe ser de dimensiones cuadradas!");
        }
        
    }
});
//--------------------------------------------------------------------------------------------------------
$( "#btnMaTrans" ).on( "click", function() {
    var rows = $('#rowsTres').val();
    var cols = $('#colsTres').val();

    if(rows == "" || cols == "" ){
        alert("NO se han creado las matrices ");
    }else{
        $('#nameOperaUno').empty();
        $('#nameOperaUno').append("Transpuesta de una matriz ");
        var datos = JSON.stringify({
            mUno: getMatrix('matrizTres')
        }); 
        calcMa('btnMaTrans',datos,'matrixResultDos');
    }
});
//--------------------------------------------------------------------------------------------------------
$( "#btnEscalar" ).on( "click", function() {
    var rows = $('#rowsTres').val();
    var cols = $('#colsTres').val();

    if(rows == "" || cols == "" ){
        alert("NO se han creado las matrices ");
    }else{
        $('#nameOperaUno').empty();
        $('#nameOperaUno').append("Producto Escalar");
        var datos = JSON.stringify({
            mUno: getMatrix('matrizTres'),
            producto:$("#producto_k").val()
        }); 
        calcMa('btnEscalar',datos,'matrixResultDos');
        $('#modalProdEsca').modal('hide');
    }
});
//--------------------------------------------------------------------------------------------------------
$( "#btnMaGauss" ).on( "click", function() {
    var rows = $('#rowsTres').val();
    var cols = $('#colsTres').val();

    if(rows == "" || cols == "" ){
        alert("NO se han creado las matrices ");
    }else{
        
        if(rows == (cols-1)){
            $('#nameOperaUno').empty();
            $('#nameOperaUno').append("Gauss Jordan ");
            var datos = JSON.stringify({
                mUno: getMatrix('matrizTres')
            }); 
            calcMa('btnMaGauss',datos,'matrixResultDos');
        }else{
            alert("la matriz debe ser de dimensiones cuadradas!");
        }
    }
});
//--------------------------------------------------------------------------------------------------------
$( "#btnSum" ).on( "click", function() {
    var rowsCols = getRowsCols();

    if(rowsCols[0].includes(NaN) || rowsCols[1].includes(NaN) ){
        alert("NO se han creado las matrices ");
    }else{
        if(rowsCols[0][0] == rowsCols[1][0] && rowsCols[0][1] == rowsCols[1][1]){
            $('#nameOpera').empty();
            $('#nameOpera').append("Suma de Matrices ");
            var datos = JSON.stringify({
                mUno: getMatrix('matrizUno'),
                mDos: getMatrix('matrizDos')  
            });
            calcMa('btnSum', datos, 'matrixResult');
            
        }else{
            alert("las filas y columnas de las matrices deben ser iguales!!"); 
        }
    }
});
//--------------------------------------------------------------------------------------------------------
$( "#btnRest" ).on( "click", function() {
    var rowsCols = getRowsCols();

    if(rowsCols[0].includes(NaN) || rowsCols[1].includes(NaN) ){
        alert("NO se han creado las matrices ");
    }else{
        if(rowsCols[0][0] == rowsCols[1][0] && rowsCols[0][1] == rowsCols[1][1]){
            $('#nameOpera').empty();
            $('#nameOpera').append("Resta de Matrices ");
            var datos = JSON.stringify({
                mUno: getMatrix('matrizUno'),
                mDos: getMatrix('matrizDos')  
            });
            calcMa('btnRest', datos, 'matrixResult');
        }else{
            alert("las filas y columnas de las matrices deben ser iguales!!");
        }
    }
});
//----------------------------------------------------------------
$( "#btnMult" ).on( "click", function() {
    var rowsCols = getRowsCols();

    if(rowsCols[0].includes(NaN) || rowsCols[1].includes(NaN) ){
        alert("NO se han creado las matrices ");
    }else{
        if((rowsCols[0][0] == rowsCols[1][0]) || (rowsCols[0][0] == rowsCols[1][1]) ||
        (rowsCols[0][1] == rowsCols[1][1]) || (rowsCols[0][1] == rowsCols[1][0]) ){
            $('#nameOpera').empty();
            $('#nameOpera').append("Multiplicacion de Matrices ");
            var datos = JSON.stringify({
                mUno: getMatrix('matrizUno'),
                mDos: getMatrix('matrizDos')  
            });
            calcMa('btnMult', datos, 'matrixResult');
            
        }else{
            alert("las filas y columnas de las matrices son incongruentes!!"); 
        }
    }
});
//------------------------------------------------------------------------
function calcMa(btnName,datos, maResult){
    $.ajax({
        url: $('#'+btnName).attr('url'),
        data: {
            dats:datos,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        type: 'POST',
        dataType: 'json',
        success: function (data) {
            if (data.success) {

                showResult(data.matrResult, maResult );     
            }
            else {
                alert('error');
            }
        },
        error: function () {
            alert("Incongruencia en los datos!!");
        }
    });
}
//------------------------------------------------------------------------


//---------------------------------------------------------------------
function getMatrix(nametable){
    var dats = [];
    $('#'+nametable+' tr').each(function (index){
        var row = [];

        $($(this).find('td')).each(function (){
            row.push(parseFloat($(this).find('input').val()));
        });
        dats.push(row);

    });
    return dats;
}


//---------------------------------------------------------------------

function showResult(matrixResult, nameMatrix){
    $('#'+nameMatrix).empty();
    var content = ""
    $.each(matrixResult, function(i , row){
    
        content += "<tr>";
        $.each(row, function(j, dat){
            content += "<td>" + dat +"</td> ";
 
        });
        content += "</tr>";
    });
        
    $('#'+nameMatrix).append(content);
}

//---------------------------------------------------------------------

function createMatrix(rows, cols, id_mariz) {
    var content = ""
    for ( r = 0; r < rows; r++){
        content += "<tr>";
        for(c = 0; c < cols; c++){
            content += "<td><input type='number';-webkit-appearance: none;'></td> ";
        }
        content += "</tr>";
    }

    $('#'+id_mariz).append(content);
}

// ------------- AJUSTE CURVAS ------------


$('#btnCalcularAjus').on("click", function(){

    alert("btn ajuste de curvas");

    var datos = JSON.stringify({
        mUno: getMatrix('coeAjus')
    });

    calcEcua('btnCalcularAjus', datos, "reAjus","","");
});

$("#btnGraficarAjus").on("click", function(){

    var dats = getMatrix('coeAjus');
    var px = dats[0].toString();
    var py = dats[1].toString();
    var funcion = $("#reAjus").val();

    $("#imgUnoPoli").attr("src","/graficap/"+funcion+"/"+px+"/"+py);
    
});

$( "#btnDatosAjus" ).on( "click", function() {
    var longiAjus = $("#longiAjus").val(); 
    $("#coeAjus").empty();
    if(longiAjus == ""){
        alert("NO se han creado los campos ");
    }else{
        createMatrix(2, longiAjus, "coeAjus");
    }    
});

function getRowsCols(){
    var dat = [[parseInt($('#rowsUno').val(), 10),parseInt($('#colsUno').val(),10)],
                [parseInt($('#rowsDos').val(),10),parseInt($('#colsDos').val(),10)]];
    return dat;
}

function graficarFuncion(funcion, a, b, nameImg){

    $("#"+nameImg).attr("src","/grafica/"+funcion+"/"+a+"/"+b);
    
}

function calcEcua(btnName,datos, ouUno, ouDos, ouTres){
    $.ajax({
        url: $('#'+btnName).attr('url'),
        data: {
            dats:datos,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        type: 'POST',
        dataType: 'json',
        success: function (data) {
            if (data.success) {

                $("#"+ouUno).val(data.uno);
                $("#"+ouDos).val(data.dos);
                $("#"+ouTres).val(data.tres);
            }
            else {
                alert('error');
            }
        },
        error: function () {
            alert("Incongruencia en los datos!!");
        }
    });
}
//-------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------
//-------metodos simpson 1/ 3



$("#btnGraficarSin13").on("click", function(){
    var funcion = $("#ecuaSin13").val();
    if(funcion != null && funcion != ""){
        graficarFuncion(funcion, -12, 12, "imgUnoSin13");
    }
    else{   
        alert("Ingrese Una funcion");
    }
});

$("#btnIntervalosSin13").on("click", function(){

    var funcion = $("#ecuaSin13").val();
    var a = $("#inaSin13").val();
    var b = $("#inbSin13").val();

    if(funcion != null && funcion != "" && a != "" && b != ""){
        graficarFuncion(funcion, a, b, "imgDosSin13");
    }
    else{
        
        alert("Ingrese Una funcion");
    }

});

$( "#btnCalcularSin13" ).on( "click", function() {

    var ecuacion = $('#ecuaSin13').val();
    var _a = $('#inaSin13').val();
    var _b = $('#inbSin13').val();
    var _n = $('#parSin13').val();
    var datos = JSON.stringify({
        funcion:ecuacion,
        a:_a,
        b:_b,
        n:_n
    });
    var r = calcEcua("btnCalcularSin13", datos,"reSin13", "errSin13", "sd" );

});
//-------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------
//-------metodos simpson 3 / 8

$( "#btnCalcularSin38" ).on( "click", function() {

    var ecuacion = $('#ecuaSin38').val();
    var _a = $('#inaSin38').val();
    var _b = $('#inbSin38').val();
    var _n = $('#parSin38').val();
    var datos = JSON.stringify({
        funcion:ecuacion,
        a:_a,
        b:_b,
        n:_n
    });
    alert("datoss38 : " + datos);
    var r = calcEcua("btnCalcularSin38", datos,"reSin38", "errSin38", "" );

});

$("#btnIntervalosSin38").on("click", function(){

    var funcion = $("#ecuaSin38").val();
    var a = $("#inaSin38").val();
    var b = $("#inbSin38").val();

    if(funcion != null && funcion != "" && a != "" && b != ""){
        graficarFuncion(funcion, a, b, "imgDosSimp38");
    }
    else{
        
        alert("Ingrese Una funcion");
    }

});

$("#btnGraficarSin38").on("click", function(){
    var funcion = $("#ecuaSin38").val();
    if(funcion != null && funcion != ""){
        graficarFuncion(funcion, -12, 12, "imgUnoSimp38");
    }
    else{   
        alert("Ingrese Una funcion");
    }
});


//-------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------
//-------metodos montecarlo


$("#btnCalcMonte").on("click", function(){
    alert("btn monte carlo");
    var funcion = $("#ecuacionMonte").val();
    var _a = $("#aMonte").val();
    var _b = $("#bMonte").val();
    var _k = $("#kMonte").val();
    var _n = $("#nMonte").val();
    if(funcion != "" && _a != "" && _b != "" && _k != "" && _n != ""){
        var datos = JSON.stringify({
            funcion:funcion,
            a:_a,
            b:_b,
            k:_k,
            n:_n
        });
        alert("calc monte!! datos : " + datos);
        calcEcua("btnCalcMonte", datos, "resMonte","","");

    }else{
        alert("Hay Campos Vacios!!!")
    }
    
});

$("#btnGraIntervMonte").on("click", function(){

    var funcion = $("#ecuacionMonte").val();
    var a = $("#aMonte").val();
    var b = $("#bMonte").val();

    if(funcion != null && funcion != "" && a != "" && b != ""){
        graficarFuncion(funcion, a, b, "imgDosMonte");
    }
    else{
        alert("Ingrese Una funcion");
    }
});

$("#btnGenGrafMonte").on("click", function(){
    var funcion = $("#ecuacionMonte").val();
    if(funcion != null && funcion != ""){
        graficarFuncion(funcion, -12, 12, "imgUnoMonte");
    }
    else{   
        alert("Ingrese Una funcion");
    }
});

//-------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------
//-------metodos trapecios
$("#btnCalcularTrap").on("click", function(){
    alert("btn trapecios");
    var funcion = $("#ecuaTrap").val();
    var _a = $("#inaTrap").val();
    var _b = $("#inbTrap").val();
    var _n = $("#parTrap").val();
    if(funcion != "" && _a != "" && _b != "" && _n != ""){
        var datos = JSON.stringify({
            funcion:funcion,
            a:_a,
            b:_b,
            n:_n
        });
        alert("calc trapecios!! datos : " + datos);
        calcEcua("btnCalcularTrap", datos, "reTrap","errTrap","");

    }else{
        alert("Hay Campos Vacios!!!")
    }
    
});

$("#btnIntervalosTrap").on("click", function(){

    var funcion = $("#ecuaTrap").val();
    var a = $("#inaTrap").val();
    var b = $("#inbTrap").val();

    if(funcion != null && funcion != "" && a != "" && b != ""){
        graficarFuncion(funcion, a, b, "imgDosTrap");
    }
    else{
        alert("Ingrese Una funcion");
    }
});

$("#btnGraficarTrape").on("click", function(){
    var funcion = $("#ecuaTrap").val();
    if(funcion != null && funcion != ""){
        graficarFuncion(funcion, -12, 12, "imgUnoTrap");
    }
    else{   
        alert("Ingrese Una funcion");
    }
});

//-------------------------------------------------------------------------------------------------------
//-------------------------------------------------------------------------------------------------------
//-------metodos rectangulos

$("#btnIntervalosRect").on("click", function(){

    var funcion = $("#ecuaRect").val();
    var a = $("#inaRect").val();
    var b = $("#inbRect").val();

    if(funcion != null && funcion != "" && a != "" && b != ""){
        graficarFuncion(funcion, a, b, "imgDosRect");
    }
    else{
        alert("Ingrese Una funcion");
    }
});

$("#btnGraficarRect").on("click", function(){
    var funcion = $("#ecuaRect").val();
    if(funcion != null && funcion != ""){
        graficarFuncion(funcion, -12, 12, "imgUnoRect");
    }
    else{   
        alert("Ingrese Una funcion");
    }
});
$("#btnCalcularRect").on("click", function(){
    alert("btn Rectangulos");
    var funcion = $("#ecuaRect").val();
    var _a = $("#inaRect").val();
    var _b = $("#inbRect").val();
    var _n = $("#parRect").val();
    if(funcion != "" && _a != "" && _b != "" && _n != ""){
        var datos = JSON.stringify({
            funcion:funcion,
            a:_a,
            b:_b,
            n:_n
        });
        alert("calc rectangulos!! datos : " + datos);
        calcEcua("btnCalcularRect", datos, "extIzRect","extDeRect","puntoMedRect");

    }else{
        alert("Hay Campos Vacios!!!")
    }
    
});