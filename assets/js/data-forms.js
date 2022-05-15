// Dynamic forms to edit YAML data files through staticman
$(function() {
    $("#item-form").submit(function() {
        var form = this;

        $(form).addClass("disabled");
        $("#item-form-submit").html(
        'Sending...'
        );

        $.ajax({
        type: $(this).attr("method"),
        url: $(this).attr("action"),
        data: $(this).serialize(),
        contentType: "application/x-www-form-urlencoded",
        success: function(data) {
            window.location.reload(true);
        },
        error: function(err) {
            console.log(err);
            $("#item-form-submit").html("Enviar");
            $("#item-static-form .js-notice-text")
            .removeClass("text-success")
            .addClass("text-danger");
            showAlert(
                "<strong>Sorry, there was an error with your submission.</strong><br>Please make sure all required fields have been completed and try again."
            );
            $(form).removeClass("disabled");
        }
        });

        return false;
    });

});

function showAlert(message) {
    $("#item-form-submit .js-notice").show()[0];
    $("#item-form-submit .js-notice-text").html(message);
}

function hideAlert() {
    $("#item-form-submit .js-notice").hide()[0];
    $("#item-form-submit .js-notice-text").html("");
}

function toggleDisplay(e) {
    if (typeof e === "string") {
        e = document.getElementById(e);
    }
    if (e.style.display === "none") {
        e.style.display = "";
    } else {
        e.style.display = "none";
    }
}

document.getElementById("new-item").onclick = function() {
    toggleDisplay("item-static-form");
    toggleDisplay("item-content");
};

document.getElementById("cancel-form").onclick = function() {
    toggleDisplay("item-static-form");
    toggleDisplay("item-content");
};

$("#item-form-submit .js-notice").hide()[0];