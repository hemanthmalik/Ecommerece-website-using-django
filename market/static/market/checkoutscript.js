console.log(cart);

$(document).ready(function(){
    $.ajax({url: "/market/checkout/", method: "POST", data: {"hello": 50, "csrfmiddlewaretoken": csrf}}).done(function(data){console.log(data)});
    console.log(totalCart);
    var checkoutItems = document.getElementById('checkoutItems');
    var checkDisplay = "";
    if (totalCart > 0){
        $('#itemsJson').val(JSON.stringify(cart));
        for (i in cart){
            if (cart[i][0] > 0){
            checkDisplay += `<li class="list-group-item d-flex justify-content-between align-items-center">` + cart[i][1] +
            `<span class="badge badge-primary badge-pill">` + cart[i][0] + `</span>
        </li>`;
            }
        }
    }
    else{
        checkDisplay = `<li class="list-group-item d-flex justify-content-between align-items-center">
        Your cart is empty...
    </li>`;
    }
    checkoutItems.innerHTML = checkDisplay;
})