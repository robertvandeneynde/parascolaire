$(function(){
    function setVisibility(elem, bool){
        elem[bool ? 'show' : 'hide']()
    }
    
    function setVisibilityWidth(elem, bool){
        elem.css('visibility', bool ? '' : 'hidden')
    }
    
    $('.slideshow').each(function(){
        var self = $(this)
        
        function getNum() {
            return (self.data('current') || 1) - 1
        }
        
        self.find('slide .next').each(function(){
            this.addEventListener('contextmenu', function(ev) {
                if(!ev.ctrlKey) {
                    ev.preventDefault()
                    if(getNum() > 0) {
                        setNum(getNum() - 1)
                    }
                }
            })
        })
        
        function setNum(num) {
            var N = self.find('.slide').length
            num = (num + N) % N // python "num"
            self.data('current', num + 1)
            
            self.find('.slide').each(function(i){
                setVisibility($(this), i == num)
            })
            
            //setVisibilityWidth(
                //self.find('.next:not(.slide,h2)'),
                //!!self.find('.slide')[num + 1])
            
            setVisibilityWidth(
                self.find('.prev:not(.slide,h2)'), 
                !!self.find('.slide')[num - 1])
        }
        
        self.find('.next').on('click', function(){
            setNum(getNum() + parseInt(this.getAttribute('n') || this.getAttribute('s') || '1'))
        })
        
        self.find('.prev').on('click', function(){
            setNum(getNum() - parseInt(this.getAttribute('n') || this.getAttribute('s') || '1'))
        })
        
        self.find('.goto').on('click', function(){
            setNum(this.getAttribute('n') ? parseInt(this.getAttribute('n')) :
                   this.getAttribute('s') ? (function(x){ return x < 0 ? x : x - 1 })(parseInt(this.getAttribute('s'))) : 
                   -1)
        })
        
        setNum(getNum() || 0)
    })
})
