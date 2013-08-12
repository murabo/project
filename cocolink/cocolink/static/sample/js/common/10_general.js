////////////////////////////////////////////////////////////////////////////////
/// jquery
////////////////////////////////////////////////////////////////////////////////
$(function(){

	$('input').keydown(function(e) {if (e.keyCode === 13) e.preventDefault();});//enter key無効
	$('body').defer();//画像遅延読み込み
	$.preloadImages(image_url+"loader.gif");//プレロード

	//header 戻るボタン
	$('.backBtn').click(function(){
		if ($('#back_url').is('*') && $('#back_url').val() != ''){
			location.href = $('#back_url').val();
			return false;
		}
		history.back();
		return false;
	});

	//フッターアコーディオン
	$(".js-footer-toggle-switch").click(function(){
		$(this).next().slideToggle("200");
		$(this).toggleClass("ft_arrow_up ft_arrow_down");
	});

	//アプリver1.2.2以上は簡単ログイン可
	$(document).on('click','.js-pre-login',function(){
		if(is_app == 1 &&  is_app_ver >= 122){
			event.preventDefault();
			var href = $(this).attr('href').indexOf("from=direct",0);
			if(href > 0){
//				location.href = 'glup://preLogin/q?fromDirect';
				location.href = base_url +'web/login/set_referer?from=direct';
			}else{
//				location.href = 'glup://preLogin/q?';
				location.href = base_url +'web/login/set_referer';
			}
		}
	});

});


/*
ユーザーエージェント取得
----------------------------------------------------------------------*/
var ua="";
var trigger = "";
var nua = navigator.userAgent;
//if ((nua.indexOf('iPhone') > 0 && nua.indexOf('iPad') == -1) || nua.indexOf('iPod') > 0 || (nua.indexOf('Android') > 0 )) {
if ((nua.indexOf('iPhone') > 0 && nua.indexOf('iPad') == -1) || nua.indexOf('iPod') > 0 || (nua.indexOf('Android') > 0 &&  0 > nua.indexOf('SC'))) {
	ua = 'SP';
	trigger = 'touchstart';
}else{
	ua = 'PC';
	trigger = 'click';
}
/*
Retinaディスプレイ判定
----------------------------------------------------------------------
var ratio = false;
if(window.devicePixelRatio > 1) {
	ratio = true;
}
*/

/*
定数
----------------------------------------------------------------------*/
social_name = new Array(3);
social_name[2] = "facebook";
social_name[3] = "twitter";
social_name[4] = "mixi";

////////////////////////////////////////////////////////////////////////////////
/// jquery plugin
////////////////////////////////////////////////////////////////////////////////
(function($){

	/*
	タッチしたボックスの background color 変更
	----------------------------------------------------------------------*/
	$.fn.touchColor = function(touchCol) {
		var start = "touchstart";
		var end   = "touchend";
		return this.each(function() {
			$(this).bind(start,function(){$(this).addClass(touchCol);});
			$(this).bind(end,function(){$(this).removeClass(touchCol);});
		});
	};


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
			var that = $(this);
			//that.attr('src', that.attr('data-defer-src').replace(/(\.jpg|\.png)/gi,'@2x$1'));
			that.attr('src',that.attr('data-defer-src'));
		});
	}

	/*
	表示位置設定 画面の中央に表示
	----------------------------------------------------------------------*/
	$.fn.adjustCenter = function (top) {
		var that = this;
		var tw=that.outerWidth()/2;
		var tH=that.outerHeight()/2;
		var tS =(document.documentElement.scrollTop > 0) ? document.documentElement.scrollTop: document.body.scrollTop;
		var docH = document.documentElement.clientHeight;
		if(top){
			that.css({"top":top+'px', "margin-left":-tw+"px"});
		}else{
			that.css({"top":tS+(docH/2)+"px","margin-top":-tH+20+"px", "margin-left":-tw+"px"});
		}
		var docHeight=$(document).height();
		that.parent().css({"min-height":docHeight,"max-height":docHeight});
	}
	/*
	表示位置設定 画面トップに表示
	----------------------------------------------------------------------*/
	$.fn.adjustCenterTop = function (top) {
		var that = this;
		var tw=that.outerWidth()/2;
		var t=(top)?top:0;
		that.css({"top":t+'px', "margin-left":-tw+"px"});
	}

	/*
	ボタン disabled
	----------------------------------------------------------------------*/
	$.fn.disabledBtn = function(options) {
		return $('.js-submit,.js-submit_comment,.js-post').each(function() {
			$(this).prop("disabled",true).addClass('opa50');
		})
	}

	/*
	ボタン enable
	----------------------------------------------------------------------*/
	$.fn.enableBtn = function(options) {
		return $('.js-submit,.js-submit_comment,.js-post').each(function() {
			$(this).prop("disabled",false).removeClass('opa50');
		})
	}

	/*
	アコーディオン
	----------------------------------------------------------------------*/
	$.fn.accordion = function(options) {
		return $(".js-toggle-switch").click(function(){
			$(this).next().slideToggle();
			$(this).parent().toggleClass("arrow_up arrow_down");
		});
	}

	/*
	プレロード
	----------------------------------------------------------------------*/
	jQuery.preloadImages = function(){
	    for(var i = 0; i< arguments.length; i++){
			jQuery("<img>").attr("src", arguments[i]);
	    }
	};


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
return function(str) { str=str+"";return str.replace(/<|>|&|'|"/g, replaceStr);};
//return function(str) {if ((str instanceof String) || (typeof str == 'string')) { str=str+"";return str.replace(/<|>|&|'|"/g, replaceStr); } else {return str} };
})();

/*
リンク生成
----------------------------------------------------------------------*/
var replaceUrlToAnchor=function(val){
	val = val.split('\n').join('<br />\n');
	return val.replace(/(http:\/\/)([-\w\.\&\=]+)(:\d+)?(\/)?([-_.!~*()a-zA-Z0-9;\/?:=+$,%#&]+)?/g, function(match) {
		var popup = 'target="_blank"';
		var paramUrl = match;
		if (match.substr(0, base_url.length) === base_url){
			popup = 'target="_self"';
		}else{
			paramUrl = encodeURI(paramUrl);
		}
		return '<a href="'+paramUrl+'" '+popup+' class="text_col_gray text11 tx_underline">'+match+'</a>';
	});
};
/*
文字切り抜き+3点リーダ
----------------------------------------------------------------------*/
var strimwidth = function(str,n) {
	var temp='';
	(str.length < n ) ? temp = str : temp = str.substring(0,n);
	return temp;
}
/*
改行
----------------------------------------------------------------------*/
var nl2br = function(str,n) {
	var val = str.split('\n').join('<br />\n');
	return val;
}
/*
trim+３点リーダー+続きを読む+改行
----------------------------------------------------------------------*/
var trimContinue = function(str,n) {
	(str.length < n ) ? temp = str : temp = str.substring(0,n)+'…'+ '<span class="continue">続きを読む</span>';
	var val = temp.split('\n').join('<br />\n');
	return val;
}


/*
時間の表示；引数(システム日付) 何分前・何時間前・昨日・何月何日
----------------------------------------------------------------------*/
var time_ago = function(time){

	var dispTime ="";
	(time=="") ? time = new Date() : time = time.replace(/\-/g,"/");

	var param_date = new Date(time);
	var current_date = new Date();

	var second_diff = current_date.getTime() - param_date.getTime();
	second_diff = Math.floor(second_diff / 1000); /* msからsへの変換 */
	var dayago = Math.floor(second_diff / 86400);

	if( second_diff < 60 ){
		dispTime = 'たった今';
	}
	else if( second_diff < 3600){
		dispTime = Math.floor(second_diff / 60) + '分前';
	}
	else if( second_diff < 86400){
		dispTime = Math.floor(second_diff / 3600) + '時間前';
	}
	// else if( second_diff < 172800){
	// 	dispTime = '昨日';
	// }
	else if( dayago <= 7 ){
		dispTime =  dayago + '日前';
	}
	else{
		dispTime = param_date.getMonth() + 1 + "月"+ param_date.getDate()+"日";
	}

	return dispTime;
}

/*
時間の表示；引数(システム日付) YYYY年MM月DD日
----------------------------------------------------------------------*/
var format_date = function(time){
	time = time.replace(/\-/g,"/");
	var dispTime ="";
	var param_date = new Date(time);
	dispTime = param_date.getFullYear() + "年" + (param_date.getMonth() + 1) + "月"+ param_date.getDate()+"日";

	return dispTime;
}

/*
時間の表示；引数(システム日付) MM月DD日
----------------------------------------------------------------------*/
var format_date2 = function(time){
	time = time.replace(/\-/g,"/");
	var dispTime ="";
	var param_date = new Date(time);
	dispTime = (param_date.getMonth() + 1) + "月"+ param_date.getDate()+"日";

	return dispTime;
}

/*
時間の表示；引数(システム日付) MM月DD日
----------------------------------------------------------------------*/
var get_week = function(time){
	time = time.replace(/\-/g,"/");
	time = new Date(time);
	var w = ["日","月","火","水","木","金","土"];

	return w[time.getDay()];
}

/*
onclick
----------------------------------------------------------------------*/
$(".js-onclick").click(function(){
	/*何もないですがlabelで使っています。削除禁止*/
});


/*
要素にフォーカス
----------------------------------------------------------------------*/
function focusElement(obj) {
	var position, target = $(obj)[0];
	target.focus();
	if (target.setSelectionRange) {
		position = target.value.length;
		target.setSelectionRange(position, position);
	}
}

/*
object clone 生成
----------------------------------------------------------------------*/
clone = function(source) {
  return $.extend(true,{},source);
}
/*
デフォルトイベントストップ
----------------------------------------------------------------------*/
function touchHandler(event) {
	event.preventDefault();
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
ダイアログ
引数1:コールバック関数
引数2:表示文言(エスケープあり)
引数3:ボタン表示文言
引数4:ボタンのカラー
引数5:ボタンの数
引数6:アイコン(エスケープなし)
引数7:ボタンクラス
引数8:タイトル
-------------------------------	---------------------------------------*/
var dialog = function (callback,message,btn_name,btn_color,btn_num,icon,dialog_class,title,top,btn_name2) {

	var $body = $('body');
	$('a').addClass('no_highlight');

	if(btn_name == undefined) btn_name = "はい";
	if(btn_color == undefined) btn_color = "";
	if(icon == undefined) icon = "";
	(title == undefined)? title = "" : title = '<h6 class="pb10">' + title + '</h6>';

	var html = '<div class="dialog_area">'+
				'<div class="overlay_black">'+
				'<div class="dialog dialog_popup">'+title+
				'<div class="dialog_message_bx">'+
				'<div class="dialog_class"><div class="text12 fw_bld">' +  icon  + htmlEscape(message) +'</div></div>'+
				'<ul class="btn_area mt10">';

			if(btn_num == 1){
				html+='<li><button type="button" class="btn_all js-execute"><span class="text12">' + htmlEscape(btn_name) + '</span></button></li>';
			}else{
				html+='<li><button type="button" class="btn_all js-execute"><span class="text12">' + htmlEscape(btn_name) + '</span></button></li>'+'<li class="mt10"><button type="button" class="btn_all js-cancell"><span class="text12">';
				(undefined == btn_name2)? html+='キャンセル' :html+= btn_name2;
				html+='</span></button></li>';
			}

			html+='</ul></div></div></div></div>';


	$body.append(html);
	var dialog = $('.dialog_area');
	if(btn_color != '') $('.dialog_area .js-execute').addClass(btn_color);

	var  dialog_child = dialog.find('.dialog_class');
	(dialog_class == '' || dialog_class == undefined) ? dialog_child.addClass('message') : dialog_child.addClass(dialog_class);

	$('.dialog').adjustCenter(top);
	dialog.css("visibility", "visible");
	document.addEventListener("touchmove", touchHandler, false);

	$('.js-cancell,.overlay_black').off('click').on('click',function(event) {
		dialog.remove();
		 $('a').removeClass('no_highlight');
		document.removeEventListener("touchmove", touchHandler);
	});

	$('.js-execute').off('click').on('click', function(event) {
		callback();
		dialog.remove();
		document.removeEventListener("touchmove", touchHandler);
	});


};


/*
ダイアログ表示
-------------------------------	---------------------------------------*/
/*チュートリアルダイアログhtml---*/
var tutorial_dialog = '<div class="dialog_area tutorial_dialog">'+
		'<div class="overlay_tranc">'+
		'<div class="dialog amine">'+
		'<img src="'+ image_url +'tutorial.png" class="dialog_img_tuto" alt="">'+
		'<span class="sprite_image icon_image64 deleteimage js-dialog_delete pointer"></span>'+
		'<span class="tuto_sprite heart disp_none"></span>'+
		'<span class="tuto_sprite sta_s disp_none"></span>'+
		'<span class="tuto_sprite sta_m disp_none"></span>'+
		'<p class="ph11">'+
		'<button type="button" class="js-execute btn2 btn_all bg_col_pink_gradient">GIRLS UPにログインする</button>'+
		'</p>'+
		'</div></div>'+
		'</div>';

/*ログインダイアログhtml---*/
var login_dialog = '<div class="dialog_area login_dialog">'+
				'<div class="overlay_tranc">'+
				'<div class="dialog amine2">'+
				'<img src="'+ image_url +'img_login_popup.png" class="dialog_img_login" alt="">'+
				'<span class="sprite_image icon_image64 deleteimage js-dialog_delete pointer"></span>'+
				'<p class="ph11"><button type="button" class="js-execute btn2 btn_all bg_col_pink_gradient">GIRLS UPにログインする</button></p>'+
				'</div></div>'+
				'</div>';


/*ログインダイアログhtml---*/
var login_notes =	'<div class="dialog_area login_notes">'+
					'<div class="overlay_black">'+
					'<div class="dialog dialog_popup"><h6 class="text13 pb10">サービスIDでログインする際の注意事項</h6>'+
					'<div class="dialog_message_bx">'+
					'<div class="dialog_class"><div class="text12 taLeft">'+
					'<span class="disp_block">※Ameba以外のサービスをご利用の場合<a href="http://help.amebame.com/ameba-rules/" target="_blank">利用規約</a>と<a href="http://help.amebame.com/ameba-rules/821/" target="_blank">コネクトに関する同意事項</a>に同意の上、ログインしてください。</span>'+
					'<span class="disp_block mt5">※以前Amebaにログインした際と同一のサービスでログインしてください。</span>'+
					'<span class="disp_block mt10 textlnk"><a href="http://help.amebame.com/" target="_blank">よくある質問</a> <a href="http://help.amebame.com/ameba-rules/" target="_blank">利用規約</a></span>'+
					'</div></div></div></div></div></div>';

/*ダイアログ表示共通---*/
var dispDialog = function (html,classname,exc_callback,del_callback,top) {

	$('a').addClass('no_highlight');
	$('body').append(html);
	var dialog = $(classname);

	$('.dialog').adjustCenter(top);

	setTimeout(
		dialog.css("visibility", "visible")
		,700);

	var exec_flag = 0;
	$('.js-dialog_delete,.overlay_tranc,.overlay_black').off('click').on('click',function(event) {
		if(exec_flag == 0){
			AMB.track.action({name: 'action'});//トラッキング
			del_callback();
			dialog.remove();
			 $('a').removeClass('no_highlight');
		}
	});

	$('.js-execute').off('click').on('click', function(event) {
		exec_flag = 1;
		AMB.track.action({name: 'action'});//トラッキング
		exc_callback();
	});

};

/*ログインダイアログ表示処理呼び出し---*/
var dispLoginDialog = function(){

	//GIRLS UP以外のアプリの場合、遷移、その他はポップアップ表示
	if(is_app == 1  && is_my_app == 0){
		location.href = base_url +'web/login/pre_login/';
	}else{
		event.preventDefault();
		dispDialog(login_dialog,'.login_dialog', function(){
			if(is_app == 1 &&  is_app_ver >= 122){
//				location.href = 'glup://preLogin/q?';//アプリver1.2.2以上は簡単ログイン可
				location.href = base_url +'web/login/set_referer/';
			}else{
				location.href = base_url +'web/login/pre_login/';
			}

		},function(){});
	}

}

/*チュートリアル表示処理呼び出し---*/
var tutorial = function() {

	//GIRLS UP以外のアプリの場合、遷移、その他はポップアップ表示
	if(is_app == 1  && is_my_app == 0){
		location.href = base_url +'web/login/pre_login/';
	}else{

		AMB.track.action({name: 'action'});//トラッキング
		var that = $(this);
		var count = that.find('.js-count');
		if(that.hasClass('on')){
			count.html(parseInt(count.html())-1);
		}else{
			count.html(parseInt(count.html())+1);
		}
		that.toggleClass('on off');//レイアウトきりかえ
		that.find('.praise_icon').addClass('prais_rotate_anime');
		that.next('.hand').remove();
		$('.tuto').addClass('amine');
		dispDialog(tutorial_dialog,'.tutorial_dialog',function() {
			if(is_app == 1 &&  is_app_ver >= 122){
//				location.href = 'glup://preLogin/q?';//アプリver1.2.2以上は簡単ログイン可
				location.href = base_url +'web/login/set_referer/';
			}else{
				location.href = base_url +'web/login/pre_login/';
			}
		},function() {$('.tuto').remove();});

		setTimeout( function() {
			$('.tuto').remove();
			$('.tutorial_dialog .heart,.tutorial_dialog .sta_s,.tutorial_dialog .sta_m').addClass('amine')
		},1000);

	}

}

/*ログインダイアログ表示処理呼び出し---*/
var login_notes_area = function(){

	//GIRLS UP以外のアプリの場合、遷移、その他はポップアップ表示
	dispDialog(login_notes,'.login_notes', function(){},function(){});

}

/*
絵文字
----------------------------------------------------------------------*/
var emoji_list={'[とかげ]':'001','[にゃー]':'002','[わんわん]':'003','[しっぽフリフリ]':'004','[足あと]':'005','[パンダ]':'006','[ぶーぶー]':'007','[ヒヨコ]':'008','[ヒツジ]':'009','[カメ]':'010','[うり坊]':'011','[ブタ]':'012','[ウサギ]':'013','[ネコ]':'014','[ペンギン]':'015','[フグ]':'016','[カエル]':'017','[クマ]':'018','[ブタネコ]':'019','[クマノミ]':'020','[雨]':'021','[晴れ]':'022','[雪]':'023','[雷]':'024','[波]':'025','[虹]':'026','[くもり]':'027','[汗]':'028','[あせる]':'029','[ぐぅぐぅ]':'030','[ドキドキ]':'031','[ハートブレイク]':'032','[恋の矢]':'033','[むかっ]':'034','[ラブラブ]':'035','[爆弾]':'036','[メラメラ]':'037','[音譜]':'038','[ビックリマーク]':'039','[はてなマーク]':'040','[OK]':'041','[NG]':'042','[パンチ！]':'043','[走る人]':'044','[テニス]':'045','[スノーボード]':'046','[サーフィン]':'047','[野球]':'048','[ゴルフ]':'049','[サッカー]':'050','[柔道]':'051','[ブーケ１]':'052','[ブーケ２]':'053','[クローバー]':'054','[てんとうむし]':'055','[あじさい]':'056','[黄色い花]':'057','[コスモス]':'058','[ハチ]':'059','[チューリップ黄]':'060','[チューリップ赤]':'061','[チューリップ紫]':'062','[チューリップピンク]':'063','[チューリップオレンジ]':'064','[キャンディー]':'065','[いちご]':'066','[お茶]':'067','[おにぎり]':'068','[カクテルグラス]':'069','[キノコ]':'070','[コーヒー]':'071','[食パン]':'072','[ソフトクリーム]':'073','[チョコレート]':'074','[ナイフとフォーク]':'075','[オレンジ]':'076','[ビール]':'077','[ぶどう]':'078','[ハンバーガー]':'079','[リンゴ]':'080','[ワイン]':'081','[お団子]':'082','[ケーキ]':'083','[チーズ]':'084','[タバコ]':'085','[禁煙]':'086','[トイレ]':'087','[メガネ]':'088','[ひらめき電球]':'089','[ポスト]':'090','[家]':'091','[病院]':'092','[ビル]':'093','[お月見]':'094','[桜]':'095','[クリスマスツリー]':'096','[観覧車]':'097','[クラッカー]':'098','[鏡餅]':'099','[打ち上げ花火]':'100','[ハロウィン]':'101','[プレゼント]':'102','[耳]':'103','[グー]':'104','[チョキ]':'105','[パー]':'106','[携帯]':'107','[テレビ]':'108','[ヘッドフォン]':'109','[CD]':'110','[カメラ]':'111','[星]':'112','[指輪]':'113','[流れ星]':'114','[宝石ブルー]':'115','[宝石緑]':'116','[宝石紫]':'117','[宝石赤]':'118','[宝石白]':'119','[王冠１]':'120','[王冠２]':'121','[星空]':'122','[キラキラ]':'123','[雪の結晶]':'124','[車]':'125','[電車]':'126','[ロケット]':'127','[船]':'128','[飛行機]':'129','[UFO]':'130','[メモ]':'131','[旗]':'132','[カバン]':'133','[温泉]':'134','[ゲーム]':'135','[祝日]':'136','[ヒミツ]':'137','[イカリマーク]':'138','[ニコニコ]':'139','[プンプン]':'140','[ガーン]':'141','[かお]':'142','[ショック！]':'143','[しょぼん]':'144','[シラー]':'145','[むっ]':'146','[えっ]':'147','[帽子]':'148','[くつ]':'149','[サンダル]':'150','[かさ]':'151','[ドクロ]':'152','[手裏剣]':'153','[夜の街]':'154','[ナゾの人]':'155','[オバケ]':'156','[天使]':'157','[女の子]':'158','[男の子]':'159','[宇宙人]':'160','[ねこへび]':'161','[台風]':'162','[バスケ]':'163','[フラッグ]':'164','[新幹線]':'165','[バス]':'166','[美容院]':'167','[カラオケ]':'168','[リボン]':'169','[あし]':'170','[お月様]':'171','[手紙]':'172','[アップ]':'173','[キスマーク]':'174','[ダウン]':'175','[！！]':'176','[！？]':'177','[DASH!]':'178','[長音記号１]':'179','[長音記号２]':'180','[口紅]':'181','[ベル]':'182','[お金]':'183','[パソコン]':'184','[ラブレター]':'185','[ラブラブ！]':'186','[グッド！]':'187','[べーっだ！]':'188','[得意げ]':'189','[さくらんぼ]':'190','[お酒]':'191','[ラーメン]':'192','[にひひ]':'193','[ハート]':'194','[ダイヤ]':'195','[クラブ]':'196','[スペード]':'197','[モグラ]':'198','[将棋]':'199','[うんち]':'200','[カゼ]':'201','[おやしらず]':'202','[ヒマワリ]':'203','[ワンピース]':'204','[ネイル]':'205','[霧]':'211','[おひつじ座]':'212','[おうし座]':'213','[ふたご座]':'214','[かに座]':'215','[しし座]':'216','[おとめ座]':'217','[てんびん座]':'218','[さそり座]':'219','[いて座]':'220','[やぎ座]':'221','[みずがめ座]':'222','[うお座]':'223','[スポーツ]':'224','[ポケベル]':'225','[地下鉄]':'226','[銀行]':'227','[ATM]':'228','[ホテル]':'229','[コンビニ]':'230','[ガソリンスタント]':'231','[駐車場]':'232','[信号機]':'233','[映画]':'234','[右上矢印]':'235','[アート]':'237','[演劇]':'238','[チケット]':'239','[本]':'240','[電話]':'241','[目]':'242','[右下矢印]':'243','[左上矢印]':'244','[車椅子]':'245','[新月]':'246','[やや欠け月]':'247','[半月]':'248','[三日月]':'249','[満月]':'250','[左下矢印]':'251','[FAX]':'253','[叫び]':'254','[東京タワー]':'255','[ジェットコースター]':'256','[割り箸]':'257','[￥]':'258','[FREE]':'259','[ID]':'260','[カギ]':'261','[次項]':'262','[クリア]':'263','[サーチ]':'264','[NEW]':'265','[フリーダイヤル]':'266','[シャープ]':'267','[Q]':'268','[1]':'269','[2]':'270','[3]':'271','[4]':'272','[5]':'273','[6]':'274','[7]':'275','[8]':'276','[9]':'277','[0]':'278','[ドンッ]':'280','[カチンコ]':'281','[椅子]':'282','[右矢印]':'283','[左右矢印]':'284','[左矢印]':'285','[時計]':'286','[ロボット]':'287','[ドリル]':'288','[がま口財布]':'289','[ジーンズ]':'290','[ドア]':'291','[レンチ]':'292','[砂時計]':'293','[自転車]':'294','[腕時計]':'295','[クリップ]':'296','[コピーライト]':'297','[トレードマーク]':'298','[リサイクル]':'299','[レジスタードトレードマーク]':'300','[注意]':'301','[禁止]':'302','[空]':'303','[合格]':'304','[満]':'305','[上下矢印]':'307','[学校]':'308','[富士山]':'309','[バナナ]':'310','[もみじ]':'312','[かたつむり]':'313','[馬]':'314','[ガックリ]':'337','[チョコ]':'338','[バレンタインチョコ]':'339','[おひなさま]':'340','[桜餅]':'341','[スキー]':'343','[アメーバ]':'344'};

// 絵文字かどうかの判定
function is_emoji(str){
	// 文字列のマッチング処理
	if(emoji_list[str]){
		return true;
	}
	return false;
}

// 絵文字を含んだ文字列長を計算
function emoji_strlen(str,n){
	var result = str.match(/(\[[^\[\]]+\]|.|\r\n|\n|\r)/g);
	var result_str ='';
	    for(var i=0; i<result.length; i++){
	        if(i == n) break;
            result_str += result[i];
	    }
	    r = new Array();
	    r[0] = result.length;
	    r[1] = result_str;
	return r;
}

// 文字列中の絵文字タグをHTMLタグへ変換
function emoji_rendor(str){
	str = str.replace(/(\[[^\[\]]+\])/g, emoji_replace_callback);
	return str;
}
function emoji_replace_callback(str){
	var class_name = emoji_list[str];
	if(class_name){
		var length = str.length;
		str = str.slice(1,length-1);
		str = '<img data-defer-src="'+ emoji_image_path + class_name +'.gif" alt="['+ str + ']" class="spacer">';
	}
	return str;
}


////////////////////////////////////////////////////////////////////////////////
/// native アプリ用
////////////////////////////////////////////////////////////////////////////////
/*
写真セット
----------------------------------------------------------------------*/
function setCommonImage(imgId, base64ImgData) {
	var img_disp = "js-disp_" + imgId;
	var img_hidden = "js-hidden_" + imgId;
	var data = "data:image/png;base64," + base64ImgData;//表示用
	$('#'+img_disp).attr("src", data);//imgの場合
	$('#'+img_disp).css("background-image","url("+data+")");//backgroundの場合
	$('#'+img_hidden).val(base64ImgData);//hiddenに設定
}
/*
写真クリア
----------------------------------------------------------------------*/
function clearCommonImage(imgId) {
	$('#js-hidden_'+imgId).val('');
}

/*
カバー写真リストへリダイレクト
----------------------------------------------------------------------*/
function moveDefaultCaverimage() {
	$(".js-defaultCoverimage").displayBlock();
	$(".js-main_page,.js-app_header,.js-tab,.js-footer,#deca_header,#deca_footer,#amb_header,.ad_frame").displayNone();

}

/*
andoroid用 バックキー対応
----------------------------------------------------------------------*/
function goBack(){
	var flag;
	if($('.backBtn').size()){
		flag=1;
		$('.backBtn').click();
	}else{
		flag=0;
	}
	return flag;
}



