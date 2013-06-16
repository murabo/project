/*
url
----------------------------------------------------------------------*/
//api_url = base_url+'api/1/';
api_url = '../json/';
api_path = new Object();
api_path['feed'] = api_url+'feed.json';// フィード
api_path['place'] = 'http://localhost/project/OpenPNE3/apps/api/google_place_api.php';// フィード

//api_path['plus'] = api_url+'plus.json';// maplus


/*
ajax用 value object
-------------------------------	---------------------------------------*/
var AjaxVo = function() {
	this.path = '';
	this.type = 'POST';
	this.datatype = 'json';
	this.data = '';
	this.result = false;
	this.next_btn = $('.js-btn_more');
	this.target = $("#js_addlist");
};
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
			dataType: ajaxVo.datatype,
			data: ajaxVo.data,
			timeout: 15000,
			cache: false,
			beforeSend: function() {this.flag_exec=false;},
			error: function(data){rec.err = data; callback(rec);},
			success: function(data) {rec.suc = data; callback(rec);},
			complete: function (data){this.flag_exec=true;}
		});
	},

	execute: function(ajaxVo, callback) {
		$('body').disabledBtn();
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
		}else{
			alert(error_obj.response.error.code + '/'+ error_obj.response.error.message);
		}
	}

}

/*
リスト生成用 Util
-------------------------------	---------------------------------------*/
var GetListUtil = function () {

};
GetListUtil.prototype = $.extend({}, AjaxUtil.prototype, {

	get: function(ajaxVo) {
		ajaxVo.type = 'GET';
		var that = this;
		that.execute(ajaxVo , function(ajaxVoResponse){
			var templ = that.render(ajaxVoResponse.result);
			ajaxVoResponse.data.offset = ajaxVoResponse.result['next_offset'];
			//var html = templ.replace( /{{base_url}}/ig, base_url);
			//ajaxVoResponse.target.append(html);
			ajaxVoResponse.target.append(templ);
			$('body').defer();
			(ajaxVoResponse.data.offset == false)? ajaxVoResponse.next_btn.displayNone() : ajaxVoResponse.next_btn.displayBlock();
		});
	},
	_bind: function(ajaxVo) { },
	_render: function(result) { }
});

var Super = function () {};
Super.prototype = {
	_getid: function(self) {
		return self.attr('id').split("_");
	}
}


/*===================================================================================
バリデート
===================================================================================*/
var Validate = function(){};
//エラーの表示
Validate.prototype.error = function (obj,error) {

	$('#'+obj.attr('id')+'-error').text(error);
	$('body').enableBtn();
}
//文字数チェック
Validate.prototype.count = function (obj,minnum,maxnum,error) {

	var len = obj.val().length;

	if( (minnum && (len < minnum)) || (maxnum && (len > maxnum)) ){
		this.error(obj,error);
		return true;
	}

	return false;
}




//空文字(未使用)
Validate.prototype.isset = function (obj,error) {
	if (!obj.val().match(/\S/g)){
		if(error != ''){
			this.error(obj,error);
		}
		return true;
	}
	return false;
}

//日付(未使用)
Validate.prototype.checkDate = function (obj,error,year, month, day){
	var dt = new Date(year, month - 1, day);
	if(dt == null || dt.getFullYear() != year || dt.getMonth() + 1 != month || dt.getDate() != day) {
		this.error(obj,error);
		return true;
	}
	return false;
}

//YYYY-MM-DD形式にフォーマット(未使用)
Validate.prototype.formatDate = function (year, month, day){
	return function(){
		if(month<10)month='0'+month;
		if(day<10)day='0'+day;
		return year + '-' +month +'-' +  day
	};
}

