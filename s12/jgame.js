
var table= $('table tr');


// get the colu, of thr recent click
var col = $("table button").on('click',function(){
    console.log($(this).closest('td').index());
    })

// get the last column with grey color
function checkBottom(col) {
    var getColor

}
