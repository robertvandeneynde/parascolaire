$(function(){
    if(location.hash) {
        var hash = document.location.hash;
        if(hash.length > 1) {
            var ahash = hash 
            var target = $(hash);
            target = target.length ? target : $('[name=' + hash.slice(1) +']');
            if (target.length) {
                if(target.offset().top > 2000)
                    location.hash = ahash;
                else {
                    $('html,body').animate({
                        scrollTop: target.offset().top
                    }, 500, void 0, function(){
                        location.hash = ahash
                    })
                } 
            }
        }
    }
    
    $('a[href^=#]').click(function(ev) {
        if($(this).attr('href') == '#') {
            $('html,body').animate({
                scrollTop: 0
            }, 500, void 0, function(){
                location.hash = ''
            });
            ev.preventDefault();
        } else if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
            if(this.hash.length > 1) {
                var ahash = this.hash 
                var target = $(this.hash);
                target = target.length ? target : $('[name=' + this.hash.slice(1) +']');
                if (target.length) {
                    $('html,body').animate({
                        scrollTop: target.offset().top
                    }, 500, void 0, function(){
                        location.hash = ahash
                    });
                    ev.preventDefault();
                }
            }
        }
    });
})