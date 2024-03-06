//review form
//make review without refreshing page
$(".comment-form").submit(function(e){
    e.preventDefault();
    //Get all data submitted using json

    $.ajax({
        data:$(this).serialize(),
        method:$(this).attr("method"),
        url:$(this).attr("action"),
        dataType:"json",//wat we are returning from the server

        success:function(response){
            console.log("Successful review submission")
            if (response.bool == true){
                $("#review-para").html("Thanks for your feedback.Feel appreciated")
                $(".comment-form").hide()
                
               
                let _html = '<div class="review-card">';
                _html += '<p>' + response.context.review + '</p>';
                _html += '<span class="star-rating">';
                for (let i = 0; i < response.context.rating; i++) {
                    _html += '<i class="fas fa-star"></i>';
                }
                _html += '</span>';
                _html += '<span class="user-name"><i class="fas fa-user"></i>' + response.context.user + '</span>';
                _html += '<span class="review-date">Just now</span>';
                _html += '</div>';

                $(".reviews-container").prepend(_html);
            }
            
        }
    })

})
//FILTER PRODUCTS
$(document).ready(function(){
    $(".filter-checkbox").on("click",function(){
        let filterObject={}
        $(".filter-checkbox").each(function(i){
            let filterValue=$(this).val()
            let filterKey=$(this).data("filter")
            filterObject[filterKey]=Array.from(document.querySelectorAll('input[data-filter=' + filterKey + ']:checked')).map(function(e){
                return e.value
            })
        })
        console.log("FilterObject is:",filterObject)
        $.ajax({
            url:'/filter-product',
            data:filterObject,
            dataType:'json',
            beforeSend:function(){
                console.log("Filtering.....")
            },
            success:function(response){
                console.log(response);
                console.log("Filtered successfully")
                $("#filtered-products").html(response.data)
            }
        })
    })

})

//ADD ITEMS TO CART
$(".add-to-cart-btn").on("click",function(){
    let productId=$(".product-id").val()
    let qty=$(".product-quantity").val()
    let productPrice=$(".current-price").text()
    let productTitle=$(".product-title").val()
    let thisVal=$(this)

    $.ajax({
        url:'/add-to-cart',
        data:{
            'qty':qty,
            'productTitle':productTitle,
            'productId':productId,
            'productPrice':productPrice
        },
        dataType:'json',
        beforeSend:function(){
            console.log("Adding to cart....")
        },
        success:function(response){
            console.log(response)
            console.log("Added to cart successfully")
            $(".cart-count").text(response.cart_count)
            thisVal.html("Added to cart")
        }
    })

})