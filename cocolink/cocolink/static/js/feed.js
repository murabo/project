$(function() {

	var Feed = function() {};
	Feed.prototype = $.extend({}, GetListUtil.prototype, {

		init: function() {

			this.template = $.trim($('#template').html());//テンプレート

			//一覧取得用 vo
			this.searchVo = new AjaxVo();
			this.searchVo.path = api_path['feed'];
			this.searchVo.data = {'offset':10,'limit':10};

			this._bind();
		},

		_bind: function() {

			var that = this;
			that.get(that.searchVo);

			this.searchVo.next_btn.on('click', function(event) {
				that.get(that.searchVo);
			});

			$('.js_btn_plus').plus();

			$('.menu').on('click', function(event) {
				$('.menu').addClass('anime');
			})

			//document.getElementById("target").className = "slide";
			//document.getElementById("target").style.left = '190px';





		},

		template :null,

		render : function(data) {

			var frag='';
			var $body = $('body');
			var template = this.template;

			$.each(data.feed, function(i,val){

				//投稿画像
				var image = '';
				for (var j in val['images']){
					//image += '<div class="post_images clear"><img src="'+htmlEscape(val['images'][j]) +'"></div>';
				}
				//ボタン
				var btn = '';
					if(val['mine_plus_flg'] == 0 ){
						//btn =  $body.data('Thanks').settings.praises_icon;
					}else{
						//btn = $body.data('Thanks').settings.praised_icon;
					}

				frag += template.replace( /{{id}}/ig,encodeURI(val['id']))
								.replace( /{{content}}/ig,htmlEscape(val['content']))
								.replace( /{{images}}/ig,image)
								.replace( /{{zip}}/ig,htmlEscape(val['user_id']))
								.replace( /{{mine_flg}}/ig,htmlEscape(val['mine_flg']))
								.replace( /{{create_datetime}}/ig, time_ago(val['create_datetime']))
								.replace( /{{btn}}/ig,btn);

			});
			return frag;
		}

	});

	var feed = new Feed();
	feed.init();


});



