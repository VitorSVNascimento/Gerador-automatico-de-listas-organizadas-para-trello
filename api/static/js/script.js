const ENTER_CODE = 13

if(typeof document.hidden !== "undefined") {// visibility API supported!
	
	function chickenRun(){	
	
	var domSwing = document.getElementById('swinging'), 
	domShadow = document.getElementById('shadow');
	
		if (document.hidden) {
			domSwing.style.animationPlayState = "paused";
			domShadow.style.animationPlayState = "paused";
		} else {
			domSwing.style.animationPlayState = "running";
			domShadow.style.animationPlayState = "running";
		}
	}
	
	document.addEventListener('visibilitychange', chickenRun, false);
	
}



$(document).ready(function () {
    $("form").submit(function (event) {
        $('.modal').modal();
        $('#loading_modal').modal('open');

        // $("#loading_div").addClass("active")
        // $("#loading_div").show()

        var prompt = $("#prompt").val();
        
        $.ajax({
            type: "POST",
            url: "/generate",
            data: {prompt: prompt},
            success: function(response) {
                // $("#loading_div").hide()
                // $("#loading_div").removeClass("active")
                $("#trello_viewer").attr('src', response+".html");
                $("#trello_viewer_div").show()
                $("#loading_modal").modal('close')
            },
            error: function (xhr, status, error) {
                // Erro
                alert(error+" = "+xhr.responseText);
                // $("#loading_div").hide()
                // $("#loading_div").removeClass("active")
                // instance.close()
                $("#loading_modal").modal('close')
                // Adicione aqui o código para lidar com o erro, exibindo uma mensagem de erro, etc.
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
