////////////////////////////////////////////////////////////////////////////////
/// jquery
////////////////////////////////////////////////////////////////////////////////
$(function(){

	$('img').lazyload({ threshold : 200 });//画像遅延読み込み
	$('input').keydown(function(e) {if (e.keyCode === 13) e.preventDefault();});//enter key無効
	$('textarea').autoResize();	//テキストエリア自動拡張
	$('body').defer();//画像遅延読み込み

});

////////////////////////////////////////////////////////////////////////////////
/// jquery plugin
////////////////////////////////////////////////////////////////////////////////
(function($){
	/*
	オブジェクト 表示
	----------------------------------------------------------------------*/
	$.fn.displayBlock = function() {
		this.css('display','block');
	};
	/*
	オブジェクト 非表示
	----------------------------------------------------------------------*/
	$.fn.displayNone = function() {
		this.css('display','none');
	};
	/*
	画像の遅延読み込み
	----------------------------------------------------------------------*/
	$.fn.defer = function(options) {
		return $('img').each(function() {
			$(this).attr('src',$(this).attr('data-defer-src'));
		});
	}
	/*
	表示位置設定
	----------------------------------------------------------------------*/
	$.fn.adjustCenter = function () {
		//alert(document.documentElement.clientHeight);
		var tw=$(this).width()/2;
		var tH=$(this).height()/2;
		//var tS = document.body.scrollTop || document.documentElement.scrollTop;
		//var marginTop = ""+(tS + document.documentElement.clientHeight / 2 - tH);
		//var marginLeft = ($(window).width()-$(this).width())/2;
		var docHeight=$(document).height();
		$(this).parent().css({"min-height":docHeight,"max-height":docHeight});
		//$(this).css({top:marginTop+"px", left:marginLeft+"px"});
		$(this).css({"margin-top":-tH+"px", "margin-left":-tw+"px"});
	}

	/*
	ボタン disabled
	----------------------------------------------------------------------*/
	$.fn.disabledBtn = function(options) {
		return $('.js-submit,#js-submit').each(function() {
			$(this).prop("disabled",true).addClass('opa50');
		})
	}

	/*
	ボタン enable
	----------------------------------------------------------------------*/
	$.fn.enableBtn = function(options) {
		return $('.js-submit,#js-submit').each(function() {
			$(this).prop("disabled",false).removeClass('opa50');
		})
	}


})(jQuery);

////////////////////////////////////////////////////////////////////////////////
/// 関数
////////////////////////////////////////////////////////////////////////////////
/*
cookie 取得；引数(cookie名)
----------------------------------------------------------------------*/
var getCookie = function (theName){
	theName += "=";
	theCookie = document.cookie+";";
	start = theCookie.indexOf(theName);
	if (start != -1){
		end = theCookie.indexOf(";",start);
		return unescape(theCookie.substring(start+theName.length,end));
	}
	return false;
}
/*
配列キー存在チェック:引数(key,配列)
----------------------------------------------------------------------*/
var arrayKeyExists = function (key, search) {
	if (!search || (search.constructor !== Array && search.constructor !== Object)) {
		return false;
	}
	return key in search;
}
/*
パラメータ取得:引数(key)
----------------------------------------------------------------------*/
var getUrlVars = function (){
	var vars = [], hash;
		hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
		for(var i = 0; i <hashes.length; i++){
			hash = hashes[i].split('=');
			vars.push(hash[0]);
			vars[hash[0]] = hash[1];
		}
	return vars;
}
/*
htmlEscape
----------------------------------------------------------------------*/
var htmlEscape = (function(){
var map = {"<":"&lt;", ">":"&gt;", "&":"&amp;", "'":"&#39;", "\"":"&quot;"};
var replaceStr = function(s){ return map[s]; };
return function(str) {if ((str instanceof String) || (typeof str == 'string')) { str=str+"";return str.replace(/<|>|&|'|"/g, replaceStr); } else {return str} };
})();
/*
時間の表示；引数(システム日付) 何分前・何時間前・昨日・何月何日
----------------------------------------------------------------------*/
var time_ago = function(time){

	var today = new Date();

 	var dispTime ="";
	(time=="" || time == undefined)?time = new Date():time = time.replace(/\-/g,"/");

 	var time = new Date(time);

 	var today = new Date();
 		today.setHours(0);
 		today.setMinutes(0);
 		today.setSeconds(0);
		today.setMilliseconds(0);

 		var pre = new Date();
 		pre.setDate(pre.getDate()-1);
 		pre.setHours(0);
 		pre.setMinutes(0);
 		pre.setSeconds(0);
 		pre.setMilliseconds(0);

 		var ints = {
 				    //second: 1,
 					'分': 60,
 	 				'時間': 3600
 				//    day: 86400,
 				//    week: 604800,
 				//    month: 2592000,
 				//    year: 31536000
 			};

	 	if(time < pre){
			dispTime = time.getMonth() + 1 + "月"+ time.getDate()+"日";
	 	}else if(pre <= time && time <= today){
			dispTime ="昨日";
	 	}else{
	 		time = +new Date(time);
	 		var gap = ((+new Date()) - time) / 1000,amount, measure;

	 		for (var i in ints) {
	 			if (gap > ints[i]) { measure = i; }
	 		}
	 		amount = gap / ints[measure];

	 		//amount = gap > ints.day ? (Math.round(amount * 100) / 100) : Math.round(amount);
	 		amount =  Math.round(amount);
	 		if(undefined == measure){
	 			amount = '0分前'
	 		} else{
		 		amount += '' + measure + '前';
	 		}

	 		dispTime = amount || 0;
	 	}

	 return dispTime;
}

/*
set seectbox color
----------------------------------------------------------------------*/
var setSelectboxOptionColor= function(obj,flag){
	if(flag==true){
		obj.removeClass("text_col3");
		obj.parent().addClass("toggle-off");
	}else{
		obj.addClass("text_col3");
		obj.parent().removeClass("toggle-off");
	}
}

/*
写真セット
----------------------------------------------------------------------*/
function setCommonImage(imgId, base64ImgData) {
	var img_id = "js-" + imgId;
	var img_display = "js-img_" + imgId;
	var img_hidden = "js-hidden_" + imgId;
	var data = "data:image/png;base64," + base64ImgData;
	$('#'+img_display).attr("src", data);
	$('#'+img_id).css("background-image","url("+data+")");
	$('#'+img_hidden).val(base64ImgData);
}

/*
写真クリア
----------------------------------------------------------------------*/
function clearCommonImage(imgId) {
	$('#js-hidden_'+imgId).val('');
}
/*
文字切り抜き+3点リーダ
----------------------------------------------------------------------*/
var strimwidth = function(str,n) {
	return str.substring(0,n)+'…';
}
/*
object clone 生成
----------------------------------------------------------------------*/
clone = function(source) {
  return $.extend(true,{},source);
}

/*
feedInOut
-------------------------------	---------------------------------------*/
var feedInOut = function (callback,message,vox) {

	var html = 	'<div class="anime_area">'+
				'<div class="feedinout_anime">'+
				'<div class="' + vox + '">'+
				'<div class="text15 fw_bld taCenter mt10">' + message + '</div>'+
				'<div class="taCenter mt10"><span class="icon_sprite praise"></span></div>'+
				'</div>'+
				'</div>'+
				'</div>';

	$('body').append(html);

	$('.praises').fadeIn('slow',function(){
		$(this).fadeOut('slow',function(){$('.anime_area').remove()});
	});

};
/*
ダイアログ
-------------------------------	---------------------------------------*/
var dialog = function (callback,message,btn_name,btn_color,btn_num) {

	var $body = $('body');

	$('a').addClass('no_highlight');

	if(btn_name == undefined){
		btn_name = "はい";
	}
	if(btn_color == undefined){
		btn_color = "";
	}
	var html = '<div class="dialog_area">'+
				'<div class="overlay_black">'+
				'<div class="dialog">'+
				'<p class="message"><span>'+ message +'</span></p>'+
				'<ul class="btn_area">';

			if(btn_num == 1){
				html+='<li><button type="button" class="btn_all js-execute ' + btn_color + '"><span class="text12 text_col3">' + btn_name + '</span></button></li>';

			}else{
				html+='<li class="w50p"><button type="button" class="btn_all js-cancell"><span class="text12 text_col3">キャンセル</span></button></li>'+
						'<li class="w50p" ><button type="button" class="btn_all js-execute ' + btn_color + '"><span class="text12 text_col3">' + btn_name + '</span></button></li>';
			}

			html+='</ul>'+
					'</div></div></div>';


	var dialog = $('.dialog_area');


	$body.append(html);
	$('.dialog').adjustCenter();
	$('.dialog_area').displayBlock();

	$('.js-cancell,.overlay_black').off('click').on('click',function(event) {
		 $('.dialog_area').remove();
		 $('a').removeClass('no_highlight');
	});

	$('.js-execute').off('click').on('click', function(event) {
		callback();
		 $('.dialog_area').remove();
	});

};
/*
ダイアログ 縦
-------------------------------	---------------------------------------*/
var dialog_2 = function (callback,message,btn_color) {

	$('a').addClass('no_highlight');
	if(btn_color == undefined){
		btn_color = "";
	}

	var html = '<div class="dialog_area">'+
				'<div class="overlay_black">'+
				'<div class="dialog_2">'+
				'<ul class="btn_area">'+
				'<li><button type="button" class="btn_all js-execute ' + btn_color + '"><span class="text12 text_col3">'+ message +'</span></button></li>'+
				'<li ><button type="button" class="btn_all js-cancell"><span class="text12 text_col3">キャンセル</span></button></li>'+
				'</ul>'+
				'</div></div></div>';

	var $body = $('body');
	var dialog = $('.dialog_area');


	$body.append(html);
	$('.dialog_2').adjustCenter();
	$('.dialog_area').displayBlock();

	$('.js-cancell,.overlay_black').off('click').on('click',function(event) {
		 $('.dialog_area').remove();
		 $('a').removeClass('no_highlight');
	});

	$('.js-execute').off('click').on('click', function(event) {
		callback();
		 $('.dialog_area').remove();
	});

};








