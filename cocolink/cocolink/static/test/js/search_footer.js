
(function(window, document){
	

	var SearchFooter = function (){};

	SearchFooter.prototype = {

		wrapp : null,
		tab :null,
		bar : null,
		timer : null,
		activeFlg : 0,
        landscape : 0,
		channel :  null,
		sr :  null,
		init : function(){

			this.channel = arguments[0];
			this.sr = arguments[1];
            this.createTemplate(arguments[2]);
            this.handler();

		},
        handler : function(){

            this.setTabStyle();
            document.addEventListener("scroll",bind(this,"setTabStyle"),false);
            document.addEventListener("touchstart",bind(this,"setTabStyle"),false);
            this.tab.addEventListener("click", bind(this,"clickEvent"), false);
            this.wrapp.addEventListener("webkitAnimationEnd", bind(this,"animeEndEvent"), false);
            window.addEventListener("orientationchange", bind(this,"orientEvent"), false);


        },
 		orientEvent  : function(){

            clearTimeout(this.timer);
            var test = document.getElementById("test");
            var test2 = document.getElementById("test2");

            test.innerHTML = "たて"+window.innerHeight +'//'+'よこ'+window.innerWidth;
            if (Math.abs(window.orientation) === 90) {
                this.landscape = 1;
                this.tab.style.opacity = '0';
                this.tab.style.webkitTransitionDuration = '0';
                this.tab.className = 'footer_search_tab';
                if(this.activeFlg == 1) this.clickEvent();

            } else {
                this.landscape = 0;
                this.setTabStyle();
            }

		},
		clickEvent : function(){

            if ( this.activeFlg == 1 ) {
                this.activeFlg = 0;
                this.wrapp.style.webkitAnimationName = 'animation_down';
                this.wrapp.style.WebkitAnimationDuration = '0.2s';
                this.setTabStyle();

            } else{
                this.activeFlg = 1;
                this.wrapp.style.webkitAnimationName = 'animation_up';
                this.wrapp.style.WebkitAnimationDuration = '0.3s';
                this.bar.style.display = 'block';
                this.bar.style.opacity = '1';
                this.tab.style.opacity = '1';
                this.tab.style.webkitTransitionDuration  = '0';
                this.tab.className = 'footer_search_active';

            }

			
		},
		animeEndEvent : function(){

			if (this.activeFlg == 1 ){
				this.wrapp.style.bottom = '-10px';
			}else{
				this.tab.className = 'footer_search_tab';
				this.wrapp.style.bottom = '-100px';
				this.bar.style.display = 'none';
			}

		},
		setTabStyle : function () {

            var that = this;
            this.timer = null;

            if(this.landscape == 0 ){
                this.tab.style.opacity = '1';
                this.tab.style.webkitTransitionDuration = '0';
            }

            this.timer = setTimeout(function(){
                if(that.activeFlg == 0 && that.landscape == 0){
                    that.tab.style.opacity = '0.5';
                    that.tab.style.webkitTransitionDuration  = '2s';
                    that = null;
                }
            } ,1000);

		},
		createTemplate : function (islowOs){


			var tab_tpl ='<section id="footer_search_tab" class="footer_search_tab"  style="opacity:1">'+
						'<div class="footer_layout">'+
						'<div class="footer_tab_content">'+
						'</div>'+
						'<i class="sprite_icon_footer sprite_icon01"></i>'+
						'</div>'+
						'</section>';

			var bar_tpl ='<section id = "footer_search_bar" class= "footer_search_bar" style="opacity:1">'+
						'<form name="search" action="http://win.auone.jp/top/redirect.php?uri=http%3A%2F%2Fa.news.auone.jp%2Fhotword%2Findex.php&fid=l_google" method="get" class="frame">'+
						'<div class="txt_bx"><input type="text" id="keyword" name="q" placeholder="検索ワードを入力" data-tr="0" autocomplete="off" widdit="on">'+
						'<span class="cross"><a href="#" onclick="delval(); return false;">'+
						'<i class="sprite_icon_footer sprite_icon02"></i>'+
						'</a></span></div><div class="btn_bx">'+
						'<button class="search_btn" type="button" onclick="search_start();">検索</button>'+
						'<i class="sprite_icon_footer sprite_icon04"></i>'+
						'</div>'+
						'</form>'+
						'<div class="hotword">'+
						'<a href="http://win.auone.jp/top/redirect.php?uri=http%3A%2F%2Fsp-search.auone.jp%2Fsearch&amp;fid=i_tl_hotword" onclick="trEvent(this.href,"TL急上昇","","");" class="hotword_more">'+
						'<i class="sprite_icon_footer sprite_icon03"></i>'+
						'</a>'+
						'<ul>'+
						'<li><a href="http://sp-search.auone.jp/search?q='+encodeURIComponent(hotWord1) +'&client=mobile-kddi-popular&channel='+this.channel+'&sr='+this.sr+'">'+ hotWord1 +'</a></li>'+
						'<li><a href="http://sp-search.auone.jp/search?q='+encodeURIComponent(hotWord2) +'&client=mobile-kddi-popular&channel='+this.channel+'&sr='+this.sr+'">'+ hotWord2 +'</a></li>'+
						'<li><a href="http://sp-search.auone.jp/search?q='+encodeURIComponent(hotWord3) +'&client=mobile-kddi-popular&channel='+this.channel+'&sr='+this.sr+'">'+ hotWord3 +'</a></li>'+
						'</ul>'+
						'</div>'+
						'</section>';


			var wrapper = document.createElement("footer");

			if (islowOs) {
				wrapper.className = 'footer_search_bottom_wrapper';
				wrapper.innerHTML =  bar_tpl;
				$('footer_search').appendChild(wrapper);

			} else{
				wrapper.className = 'footer_search_wrapper';
				wrapper.id = 'footer_search_wrapper';
				wrapper.innerHTML = tab_tpl + bar_tpl;
				document.body.appendChild(wrapper);
			}

			this.wrapp = document.getElementById("footer_search_wrapper");
			this.tab =  document.getElementById("footer_search_tab");
			this.bar =  document.getElementById("footer_search_bar");
			if (!islowOs) this.bar.style.opacity = '0';

		}

	};

	/*
	* CSSFile　load
	*/
	var loadFile = function () {

		var link = document.createElement('link');
		link.href = './css/search_footer.css';
		link.rel = 'stylesheet';
		link.type = 'text/css';
		var h = document.getElementsByTagName('head')[0];
		h.appendChild(link);
	};

	/*
	* UserAgent 判定
	*/
	var judgeUserAgent = function (){
		var ua = navigator.userAgent,isIos,ver;

		if(ua.indexOf('iPhone') > 0 || ua.indexOf('iPod') > 0 || ua.indexOf('iPad') > 0){
			isIos = 1;
			ua.match(/iPhone OS (\w+){1,3}/g);
			ver = (RegExp.$1.replace(/_/g, '')+'00').slice(0,3);

		}else if(ua.indexOf('Android') > 0){
			isIos = 0;
			ver  = parseFloat(ua.slice(ua.indexOf("Android")+8));
		}

		return {isIos:isIos,version:ver};

	};


    var bind = function(context,name){
		return function(){
			return context[name].apply(context,arguments);
		}
	};



    /*
     * Android
     */
    var orientEvent = function(){

        if (window.innerHeight > window.innerWidth) {
            this.setTabStyle();
        } else {
            if(this.activeFlg == 1){
                this.activeFlg = 0;
                this.wrapp.style.bottom = '-100px';
                this.bar.style.opacity = '0';
                this.tab.style.opacity = '0';
                this.tab.style.className = 'footer_search_tab';

            }else{
                this.tab.style.opacity = '0';
            }
        }
    };
    /*
     * Android
     */
    var clickEvent = function(){

        if ( this.activeFlg == 1 ) {
            this.activeFlg = 0;
            this.wrapp.style.bottom = '-95px';
            this.bar.style.opacity = '0';
            this.tab.className = 'footer_search_tab';
            this.setTabStyle();

        } else{
            this.activeFlg = 1;

            this.bar.style.display = 'block';
            this.wrapp.style.bottom = '-10px';
            this.bar.style.opacity = '1';
            this.tab.style.opacity = '1';
            this.tab.style.webkitTransitionDuration = '';
            this.tab.className = 'footer_search_active';
        }
    };


	window.onload = function () {

		loadFile();
        var ua = judgeUserAgent();
        var searchFooter = new SearchFooter();
        var islowOs = false;

        //ios4未満 Android2.1以下
        if( (ua.isIos && 500 > ua.version) ||  (ua.isIos == 0 && 2.1 >= ua.version)){
            islowOs = true;
            searchFooter.handler = function(){};
        }else{
            //Android4未満　2.2以上　
            if((ua.isIos == 0 && 4 > ua.version && ua.version >= 2.2) ) {
                searchFooter.orientEvent = orientEvent;
                searchFooter.clickEvent = clickEvent;
            }
        }
        searchFooter.init(channel,srPopular,islowOs);
	};

})(window,window.document);




