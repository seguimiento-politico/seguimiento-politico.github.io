$(function() {
    $('.collapse').on('shown.bs.collapse', function(e) {
        var $card = $(this).closest('.accordion-item');
        var $open = $($(this).data('parent')).find('.collapse.show');
        
        var additionalOffset = 0;
        if($card.prevAll().filter($open.closest('.accordion-item')).length !== 0)
        {
            additionalOffset =  $open.height();
        }
        $('html,body').animate({
        scrollTop: $card.offset().top - additionalOffset }, 100);
    });
});