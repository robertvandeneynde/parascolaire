$(function(){
    if(!~location.hostname.indexOf("robertvandeneynde") && location.hostname != "") {
        $('#selfdomain').show().click(function(){
            $(this).fadeOut()
        })
    } else {
        $('#selfdomain').hide()
    }
    $('#vaisseau').each(function(){
        var self = $(this)
        self.css('position', 'relative')
        self.css('cursor', 'pointer')
        var i = 0;
        self.on('click', function(){
            if(i == 0) {
                var cl = setInterval(function(){
                    var x = 0.14 * i * i + (-4.0) * i
                    i += 1;
                    
                    if(x > $(window).width()) {
                        i = 0;
                        x = 0;
                        clearInterval(cl)
                    }
                    
                    self.css('left', x)
                }, 20)
            }
        })
    })
    
    $('.springpython').each(function(){
        var self = $(this)
        var v = 0;
        
        self.css('cursor', 'pointer')
        var i = 0;
        self.on('click', function(){
            v -= 150;
            if(i == 0) {
                var x = 0;
            
                var m = 1
                var k = 0.50;
                var alpha = 0.25;
                
                var eps = 2.0
                var dt = 0.10;
                
                var cl = setInterval(function(){
                    // var x = 2.5 * i;
                    var a = (- k * x - alpha * v) / m
                    v += a * dt
                    x += v * dt;
                    i += 1;
                    
                    // if(x > 360)
                    if(Math.abs(x) < eps && Math.abs(a) < eps && Math.abs(v) < eps)
                    {
                        i = 0;
                        x = 0;
                        clearInterval(cl)
                    }
                    
                    self.css('transform', 'rotate(' + x + 'deg)')
                }, 20)
            }
        })
    })
    
    $('#tetris').each(function(){
        var self = $(this)
        
        self.css('cursor', 'pointer')
        var i = 0;
        self.on('click', function(){
            if(i == 0) {
                var x = 0;
                var cl = setInterval(function(){
                    var x = 2.5 * i;
                    
                    if(x > 360)
                    {
                        i = 0;
                        x = 0;
                        clearInterval(cl)
                    } else {
                        i++
                    }
                    
                    self.css('transform', 'rotate(' + x + 'deg)')
                }, 20)
            }
        })
    })
    
    $('#invader').each(function(){
        var p = [
            [0, 0],
            [0, -35],
            [+400, -35],
            [-400, -35],
            [0, -35],
            [0, 0],
        ]
        
        var s = [0]
        for(var i = 1; i < p.length; i++)
            s[i] = Math.abs(p[i][0] - p[i-1][0]) + Math.abs(p[i][1] - p[i-1][1])
        
        var a = [0]
        for(var i = 1; i < s.length; i++)
            a[i] = a[i-1] + s[i];
        
        var self = $(this)
        self.css('position', 'relative')
        self.css('cursor', 'pointer')
        var i = 0;
        self.on('click', function(){
            if(i == 0) {
                var cl = setInterval(function(){
                    var x = 5.0 * i;
                    i += 1;
                    
                    var rx = 0;
                    var ry = 0;
                    
                    var found = false;
                    for(var j = 1; j < s.length; j++){
                        if(x < a[j]) {
                            var f = (x - a[j-1]) / s[j]
                            rx = (1-f) * p[j-1][0] + f * p[j][0]
                            ry = (1-f) * p[j-1][1] + f * p[j][1]
                            found = true;
                            break;
                        }
                    }
                    
                    if(! found){
                        i = 0;
                        rx = 0;
                        ry = 0;
                        clearInterval(cl)
                    }
                    
                    self.css({left: rx, top: ry});
                }, 20)
            }
        })
    })
    
    function setVector(vec, x, y, vx, vy, scale, space) {
        space = space || 0
        // vector have width=1, arbitrary height
        var v = Math.sqrt(vx*vx + vy*vy)
        var vt = Math.atan2(vy, vx)
        var l = scale * v
        var r = space + l / 2
        var mx = x + r * Math.cos(vt)
        var my = y + r * Math.sin(vt)
        vec.show().css('transform', 'translate(-50%,-50%) translate(' + mx + 'px,' + my + 'px) rotate(' + vt + 'rad) scale(' + l + ',1)')
    }
    
    function setupAnimations(self, beginAnimation) {
        self.click(function(ev){
            beginAnimation(20)
            ev.preventDefault()
        })
        
        self.on('contextmenu', function(ev){
            beginAnimation(100)
            ev.preventDefault()
        })
    }
    
    $('.jumpstick').each(function(){
        var self = $(this)
        var i = 0;
        var v = 0;
        var y = 0;
        
        var g = 0.30;
        
        var vecteur_vitesse = self.parent().find('.vecteur_vitesse')
        var vecteur_accel = self.parent().find('.vecteur_accel')
        var vecteurs = vecteur_vitesse.add(vecteur_accel)
        
        function applyPos() {
            // self.css({left: 0-self.width()/2, top: y-self.height()/2}); // width() = 0 sometimes
            self.css({left: 0-(64*169/293)/2, top: y-64/2});
        }
        
        applyPos()
        
        vecteurs.hide()
        
        setupAnimations(self, function(time){
            if(time == null)
                time = 20
            
            v -= 10.0;
            if(i == 0) {
                y = 0
                var cl = setInterval(function(){
                    // var x = 2.5 * i;
                    var a = g
                    
                    // display now to be consistent with non constant acceleration
                    applyPos()
                    setVector(vecteur_vitesse, 30, y, 0, v, 10, 0)
                    setVector(vecteur_accel, 40, y, 0, a, 100, 0)
                    
                    if(y > 0) 
                    {
                        i = 0;
                        y = 0;
                        v = 0;
                        applyPos()
                        clearInterval(cl)
                        vecteurs.hide()
                    } else {
                        v += a;
                        y += v;
                        i++
                    }
                    
                }, time)
            }
        })
    })
    
    $('.planet').each(function(){
        // dx, dy, v0x, v0y = 200, -50, 0, -10
        var x0 = 0;
        var y0 = 0;
        
        var sunX = 200
        var sunY = -50
        var v0x = 0 * Math.cos(90 * Math.PI / 180)
        var v0y = 10 * Math.sin(90 * Math.PI / 180) 
        
        var self = $(this)
        var i = 0
        var vx = 0
        var vy = 0
        var M = 10 * 1500 // 10 * 1500
        
        var x = x0;
        var y = y0;
        
        self.parent().find('.sun').css({left: sunX-32, top: sunY-32})
        
        var vecteur_vitesse = self.parent().find('.vecteur_vitesse')
        var vecteur_accel = self.parent().find('.vecteur_accel')
        var vecteurs = vecteur_vitesse.add(vecteur_accel)
        
        function applyPos() {
            self.css({left: x-16, top: y-16});
        }
        
        applyPos()
        vecteurs.hide()
        
        setupAnimations(self, function(time) {
            if(time == null)
                time = 20
                
            vx += v0x
            vy += v0y
            if(i == 0) {
                var turn = 0
                var turni = 0
                
                x = x0
                y = y0
                
                var cl = setInterval(function(){
                
                    var dx = sunX - x
                    var dy = sunY - y
                    var r2 = dx*dx + dy*dy
                    var r = Math.sqrt(r2)
                    var a = M / r2
                    var ndx = dx / r
                    var ndy = dy / r
                    var ax = ndx * a
                    var ay = ndy * a
                    
                    // display now to match acceleration
                    
                    applyPos()
                    setVector(vecteur_vitesse, x, y, vx, vy, 10, 16)
                    setVector(vecteur_accel, x, y, ax, ay, 300, 16)
                    
                    if(Math.abs(x+(vx+ax)-x0) < 5 && Math.abs(y+(vy+ay)-y0) < 5 && i-turni > 5) {
                        turni = i
                        turn += 1
                    }
                    
                    if(turn >= (time > 20 ? 1 : 2)) {
                        i = 0
                        vx = 0
                        vy = 0
                        x = 0
                        y = 0
                        applyPos()
                        vecteurs.hide()
                        clearInterval(cl)
                    } else {
                        // we see one frame of collision
                        vx += ax;
                        vy += ay;
                        x += vx
                        y += vy
                        i++;
                    }
                }, time)
            }
        })
    })
    
    $('.ressort').each(function(){
        var springX = 100
        var springY = 0

        var self = $(this)
        var i = 0
        var k = 1.5
        var v0x = self.attr('v0x') == null ? 0 : parseFloat(self.attr('v0x'))
        var v0y = self.attr('v0y') == null ? 20 : parseFloat(self.attr('v0y'))
        var times = self.attr('times') == null ? 4 : parseInt(self.attr('times'))
        var cpt = 0;
        
        var springimg = self.parent().find('.springimg')
        var springattach = self.parent().find('.springattach')
        springattach.css({left: springX-12, top:springY-12})
        
        var vecteur_vitesse = self.parent().find('.vecteur_vitesse')
        var vecteur_accel = self.parent().find('.vecteur_accel')
        var vecteurs = vecteur_vitesse.add(vecteur_accel)
        
        vecteurs.hide()
        
        var x = 0
        var y = 0
        var vx = 0
        var vy = 0
        var prev = false
        
        var ndx, ndy, ax, ay;
        
        var dx = springX - x
        var dy = springY - y
        var r = Math.sqrt(dx * dx + dy * dy)
        var theta = Math.atan2(dy, dx)
        
        function applyPos() {
            self.css({left: x-16, top:y-16})
            springimg.css('transform', 'translate(-50%, -50%) translate(' + (x+springX)/2 + 'px,' + (y+springY)/2 + 'px) rotate(' + theta + 'rad) scale(' + (r/32) + ',1)')
        }
        
        applyPos()
        
        springimg.css('transform', 'translate(-50%, -50%) translate(' + (x+springX)/2 + 'px,' + (y+springY)/2 + 'px) rotate(' + theta + 'rad) scale(' + (r/32) + ',1)')
        
        setupAnimations(self, function(time) {
            if(time == null)
                time = 20
            
            if(i == 0) {
                x = 0
                y = 0
                vx = v0x
                vy = v0y
                
                var cl = setInterval(function(){
                    dx = springX - x
                    dy = springY - y
                    r = Math.sqrt(dx * dx + dy * dy)
                    theta = Math.atan2(dy, dx)
                    
                    ndx = dx / r
                    ndy = dy / r
                    
                    ax = k * ndx
                    ay = k * ndy
                    
                    // display now to match acceleration
                    applyPos()
                    setVector(vecteur_vitesse, x, y, vx, vy, 5, 16)
                    setVector(vecteur_accel, x, y, ax, ay, 25, 16)
                        
                    var cur = Math.abs(x+(vx+ay)) < 10 && Math.abs(y+(vy+ay)) < 10
                    if(!prev && cur)
                        cpt++;
                    prev = cur;
                    
                    if(cpt == times) {
                        cpt = 0
                        i = 0
                        x = 0
                        y = 0
                        
                        dx = springX - x
                        dy = springY - y
                        r = Math.sqrt(dx * dx + dy * dy)
                        theta = Math.atan2(dy, dx)
                        applyPos()
                        vecteurs.hide()
                        clearInterval(cl)
                    } else {
                        // we see 1 frame of "collision"
                        vx += ax;
                        vy += ay;
                        x += vx
                        y += vy
                        i++;
                    }
                }, time)
            }
        })
    })
    
    if(location.hash) {
        var hash = document.location.hash;
        if(hash.length > 1) {
            var ahash = hash 
            var target = $(hash);
            target = target.length ? target : $('[name=' + hash.slice(1) +']');
            if (target.length) {
                $('html,body').animate({
                    scrollTop: target.offset().top
                }, 500, void 0, function(){
                    location.hash = ahash
                });
            }
        }
    }
    
    $('a[href^=#]').click(function(ev) {
        if (location.pathname.replace(/^\//,'') == this.pathname.replace(/^\//,'') && location.hostname == this.hostname) {
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
    $('a[href=#]').click(function(ev){
        $('html,body').animate({
            scrollTop: 0
        }, 500, void 0, function(){
            location.hash = ''
        });
        ev.preventDefault();
    })
})