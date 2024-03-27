//review form
//make review without refreshing page
$(".comment-form").submit(function (e) {
    e.preventDefault();
    //Get all data submitted using json

    $.ajax({
        data: $(this).serialize(),
        method: $(this).attr("method"),
        url: $(this).attr("action"),
        dataType: "json",//wat we are returning from the server

        success: function (response) {
            console.log("Successful review submission")
            if (response.bool == true) {
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
$(document).ready(function () {
    $(".filter-checkbox").on("click", function () {
        let filterObject = {}
        $(".filter-checkbox").each(function (i) {
            let filterValue = $(this).val()
            let filterKey = $(this).data("filter")
            filterObject[filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + filterKey + ']:checked')).map(function (e) {
                return e.value
            })
        })
        console.log("FilterObject is:", filterObject)
        $.ajax({
            url: '/filter-product',
            data: filterObject,
            dataType: 'json',
            beforeSend: function () {
                console.log("Filtering.....")
            },
            success: function (response) {
                console.log(response);
                console.log("Filtered successfully")
                $("#filtered-products").html(response.data)
            }
        })
    })

})

//ADD ITEMS TO CART
$(".add-to-cart-btn").on("click", function () {
    let productCard = $(this).closest('.product-card, .product-detail-card');
    let productId = productCard.find(".product-id").val();
    let qty = productCard.find(".product-quantity").val();
    let productPrice = parseFloat(productCard.find(".current-price").text());
    let productTitle = productCard.find(".product-title").val();
    let productImage = productCard.find(".product-img .product-image").attr("src");

    let thisVal = $(this);

    $.ajax({
        url: '/add-to-cart',
        data: {
            'qty': qty,
            'productTitle': productTitle,
            'productId': productId,
            'productPrice': productPrice,
            'productImage': productImage,
        },
        dataType: 'json',
        beforeSend: function () {
            console.log("Adding to cart....")
        },
        success: function (response) {
            console.log(response)
            console.log("Added to cart successfully")
            $(".cart-count").text(response.cart_count)
            thisVal.html("Added to cart")
        }
    })

})
//DELETE PRODUCTS FROM CART
$("#async-cart").on("click", ".delete-product", function () {
    let productId = $(this).attr("data-product");
    let thisVal = $(this);

    console.log("ProductId: ", productId);
    $.ajax({
        url: "/delete-from-cart",
        data: {
            "id": productId
        },
        dataType: "json",
        beforeSend: function () {
            thisVal.hide();
        },
        success: function (response) {
            thisVal.show();
            console.log("deleted successfully");
            $(".cart-count").text(response.cart_count);
            $("#async-cart").html(response.data);
        }
    });
});

//ADD TO WISHLIST
$(".add-to-wishlist").on('click', function () {
    var product_id = $(this).attr('data-product-item');
    var this_val = $(this);
    console.log(product_id);

    $.ajax({
        url: "/add-to-wishlist",
        data: {
            product_id: product_id
        },
        dataType: 'json',
        beforeSend: function () {
            this_val.css('color','red')
        },
        success:function(response){
            if (response.bool==true){
                var wishlistCount = parseInt($(".wish-count").text());
                wishlistCount++;
                $(".wish-count").text(wishlistCount);
                $("#wishlist").html(response.data);
    
                console.log("added")
            }
        }
    });
});

$(".remove-wishitem").on('click', function() {
    let this_val = $(this);
    let id = $(this).attr("data-wishlist-product");
    console.log(this_val);
    console.log("wishlist id :", id);
    let productCard = $(this).closest('.product-card');

    $.ajax({
        url: "/remove-from-wishlist",
        data: {
            "id": id,
        },
        dataType: "json",
        beforeSend: function() {
            console.log("Deleting wishlist item");
        },
        success: function(response) {
            var wishlistCount = parseInt($(".wish-count").text());
            wishlistCount--;
            $(".wish-count").text(wishlistCount);

            // Remove the product card from the DOM
            productCard.remove();
        }
    });
});