$(function(){
    function setVisibility(elem, bool){
        if(bool)    
            elem.show()
        else
            elem.hide()
    }
    
    function setVisibilityWidth(elem, bool){
        elem.css('visibility', bool ? '' : 'hidden')
    }
    
    $('.exercice').each(function(){
        var self = $(this)
        
        function getNum() {
            return (self.data('current') || 1) - 1
        }
        
        self.find('img').each(function(){
            this.addEventListener('contextmenu', function(ev) {
                ev.preventDefault()
                if(getNum() > 0) {
                    setNum(getNum() - 1)
                }
            })
        })
        
        function setNum(num) {
            self.data('current', num + 1)
            
            self.find('.slide').each(function(i){
                setVisibility($(this), i == num)
            })
            
            setVisibilityWidth(
                self.find('.next:not(.slide,h2)'),
                !!self.find('.slide')[num + 1]
            )
            
            setVisibilityWidth(
                self.find('.prev:not(.slide,h2)'), 
                !!self.find('.slide')[num - 1]
            )
            
            if(num == 0) {
                setVisibilityWidth(self.find('.next.normal'), false)
            } else {
                setVisibilityWidth(self.find('.next.solution'), false)
            }
        }
        
        self.find('.next').on('click', function(){
            setNum(getNum() + 1)
        })
        
        self.find('.prev').on('click', function(){
            setNum(getNum() - 1)
        })
        
        self.find('.slide.next').attr('title', function(i){
            if(i == 0)
                return "Voir la solution"
            return "Suivant"
        })
        
        setNum(getNum() || 0)
    })
})