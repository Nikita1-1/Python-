var button = document.getElementsByClassName('update-cart');
var cart_total = document.getElementById('cart-total');

for(i = 0; i<button.length; i++){
    button[i].addEventListener('click', function() {
//        current_quantity = parseInt(cart_total.innerText);
//        newQuantity = current_quantity + 1;
//        cart_total.innerText = newQuantity;
        // this keyword is going to represent our data-product in store.html
        var productId = this.dataset.product
        //same with action. Will be ADD
        var action = this.dataset.action
        updateUserOrder(productId, action)
        console.log('productId:', productId, 'action:', action)
})
};

function updateUserOrder(productId, action){
    var url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken
        },
        // what is going to be in the body
        body:JSON.stringify({'productId':productId, 'action':action})
    })
    // return promise from updateItem views.py
    .then((response) => {
        console.log(response)
        return response.json();
    })
    .then((data)=>{
        console.log('data', data)
        location.reload()
    });
    //we wil get the error because we dont have csrf token, we can create it via django documentation
}

