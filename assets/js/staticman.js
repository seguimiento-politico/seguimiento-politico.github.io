$(function() {
    // Static comments
    $("#comment-form").submit(function() {
        var form = this;

        $(form).addClass("disabled");
        $("#comment-form-submit").html(
        'Sending...'
        );

        $.ajax({
        type: $(this).attr("method"),
        url: $(this).attr("action"),
        data: $(this).serialize(),
        contentType: "application/x-www-form-urlencoded",
        success: function(data) {
            $("#comment-form-submit")
            .html("Submitted")
            .addClass("btn--disabled");
            $("#respond .js-notice")
            .removeClass("danger")
            .addClass("success");
            $("#respond form").hide()[0].reset();
            showAlert(
                '<strong>Thanks for your comment!</strong><br>It is <a href="https://github.com/seguimiento-politico/seguimiento-politico.github.io/pulls">currently pending</a> and will show on the site once approved. You will be notified if your comment is approved.'
            );
        },
        error: function(err) {
            console.log(err);
            $("#comment-form-submit").html("Submit Comment");
            $("#respond .js-notice")
            .removeClass("success")
            .addClass("danger");
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
    $("#respond .js-notice").removeClass("hidden");
    $("#respond .js-notice-text").html(message);
}

function hideAlert() {
    $("#respond .js-notice").addClass("hidden");
    $("#respond .js-notice-text").html("");
}

function copyTextFromElement(e) {
    if (document.selection) { // IE
        var range = document.body.createTextRange();
        range.moveToElementText(document.getElementById(e));
        range.select();
    } else if (window.getSelection) {
        var range = document.createRange();
        range.selectNode(document.getElementById(e));
        window.getSelection().removeAllRanges();
        window.getSelection().addRange(range);
        document.execCommand("copy");
        window.getSelection().removeAllRanges();
    }
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

// Staticman comment replies
// modified from Wordpress https://core.svn.wordpress.org/trunk/wp-includes/js/comment-reply.js
// Released under the GNU General Public License - https://wordpress.org/about/gpl/
var addComment = {
    moveForm: function(commId, parentId, respondId, postId) {
        $("#respond").show()[0];
        hideAlert();
        var div,
        element,
        style,
        cssHidden,
        t = this,
        comm = t.I(commId),
        respond = t.I(respondId),
        commentHeadingText = t.I("comment-heading-text"),
        cancel = t.I("cancel-comment-reply-link"),
        parent = t.I("comment-replying-to"),
        post = t.I("comment-post-slug"),
        commentForm = respond.getElementsByTagName("form")[0];

        if (!comm || !respond || !cancel || !parent || !commentForm) {
            return;
        }

        t.respondId = respondId;
        postId = postId || false;

        if (!t.I("sm-temp-form-div")) {
            div = document.createElement("div");
            div.id = "sm-temp-form-div";
            div.style.display = "none";
            respond.parentNode.insertBefore(div, respond);
        }

        comm.parentNode.insertBefore(respond, comm.nextSibling);
        if (post && postId) {
            post.value = postId;
        }
        parent.value = parentId;
        cancel.style.display = "";
        commentHeadingText.innerText = "Respuesta";

        cancel.onclick = function() {
            $("#respond").hide()[0];
            var t = addComment,
                temp = t.I("sm-temp-form-div"),
                respond = t.I(t.respondId);
            
            if (!temp || !respond) {
                return;
            }

            t.I("comment-replying-to").value = null;
            temp.parentNode.insertBefore(respond, temp);
            temp.parentNode.removeChild(temp);
            this.style.display = "none";
            this.onclick = null;
            commentHeadingText.innerText = "Deja un comentario";
            return false;
        };

        /*
        * Set initial focus to the first form focusable element.
        * Try/catch used just to avoid errors in IE 7- which return visibility
        * 'inherit' when the visibility value is inherited from an ancestor.
        */
        try {
            for (var i = 0; i < commentForm.elements.length; i++) {
                element = commentForm.elements[i];
                cssHidden = false;

                // Modern browsers.
                if ("getComputedStyle" in window) {
                style = window.getComputedStyle(element);
                // IE 8.
                } else if (document.documentElement.currentStyle) {
                style = element.currentStyle;
                }

                /*
                * For display none, do the same thing jQuery does. For visibility,
                * check the element computed style since browsers are already doing
                * the job for us. In fact, the visibility computed style is the actual
                * computed value and already takes into account the element ancestors.
                */
                if (
                (element.offsetWidth <= 0 && element.offsetHeight <= 0) ||
                style.visibility === "hidden"
                ) {
                cssHidden = true;
                }

                // Skip form elements that are hidden or disabled.
                if ("hidden" === element.type || element.disabled || cssHidden) {
                continue;
                }

                element.focus();
                // Stop after the first focusable element.
                break;
            }
        } catch (er) {}

        return false;
    },

    I: function(id) {
        return document.getElementById(id);
    }
};

//hide form on innitial load
$("#respond").hide()[0];

//show form if new comment button clicked
//show form if new comment button clicked
document.getElementById("new-comment-link").onclick = function() {
    toggleDisplay("respond");
};
