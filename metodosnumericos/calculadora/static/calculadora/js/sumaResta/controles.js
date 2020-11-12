
function createMatrix(rows, cols, id_mariz) {
    var content = ""
    for ( r = 0; r < rows; r++){
        content += "<tr>";
        for(c = 0; c < cols; c++){
            content += "<td><input type='number' style = 'width: 40px;-webkit-appearance: none;'></td> ";
        }
        content += "</tr>";
    }


    $('#'+id_mariz).append(content);
}

function getRowsCols(){
    var dat = [[parseInt($('#rowsUno').val(), 10),parseInt($('#colsUno').val(),10)],
                [parseInt($('#rowsDos').val(),10),parseInt($('#colsDos').val(),10)]];
    return dat;
}


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
    var rows = $('#rowsUno').val();
    var cols = $('#colsUno').val();
    if(rows == ""){
        alert("Digite el numero de filas y columnas correcto !!!");
    }else{
        createMatrix(rows, cols, "matrizDos");
    }
    
});
$( "#btnDeleteOne" ).on( "click", function() {
    $('#matrizUno').empty();
    
});
$( "#btnDeleteTwo" ).on( "click", function() {
    $('#matrizDos').empty();    
});


$( "#btnSum" ).on( "click", function() {
    var rowsCols = getRowsCols();

    if(rowsCols[0].includes(NaN) || rowsCols[1].includes(NaN) ){
        alert("NO se han creado las matrices ");
    }else{
        if(rowsCols[0][0] == rowsCols[1][0] && rowsCols[0][1] == rowsCols[1][1]){

            calcSum();
            
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
            calcRest();
        }else{
            alert("las filas y columnas de las matrices deben ser iguales!!");
        }
    }
});
//------------------------------------------------------------------------
function calcSum(){
    $.ajax({
        url: $('#btnSum').attr('url'),
        data: {
            dats: JSON.stringify({
                mUno: getMatrix('matrizUno'),
                mDos: getMatrix('matrizDos')  
            }),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        type: 'POST',
        dataType: 'json',
        success: function (data) {
            if (data.success) {
               showResult(data.matrResult);     
            }
            else {
                alert('error');
            }
        },
        error: function () {
            alert("no paso nada con el ajax!!");
        }
    });
}
//------------------------------------------------------------------------
function calcRest(){
    $.ajax({
        url: $('#btnRest').attr('url'),
        data: {
            dats: JSON.stringify({
                mUno: getMatrix('matrizUno'),
                mDos: getMatrix('matrizDos')  
            }),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        type: 'POST',
        dataType: 'json',
        success: function (data) {
            if (data.success) {
               showResult(data.matrResult);     
            }
            else {
                alert('error');
            }
        },
        error: function () {
            alert("no paso nada con el ajax!!");
        }
    });
}
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

function showResult(matrixResult){
    $('#matrixResult').empty();
    var content = ""
    $.each(matrixResult, function(i , row){
    
        content += "<tr>";
        $.each(row, function(j, dat){
            content += "<td>" + dat +"</td> ";
 
        });
        content += "</tr>";
    });
        
    $('#matrixResult').append(content);
}

//---------------------------------------------------------------------
