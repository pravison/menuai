
var updateBtns = document.getElementsByClassName('update-cart')

for( var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var menuId = this.dataset.menu
        var action = this.dataset.action

        //console.log('menuId:', menuId, 'action:', action )

        console.log('User:', user)
        if(user === 'AnonymousUser'){
            addCookieItem(menuId , action)
        }else{
            updateUserOrder(menuId , action)
        }
    }) 
}

function addCookieItem(menuId , action){
    //console.log('user is not logged in')

    if (action == 'add'){
        if (cart[menuId] == undefined){
            cart[menuId] = {'quantity' : 1}
        }else{
            cart[menuId]['quantity'] += 1
        }
    }
    if (action == 'remove'){
        cart[menuId]['quantity'] -= 1
        if (cart[menuId]['quantity'] <= 0){
            console.log('remove item')
            delete cart[menuId]
        }
    }
    if (action == 'clear'){
        delete cart[menuId]
    }
    console.log('cart:', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
    location.reload()
}

function updateUserOrder(menuId , action){
    
    console.log('user is logged in sending data...')

    var url = '/update_item/'
    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken
        },

        body:JSON.stringify({'menuId': menuId , 'action': action})
    })
    .then((response)=>{
        return response.json()
    })

    .then((data)=>{
        location.reload()
        console.log('data:', data)
    })
    
}