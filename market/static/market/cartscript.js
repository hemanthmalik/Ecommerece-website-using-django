function sumValues(cart){
    var sum = 0
    for (i in cart){
        sum += cart[i][0];
    }
    return sum;
}
if ((localStorage.getItem('cart') == 0) || (localStorage.getItem('cart') == null)){
    var cart = {};
}
else{
    cart = JSON.parse(localStorage.getItem('cart'));
    var totalCart = sumValues(cart);
    document.getElementById("cartVal").innerHTML = "Cart(" + totalCart + ")";
}
$('.cart').click(function(){
    console.log("clicked");
    var idStr = this.id.toString();
    var itemName = this.name;
    console.log(itemName);
    console.log(idStr);
    if (cart[idStr] != undefined){
        cart[idStr][0] += 1;
    }
    else{
        cart[idStr] = [1, itemName];
    }
    console.log(cart);
    var totalCart = sumValues(cart);
    console.log(totalCart);
    $('[data-toggle="popover"]').attr('data-content', JSON.stringify(localStorage.getItem('cart')));
    var cartshit = document.getElementById("cartVal");
    updateCart(cart);
    cartshit.innerHTML = "Cart(" + totalCart + ")";
    localStorage.setItem('cart', JSON.stringify(cart));
});
$(document).ready(function(){
    console.log("page loaded");
    updateCart(cart);
});
$('[data-toggle="popover"]').popover({
    trigger: 'hover click',
    html: true,
    sanitize: false,
  });
  
function popoverUpdate(cart){
    console.log("pop update");
    var popoverdata = "<ol>"
    for (i in cart){
        popoverdata +="<li>" + cart[i][1] + ", Quantity : " + cart[i][0] + "</li>";
    }
    popoverdata += "</ol><a href='javascript:void(0)' onclick='clearCart();' class='btn btn-outline-danger mr-3'>ClearCart</a><a href='/market/checkout/' class='btn btn-primary'>Checkout</a>";
    $('#cartVal').attr('data-content', popoverdata);
    $('#cartVal').popover('show');
}

function updateCart(cart){
    for (val in cart){
        $("#quantityBtn"+val).html("<div class='btn-group' role='group' aria-label='Basic example'><button type='button' id='minus" + val +"' class='btn btn-primary minus'>-</button><button type='button' class='btn btn-outline-secondary'>"+ cart[val][0]+"</button><button type='button' class='btn btn-primary plus' id='plus" + val + "' name='"+ cart[val][1] + "'>+</button></div>");
        if(cart[val][0] == 0){
            delete cart[val];
        }
    }
    popoverUpdate(cart);
}
$('.divpr').on('click', 'button.minus', function(){
    values = this.id.toString().slice(5,);
    if (cart[values] != undefined){
        if (cart[values][0] > 0){
            cart[values][0] -= 1;
        }
        console.log(values);
        console.log(cart[values]);
        console.log(cart);
        localStorage.setItem('cart', JSON.stringify(cart));
        var totalCart = sumValues(cart);
        $('[data-toggle="popover"]').text("Cart(" + totalCart + ")");
        updateCart(cart);
    }

    });
$('.divpr').on('click', 'button.plus', function(){
    values = this.id.toString().slice(4,);
    console.log(values);
    if(cart[values]==undefined){
        cart[values] = [0, this.name];
    }
    cart[values][0] += 1;
    console.log(cart)
    console.log(cart[values][0]);
    localStorage.setItem('cart', JSON.stringify(cart));
    var totalCart = sumValues(cart);
    $('[data-toggle="popover"]').text("Cart(" + totalCart + ")");
    updateCart(cart);
});
function clearCart(){
    localStorage.setItem('cart', "{}");
    location.reload(false);
}

function cartSend(){
    $('#cartItems').val(JSON.stringify(cart));
    $('#cartForm').submit();
}
