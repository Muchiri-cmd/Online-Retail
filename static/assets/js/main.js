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
            if (response.bool== true){
                $("#review-para").html("Thanks for your feedback.Feel appreciated")
                $(".comment-form").hide()
            }
        }
    })

})