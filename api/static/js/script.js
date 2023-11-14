const ENTER_CODE = 13

$(document).ready(function () {
    $("form").submit(function (event) {

        $("#trello_viewer").hide() 
        $("#loading_div").addClass("active")
        $("#loading_div").show()
        var prompt = $("#prompt").val();
        
        $.ajax({
            type: "POST",
            url: "/generate",
            data: {prompt: prompt},
            success: function(response) {
                $("#loading_div").hide()
                $("#loading_div").removeClass("active")
                $("#trello_viewer").attr('src', response+".html");
                $("#trello_viewer").show()
        }
    });
    event.preventDefault();
    });

    $("form textarea").keydown(function (event) {
        if (event.which === ENTER_CODE && !event.shiftKey) {
            
            $("form").submit();
            event.preventDefault();
        }
    });


});
