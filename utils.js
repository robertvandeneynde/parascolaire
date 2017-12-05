var utils = (function(){
    
    function dedentPreCode() {
        // call python textwrap.dedent function on all "pre code"
        $('pre code').each(function(){
            var lines = this.innerHTML.split('\n')
            
            // console.log('lines', lines)
            
            while(/^\s*$/.exec(lines[0]))
                lines.shift()
            while(/^\s*$/.exec(lines[lines.length - 1]))
                lines.pop()
            
            var min = 1/0
            for(var i = 0; i < lines.length; i++)
                if(! /^\s*$/.exec(lines[i])) // line not empty
                    min = Math.min(min, /\s*/.exec(lines[i])[0].length)
                // else console.log('skipping', [lines[i]])
            
            // console.log('min', min)
                    
            this.innerHTML = lines.map(function(l){
                return l.substr(min)
            }).join('\n')
        })
    }
    
    function makeLinksBetweenTitles(titleTag, prevHref, nextHref) {
        if(titleTag == null) titleTag = 'h2';
        
        var H = $(titleTag).map(function(){
            return $(this)
        })
        
        var I = $(titleTag).map(function(x){
            return '#' + this.id
        })
        
        var N = H.length
        
        for(var i = 0; i < N; i++) {
            var txt = H[i].text()
            H[i].empty().append(
                $('<a class=totop>').attr('href', prevHref).css('margin-right', 5)
            ).append(
                $('<a class=prev>').attr('href', i == 0 ? prevHref : I[i-1])
            ).append(
                $('<a>').text(txt).attr('href', I[i])
            ).append(
                $('<a class=next>').attr('href', i == N-1 ? nextHref : I[i+1])
            ).append(
                $('<a class=permalink>').attr('href', I[i]).attr('title', 'Permalink')
            )
        }
    }
    
    function makeTitleLinks() {
        makeLinksBetweenTitles('h2', '#')
    
        // convention : each section that has h3, must have a name=id where id is the id of the corresponding h2
        var A = $.makeArray( $('h2').map(function(){ return $(this).attr('id') }) )
        A.forEach(function(x,i){
            makeLinksBetweenTitles('section[name="%%"] h3'.replace('%%', x), '#' + A[i], (A[i+1] ? '#' + A[i+1] : null))
        })
    }
    
    function smoothLinks() {
        if(location.hash) {
            var hash = document.location.hash;
            if(hash.length > 1) {
                var ahash = hash 
                var target = $(document.getElementById(hash.slice(1)));
                target = target.length ? target : $('[name="' + hash.slice(1) +'"]');
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
                    var target = $(document.getElementById(this.hash.slice(1)));
                    target = target.length ? target : $('[name="' + this.hash.slice(1) +'"]');
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
    }
    
    return {
        dedentPreCode: dedentPreCode,
        makeTitleLinks: makeTitleLinks,
        smoothLinks: smoothLinks,
    }
})();
