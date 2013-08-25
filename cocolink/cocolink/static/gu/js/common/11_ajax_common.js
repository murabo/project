/*
url
----------------------------------------------------------------------*/
api_url = base_url+'api/1/';
api_path = new Object();
api_path['disconnect'] = api_url+'oauth/disconnect';// 共有設定
api_path['notification'] = api_url+'user/notification_setting';// アプリ通知設定
// ユーザ
api_path['user_update'] = api_url+'user/update';//個人情報登録
api_path['user_search'] = api_url+'user/search';//ユーザ検索
api_path['user_invite'] = api_url+'user/invite';//ユーザ招待
api_path['update_action'] = api_url+'user/update_action';//ユーザーアクション更新
api_path['model_list'] = api_url+'user/reader_model_list';//オフィシャルユーザー一覧
api_path['official_img_list'] = api_url+'/user/official_image_add_flush_list';//オフィシャルユーザー用画像一覧取得
api_path['recent_post_list'] = api_url+'user/recent_post_list';//ユーザ投稿一覧
api_path['contribute_praise'] = api_url+'user/praise_list';//褒められた一覧
api_path['contribute_thanked'] = api_url+'user/thanked_list';//ありがとう一覧
api_path['community_user_join'] = api_url+'user/join_list';//フォローコミュニティ一覧
api_path['user_ranking'] = api_url+'user/user_ranking_list';//ユーザーランキング
api_path['user_ranking_participation'] = api_url+'user/user_ranking_participation';//ユーザーランキング参加可否
//diary
api_path['diary_name_update'] = api_url+'diary/set_diary_name';//個人情報登録
api_path['diary_cover_update'] = api_url+'diary/update_diary_image';//カバー写真更新
api_path['user_tweets'] = api_url+'diary/user_tweets_limit_date';//ダイアリー用ツイート一覧取得
api_path['diary_access'] = api_url+'diary/diary_access';//アクセスカウント用
//トピック
api_path['contributed_list'] = api_url+'topic/contributed_list';//投稿があった最近のトピック
api_path['topic_list'] = api_url+'topic/timeline';//トピック一覧
api_path['topic_push_list'] = api_url+'topic/push_list';//トピック投稿プッシュメンバー取得
api_path['topic_delete'] = api_url+'topic/delete';//トピック削除

//トピック投稿
api_path['topic_contribute_post'] = api_url+'topic_contribute/regist';//トピック投稿
api_path['topic_contribute_share'] = api_url+'topic_contribute/share';//トピック投稿をSNSへ共有
api_path['topic_contribute_push'] = api_url+'topic_contribute_push/regist';//トピックプッシュ投稿
api_path['comment_push'] = api_url+'topic_contribute_comment_push/comment_push_regist';//コメントプッシュ投稿
api_path['topic_contribute_comment'] = api_url+'topic_contribute_comment/regist';//トピックコメント投稿
api_path['topic_contribute_delete'] = api_url+'topic_contribute/delete';//トピック投稿削除
api_path['topic_contribute_hot_list'] = api_url+'topic_contribute/hot_list';//ホットツイート一覧取得
api_path['topic_contribute_comment_delete'] = api_url+'topic_contribute_comment/delete';//トピック投稿コメント削除
api_path['push_thank'] = api_url+'topic_contribute_push/push_thank';//トピック投稿プッシュへありがとうAPI
api_path['comment_push_thank'] = api_url+'topic_contribute_comment_push/comment_push_thank';//コメントほめるにありがとうAPI
api_path['comment_list'] = api_url+'topic_contribute_comment/comment_list';//トピック投稿コメント一覧取得
api_path['comment_push_list'] = api_url+'topic/comment_push_list';//褒められた一覧
api_path['flush_list'] = api_url+'topic/flush_list';//フラッシュリスト
//タイムライン
api_path['timeline'] = api_url+'feed/timeline';//タイムライン
api_path['timeline_by_last_id'] = api_url+'feed/timeline_by_last_id';//タイムライン(トップで使用)
api_path['official_timeline'] = api_url+'topic_contribute/official_timeline';//オフィシャル用タイムライン
//マイコミュ
api_path['community_feed'] = api_url+'user/community_feed';//ありがとう一覧
api_path['contributable_list'] = api_url+'topic/contributable_list';//フォローシテイル美活コミュ一覧
//新着
api_path['news_list'] = api_url+'news/news_list';//新着一覧取得
api_path['comment_news_list'] = api_url+'news/comment_news_list';//コメント新着一覧取得
api_path['follow_news_list'] = api_url+'news/follow_news_list';//フォロー新着一覧取得
api_path['topic_news_list'] = api_url+'/news/topic_news_list';//新着おしゃべり管理一覧
api_path['news_checked'] = api_url+'news/add_checked';//新着既読
//ネイティブアプリ用
api_path['register_token'] = base_url+'app/notification/register_token';//アプリトークン
//イベント用
api_path['treasure_find'] = base_url+'api/1/treasure/find';
//フォロー
api_path['favorite_regist'] = api_url+'favorite/regist';//フォロー登録
api_path['favorite_delete'] = api_url+'favorite/delete';//フォロー削除
api_path['favorite_list'] = api_url+'favorite/favorite_list';//フォローしてる人一覧
//フォロワー
api_path['registerd_list'] = api_url+'favorite/registerd_list';//フォローしてくれてる人一覧
//ダイアリー
api_path['pictures'] = api_url+'diary/pictures';//フォト一覧
api_path['cal_weekly'] = api_url+'diary/calendar_weekly_list';//週間カレンダー
api_path['cal_monthly'] = api_url+'diary/calendar_month_list';//月刊カレンダー
//ネタ別フォード
api_path['theme_timeline'] = api_url+'topic_contribute/theme_timeline';//ネタ毎フィード一覧取得
api_path['theme_group_timeline'] = api_url+'topic_contribute/theme_group_timeline';//ネタ複数フィード一覧取得
api_path['hitokoto_regist'] = api_url+'topic_contribute/hitokoto_regist';//ひとこと
api_path['campaign_timeline'] = api_url+'topic_contribute/campaign_timeline';//campaign_timeline

//キャンペーン用
api_path['tracking'] = api_url+'tracking/ameba';//トラッキング

//キャンペーン用
//api_path['set_weight'] = api_url+'diet/set_weight';//体重更新
//api_path['get_summary'] = api_url+'diet/get_weight_summary';//体重更新
api_path['enquete_answer'] = api_url+'enquete/answer';//アンケート

api_path['timeline'] = 'http://127.0.0.1:8080/static/sample/json/timeline.json';//アンケート


/*===================================================================================
ajax用 util vo
===================================================================================*/
/*
ajax用 value object
-------------------------------	---------------------------------------*/
var AjaxVo = function() {
	this.path = '';
	this.page = '';
	this.type = 'POST';
	this.data = '';
	this.result = false;
	this.next_btn = $('.js-btn_more');
	this.target = $("#list");
	this.module = '';
	this.cnt = 0;
};
//ロード中アイコン
var icon_load_img = '<div class = "taCenter js-ajax_anime"><span class="icon_load_img mr10"></span><span class="text_col_pglnk text13">読み込み中</span></div>';

/*
ajax用 通信用 Util
-------------------------------	---------------------------------------*/
var AjaxUtil = function() {
	this.flag_exec = true;
};
AjaxUtil.prototype = {

	ajax: function(ajaxVo, callback) {

		if(this.flag_exec==false) return;
		if(ajaxVo.type == "POST") ajaxVo.data['csrf_test_name'] = getCookie('csrf_cookie_name');

		var rec = {};

		$.ajax({
			url: ajaxVo.path,
			type: ajaxVo.type,
			dataType: 'json',
			data: ajaxVo.data,
			timeout: 100000,
			cache: false,
			beforeSend: function() {this.flag_exec=false;},
			error: function(data){rec.err = data; callback(rec);},
			success: function(data) {rec.suc = data; callback(rec);},
			complete: function (data){this.flag_exec=true;}
		});

	},

	execute: function(ajaxVo, callback) {
		$('.error').html('');
		var that = this;
		that.ajax(ajaxVo, function(result){
			if(!result.err && result.suc['response']['result_code']=='1'){
				(result.suc['response']['result']=='') ? ajaxVo.result = true: ajaxVo.result = result.suc['response']['result'];
				callback(ajaxVo);
			}else{
				that.error(result.err);
			}
		});
	},

	error: function(data) {
		$('body').enableBtn();
		var error_obj = $.parseJSON(data.responseText);
		if(error_obj.response.error.code=='400'){
			$.each(error_obj.response.error.params, function(key,value){
				$('#js-'+key+'_error').text(value);
			});
		}else if(error_obj.response.error.code=='401'){
			location.href=base_url+"web/login/index";
		}else if(error_obj.response.error.code=='409'){
			alert(error_obj.response.error.params['display_message']);
		}else{
			alert(error_obj.response.error.code + '/'+ error_obj.response.error.message);
		}
	}

}

/*
リスト生成用 Util
-------------------------------	---------------------------------------*/
var GetListUtil = function () {
	this._next_read_pos = 0;
};
GetListUtil.prototype = $.extend({}, AjaxUtil.prototype, {

	get: function(ajaxVo) {
		ajaxVo.next_btn.displayNone();
		ajaxVo.next_btn.after(icon_load_img);
		ajaxVo.type = 'GET';
		var that = this;
		that.execute(ajaxVo , function(ajaxVoResponse){
			ajaxVo.next_btn.next('.js-ajax_anime').remove();
			var templ = that.render(ajaxVoResponse.result);
			var html = templ.replace( /{{base_url}}/ig, base_url);
			ajaxVoResponse.target.append(html);
			$('body').defer();
			ajaxVoResponse.data.offset = ajaxVoResponse.result['next_offset'];

			if(arrayKeyExists('has_next',ajaxVoResponse.result)){
				if(ajaxVoResponse.result['has_next'] != false){
					ajaxVoResponse.next_btn.displayBlock();
					ajaxVoResponse.data.last_id = ajaxVoResponse.result['last_id'];
				}
			}else{
				if (ajaxVoResponse.data.offset != false){
					ajaxVoResponse.next_btn.displayBlock();
				};
			}
		});
	},
	get_list: function(ajaxVo) {
		ajaxVo.next_btn.displayNone();
		ajaxVo.next_btn.after(icon_load_img);
		ajaxVo.type = 'GET';
		var that = this;
		that.execute(ajaxVo , function(ajaxVoResponse){
			ajaxVo.next_btn.next('.js-ajax_anime').remove();
			var templ = that.render(ajaxVoResponse.result);
			var html = templ.replace( /{{base_url}}/ig, base_url);

			ajaxVoResponse.next_btn.before(html);
			$('body').defer();
			ajaxVoResponse.data.offset = ajaxVoResponse.result['next_offset'];
			if (ajaxVoResponse.data.offset != false){
				ajaxVoResponse.next_btn.displayBlock();
			};

		});
	},
	_next: function(ajaxVo) {
		var that = this;
		ajaxVo.next_btn.on('click', function(event) {
			that.get(ajaxVo);
		});
	},
	get_bottom: function(ajaxVo,cnt) {
		var that = this;
		that._flag_exec = false;
		ajaxVo.next_btn.after(icon_load_img);
		ajaxVo.type = 'GET';
		var that = this;

		that.execute(ajaxVo , function(ajaxVoResponse){
			ajaxVo.next_btn.next('.js-ajax_anime').remove();
			var templ = that.render(ajaxVoResponse.result);
			var html = templ.replace( /{{base_url}}/ig, base_url);
			_gaq.push(['_trackEvent', ajaxVo.page, 'infinityscroll', String(ajaxVo.cnt) + '回目', 0, true]);
			if(ajaxVo.cnt > 0 && ajaxVo.cnt%3 === 0){
				ajaxVoResponse.target.append(ajaxVo.module+ html);
			}else{
				ajaxVoResponse.target.append(html);
			}

			$('body').defer();
			ajaxVoResponse.data.offset = ajaxVoResponse.result['next_offset'];
			that._next_read_pos = $('#js-btn_more_pos').offset().top;
			ajaxVo.cnt++;

			if(arrayKeyExists('has_next',ajaxVoResponse.result)){
				if(ajaxVoResponse.result['has_next'] != false){
					if(cnt && (cnt == ajaxVo.cnt)){
						$(window).off("scroll");
						ajaxVoResponse.next_btn.displayBlock();
					}
				}else{
					$(window).off("scroll");
					ajaxVoResponse.next_btn.displayNone();
				};
				ajaxVoResponse.data.last_id = ajaxVoResponse.result['last_id'];
			}else{
				if (ajaxVoResponse.data.offset != false){
					if(cnt && (cnt == ajaxVo.cnt)){
						$(window).off("scroll");
						ajaxVoResponse.next_btn.displayBlock();
					}
				}else{
					$(window).off("scroll");
					ajaxVoResponse.next_btn.displayNone();
				}
			}

			that._flag_exec = true;
		});
	},
	_bottom: function(ajaxVo,cnt) {

		var that = this;
		var scroll=0;
		var win_h = $(window).height();

		//setTimeout(function(){
			if($('#next_offset').val() != false){
				that._next_read_pos = $('#js-btn_more_pos').offset().top;
				that.get_bottom(ajaxVo,cnt);//1回目実行
				$(window).on("scroll",function() {
					scroll =  win_h + (document.documentElement.scrollTop || document.body.scrollTop);
					if (that._flag_exec == true && ( (that._next_read_pos - scroll)/ scroll <= 0.15)) {
						that.get_bottom(ajaxVo,cnt);
					}
				});
			}
	//	},1000);

	},
	_flag_exec: true,
	_bind: function(ajaxVo) {},
	_render: function(result) { }
});


var Super = function () {};
Super.prototype = {
	_getid: function(self) {
		return self.attr('id').split("_");
	}
}

/*===================================================================================
native アプリ用
===================================================================================*/
/*
デバイストークン取得
----------------------------------------------------------------------*/
function setDeviceToken(token) {

	if(token){
		var ajaxvoutil = $.extend({},AjaxUtil.prototype);
		ajaxvoutil.error = function() { };//エラー処理行わない
		var ajaxvo = new AjaxVo;
		ajaxvo.data = {'token' : token};
		ajaxvo.path = api_path['register_token'];

		ajaxvoutil.execute(ajaxvo , function(ajaxVoResponse){
			location.href = 'glup://clearDeviceToken/';
		});
	}
}


/*===================================================================================
バリデート
===================================================================================*/
var error={ lobo_title:'タイトル欄は１８文字以内で入力する必要があります',
			lobo_category:'カテゴリを一つ以上選択してください',
			lobo_img:'画像を選択してください',
			lobo_introduction:'詳細を入力してください',
			prof_byte:'ニックネーム欄は１０文字以内で入力する必要があります',
			prof_isset:'ニックネーム欄は必須です',
			prof_birthday:'正しい日付を入力してください',
			prof_diary_byte:'ダイアリー名は１6文字以内で入力する必要があります',
			prof_diary_isset:'ダイアリー名は必須です'
}
var Validate = function(){};
//エラーの表示
Validate.prototype.error = function (obj,error) {
	$('#'+obj.attr('id')+'_error').text(error);
	$('body').enableBtn();
}

//空文字
Validate.prototype.isset = function (obj,error) {
	if (!obj.val().match(/\S/g)){
		if(error != ''){
			this.error(obj,error);
		}
		return true;
	}
	return false;
}
//日付
Validate.prototype.checkDate = function (obj,error,year, month, day){
	var dt = new Date(year, month - 1, day);
	if(dt == null || dt.getFullYear() != year || dt.getMonth() + 1 != month || dt.getDate() != day) {
		this.error(obj,error);
		return true;
	}
	return false;
}

//YYYY-MM-DD形式にフォーマット
Validate.prototype.formatDate = function (year, month, day){
	return function(){
		if(month<10)month='0'+month;
		if(day<10)day='0'+day;
		return year + '-' +month +'-' +  day
	};
}
//カウンター
Validate.prototype.counter = function (obj,counter_id,num){
	var timer = -1;
	obj.focus(function(){
		if (timer != -1) {
			clearInterval(timer);
		}
		timer = setInterval(function(){
			counter = num-obj.val().length;
			if(0 < counter){
				counter_id.text(counter);
			}else{
				counter_id.text(0);
			}
		},100);
	});
}
//文字数チェック
Validate.prototype.checkCount = function (obj,error,length){
	if (length < obj.val().length){
		if(error != ''){
			this.error(obj,error);
		}
		return true;
	}
	return false;
}


/*
ユーザアクション更新
----------------------------------------------------------------------*/
function updateAction(action_type) {
	var ajaxvoutil = $.extend({},AjaxUtil.prototype);
	ajaxvoutil.error = function() { };//エラー処理行わない
	var ajaxvo = new AjaxVo;
	ajaxvo.data = {'action_type' : action_type,'action_status' : 1,};
	ajaxvo.path = api_path['update_action'];
	ajaxvoutil.execute(ajaxvo , function(ajaxVoResponse){});
	delete ajaxvo;
}

/*
フラッシュリスト
----------------------------------------------------------------------*/
var FlushList = function(){};
FlushList.prototype = $.extend({}, GetListUtil.prototype, {
	init: function() {

		//一覧取得用 vo
		this.searchVo = new AjaxVo();
		this.searchVo.path = api_path['flush_list'];
		this.searchVo.data = {'offset': 7, 'limit': 6};
		this.searchVo.next_btn = $('#js_flush_more_btn');
		this.template = $.trim($('#flush_list_tpl').html());
		this._bind();
	},
	_bind: function() {

		var that = this;
		$(document).on('click', '.js_flush_more_btn' ,function() {
			that.get_list(that.searchVo);
		});

	},
	render: function(data) {

		var that = this;
		var frag = '';
		var template = this.template;
		var randnum = Math.floor( Math.random() * (that.searchVo.data.limit--));
		var ran = Math.floor(Math.random() * 3) + 1
		var icon ="";

		if(ran == 1){
			icon = '<p class="tag icon_col_1 ml2">HOT!</p>';
		}else if(ran == 2){
			icon = '<p class="tag icon_col_2 ml2">人気</p>';
		}else{
			icon = '<p class="tag icon_col_3 ml2">大人気</p>';
		}

		$.each(data.list, function(i, val) {

			frag+= template.replace( /{{url}}/ig, encodeURI(val['url']))
					.replace( /{{title}}/ig,emoji_rendor(val['title']))
					.replace( /{{icon}}/ig, (ran == i)? icon :'')
					.replace( /{{new}}/ig, (val['within'])? '<span class="sprite_image icon_new04 mt5"></span>' :'')
					.replace( /{{time}}/ig,time_ago(val['start_datetime']));

		});
		return frag;
	}
});









