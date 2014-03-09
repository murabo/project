
(function(window, document){
	

	var SearchFooter = function (){};

	SearchFooter.prototype = {

		wrapp : null,
		tab :null,
		bar : null,
		timer : null,
		activeFlg : 0,
		channel :  null,
		sr :  null,
		init : function(userAgent){

			this.channel = arguments[0];
			this.sr = arguments[1];
			this.judgeHandler( arguments[2]);

		},
		judgeHandler : function(ua){
/*
			if( (ua.isIos && 500 > ua.version) ||  (ua.isIos == 0 && 2.1 >= ua.version)){
				this.createTemplate(true);
	
			}else if((ua.isIos == 0 && 4 > ua.version && ua.version >= 2.2) ) {
				this.createTemplate();
				this.androidHandler();
			}else{
				this.createTemplate();
				this.defaultHandler();
			}*/

			this.createTemplate(true);

		},
		defaultHandler : function(){

			this.setTabStyle();
			document.addEventListener("scroll",bind(this,"setTabStyle"),false);
			document.addEventListener("touchstart",bind(this,"setTabStyle"),false) 

			this.tab.addEventListener("click", bind(this,"clickEvent"), false);
			this.wrapp.addEventListener("webkitAnimationEnd", bind(this,"animeEndEvent"), false);
			window.addEventListener("orientationchange", bind(this,"orientEvent"), false);

		},
		orientEvent  : function(){

			if (window.innerHeight > window.innerWidth) {
			   	this.setTabStyle();
			} else {
			    if(this.activeFlg == 1){
					this.activeFlg = 0;
					this.wrapp.setStyle({'-webkit-animation': 'animation_down 0.3s'});
					this.bar.setStyle({'opacity': '0', '-webkit-transition' : '0.3s'});
					this.tab.setStyle({'opacity': '0', '-webkit-transition' : '0.3s'});
					this.tab.removeClassName('current');
			    }else{
					this.tab.setStyle({'opacity': '0', '-webkit-transition' : '0.3s'});
			    }
			};

		},
		clickEvent : function(){

			if ( this.activeFlg == 1 ) {
				this.activeFlg = 0;
				this.wrapp.setStyle({'-webkit-animation': 'animation_down 0.3s'});
				this.bar.setStyle({'opacity': '0', '-webkit-transition' : '0.3s'});
				this.tab.removeClassName('current');
				this.setTabStyle();
	
			} else{
				this.activeFlg = 1;
				this.bar.setStyle({'display':'block'});
				this.wrapp.setStyle({'-webkit-animation': 'animation_up 0.3s'});
				this.bar.setStyle({'opacity': '1', '-webkit-transition' : '0.3s'});
				this.tab.setStyle({'opacity': '1', '-webkit-transition' : '0s'}).addClassName('current');			
			}	

		},
		animeEndEvent : function(){

			if (this.activeFlg == 1 ){
				this.wrapp.setStyle({'bottom':'-10px'});
			}else{
				this.wrapp.setStyle({'bottom':'-100px'});
				this.bar.setStyle({'display':'none'});
			}

		},
		/*
		* Android 4.0未満
		* Android 2.2以上
		*/
		androidHandler : function(){

			this.setTabStyle();
			document.addEventListener("scroll",bind(this,"setTabStyle"),false);
			document.addEventListener("touchstart",bind(this,"setTabStyle"),false) 

			this.tab.addEventListener("click", bind(this,"clickEvent_and"), false);
			window.addEventListener("orientationchange", bind(this,"orientEvent_and"), false);

		},
		orientEvent_and  : function(){

			if (window.innerHeight > window.innerWidth) {
			   	this.setTabStyle();
			} else {
			    if(this.activeFlg == 1){
					this.activeFlg = 0;
					this.wrapp.setStyle({'bottom': '-100px'});
					this.bar.setStyle({'opacity': '0'});
					this.tab.setStyle({'opacity': '0'});
					this.tab.removeClassName('current');
			    }else{
					this.tab.setStyle({'opacity': '0'});
			    }
			};

		},
		clickEvent_and : function(){

			if ( this.activeFlg == 1 ) {
				this.activeFlg = 0;
				this.wrapp.setStyle({'bottom': '-95px'});
				this.bar.setStyle({'opacity': '0'});
				this.tab.removeClassName('current');
				this.setTabStyle();
	
			} else{
				this.activeFlg = 1;
				this.bar.setStyle({'display':'block'});
				this.wrapp.setStyle({'bottom': '-10px'});
				this.bar.setStyle({'opacity': '1'});
				this.tab.setStyle({'opacity': '1', '-webkit-transition' : '0s'}).addClassName('current');			
			}	

		},
		setTabStyle : function () {

			var that = this;

			if (this.timer){
				clearTimeout(this.timer);
				that.tab.setStyle({'opacity': '1', '-webkit-transition' : ''});
			}

			this.timer = setTimeout(function(){
			
				if(that.activeFlg == 0 ){
					that.tab.setStyle({'opacity': '0.5', '-webkit-transition' : '2s'});	

					//that.tab.style.opacity = '0.5';
					//that.tab.style.WebkitAnimationDuration = '2s';
					that = null;
					timer = null;
				}

			} , 1000);

		},
		createTemplate : function (lowOsFlg){


			var tab_tpl ='<section id="footer_search_tab" class="footer_search_tab"  style="opacity:1">'+
						'<div class="footer_layout">'+
						'<div class="footer_tab_content">'+
						'</div>'+
						'<i class="sprite_icon_footer sprite_icon01"></i>'+
						'</div>'+
						'</section>';

			var bar_tpl ='<section class= "footer_search_bar" style="opacity:1">'+
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

			if (lowOsFlg) {
				wrapper.className = 'footer_search_bottom_wrapper' 
				wrapper.innerHTML =  bar_tpl;
				$('footer_search').appendChild(wrapper);

			} else{
				wrapper.className = 'footer_search_wrapper';
				wrapper.innerHTML = tab_tpl + bar_tpl;
				document.body.appendChild(wrapper);
			}

			this.wrapp = $$('.footer_search_wrapper')[0],
			//this.tab = $('footer_search_tab'),
			this.tab = $$('.footer_search_tab')[0],
			this.bar = $$('.footer_search_bar')[0];

			if (!lowOsFlg) this.bar.setStyle({'opacity': '0'});

		}

	}

	/*
	* CSSFile　load
	*/
	function loadFile() {

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
	function judgeUserAgent(){
		var ua = navigator.userAgent,isIos,ver,isMobile;

		if(ua.indexOf('iPhone') > 0 || ua.indexOf('iPod') > 0 || ua.indexOf('iPad') > 0){

			(ua.indexOf('iPad') > 0)? isMobile = 0: isMobile = 1;
			isIos = 1;
			ua.match(/iPhone OS (\w+){1,3}/g);
			ver = (RegExp.$1.replace(/_/g, '')+'00').slice(0,3);

		}else if(ua.indexOf('Android') > 0){
			
			(ua.indexOf('Mobile') > 0) ? isMobile = 1 : isMobile = 0;
			isIos = 0;
			ver  = parseFloat(ua.slice(ua.indexOf("Android")+8));
			console.log(ua);
		}

		return {isIos:isIos,version:ver,isMobile:isMobile};

	}

	
	function bind(context,name){
		return function(){
			return context[name].apply(context,arguments);
		}
	}

	window.onload = function () {
		loadFile();
		var searchFooter = new SearchFooter();
		searchFooter.init(channel,srPopular,judgeUserAgent());
	};

	

})(this, this.document)

