// Dynamic forms to edit YAML data files through staticman
$(function() {
    $("#item-form").submit(function() {
        var form = this;

        $('#item-filename').val(slugify(document.getElementById('agent').value) + '_' + slugify(document.getElementById('title').value));

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

// from https://gist.github.com/codeguy/6684588
function slugify(text) {
    return text
      .toString()                           // Cast to string (optional)
      .normalize('NFKD')            // The normalize() using NFKD method returns the Unicode Normalization Form of a given string.
      .replace( /[\u0300-\u036f]/g, '' )   // remove all previously split accents
      .toLowerCase()                  // Convert the string to lowercase letters
      .trim()                                  // Remove whitespace from both sides of a string (optional)
      .replace(/\s+/g, '-')            // Replace spaces with -
      .replace(/[^\w\-]+/g, '')     // Remove all non-word chars
      .replace(/\-\-+/g, '-');        // Replace multiple - with single -
  }
    
function showAlert(message) {
    $("#item-form-wrapper .js-notice").show()[0];
    $("#item-form-wrapper .js-notice-text").html(message);
}

function hideAlert() {
    $("#item-form-wrapper .js-notice").hide()[0];
    $("#item-form-wrapper .js-notice-text").html("");
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

hideAlert();

document.getElementById("new-item").onclick = function() {
    toggleDisplay("item-form-wrapper");
    toggleDisplay("item-content");
};

document.getElementById("cancel-form").onclick = function() {
    toggleDisplay("item-form-wrapper");
    toggleDisplay("item-content");
};

