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
                
               
                let _html='<div class="review-card">'
                    _html+='<p>'+response.context.review+'</p>'
                    for(let i=1;i<response.context.rating;i++){
                        _html+='<i class="fas fa-star"></i>'
                    }
                    _html+='<span class="user-name"><i class="fas fa-user"></i>'+response.context.user+'</span>'
                    _html+='<span class="review-date">'+ response.context.review +'</span>'
                    _html+='</div>'

                    $(".reviews-container").prepend(_html)
            }
            
        }
    })

})