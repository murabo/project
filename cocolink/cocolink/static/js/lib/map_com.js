
	var Map = function() {};
	Map.prototype = $.extend({}, GetListUtil.prototype, {

		init: function() {
			this._bind();
			this._initialize();
		},
		_initialize :function() {
			self.ajax = $.extend({}, Super.prototype, AjaxUtil.prototype);
			self.ajaxvo = new AjaxVo;
		},
		_bind: function() {

			//$(".js-submit").on("click", this.get_place_list);

		},
		_map: '',
		//現在地の座標取得
		get_present_location: function() {



		},
		//現在地取得
		get_map: function(callback){

			var that = this;

			var openInfoWindow;
			var lat="";
			var lng="";

			// 位置情報取得に成功したとき
			var position = function (position) {
				lat = position.coords.latitude;
				lng = position.coords.longitude;

				var latlng = new google.maps.LatLng(lat, lng);
				var myOptions = {
					zoom: 19,
					center: latlng,
					mapTypeId: google.maps.MapTypeId.ROADMAP
				};
				that.map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
				var marker = new google.maps.Marker({
					position: latlng,
					map: that.map,
				});

				$("body").data("lat",lat);
				$("body").data("lng",lng);

				//that.get_place_list();
				that.change_area();
			}
			// 位置情報取得に失敗したとき
			var error = function (error) {
				alert(error.message);
			}
			// 位置情報取得時に設定するオプション
			var option = {
				enableHighAccuracy: true,
				maximumAge: 60*2000,
				timeout : 1000,
			};
			//初期表示で現在地を表示
			navigator.geolocation.getCurrentPosition( position , error , option);
		},
		get_place_list: function(bounds){

			var template = $.trim($('#template').html());

			$.ajax({
				url: api_path['place'],
				type : 'GET',
				dataType: 'jsonp',
				 data:  {
					 	location: (undefined == bounds)? $("body").data("lat") +"," + $("body").data("lng") : "",
						radius: (undefined == bounds)? 1000 : "",
						bounds: (undefined == bounds)? "" : bounds,
						types: '',//複数おk
						language: 'ja',
						rankby: 'prominence',//重要度(デフォルトだから指定いらないかも)
						sensor: 'false',//gps
						key: 'AIzaSyBmZZTB4DAdN9OZq3K2NqYpgqZzDuc2am8'
				     },
				timeout: 15000,
				cache: false,
				beforeSend: function() {
				},
				jsonp : 'callback',
				error: function(data){
					alert('エラーが発生しました！');
				},
				success: function(data) {
					createList(data.results);
				},
				complete: function (data){

				}

			});


			function createList(results){

				var frag ="";
				var len= results.length;
				for (var i = 0; i < len; i++){

				    var properties = '';
				    var g = results[i].geometry['location'];
				    for (var prop in g){
				        properties += g[prop];
				    }

					frag+= template.replace( /{{name}}/ig, results[i].name)
									.replace( /{{icon}}/ig, results[i].icon)
									.replace( /{{lat}}/ig, g['lat'])
									.replace( /{{lng}}/ig, g['lng'])
									//.replace( /{{formatted_address}}/ig, results[i].formatted_address)
									.replace( /{{vicinity}}/ig, (undefined == results[i].vicinity)?"":results[i].vicinity );
				}
				$("#js-result-list").html("").html(frag);
			}


		},
		//詳細住所取得
		geocoder: function(that){

			var lat =that.find('.js-lat').val();
			var lng =that.find('.js-lng').val();

			//ジオコードオブジェクト
			var geocoder = new google.maps.Geocoder();
			geocoder.geocode(
			  {
			    'latLng': lat+','+lng
			  },
			  function(results, status){
			    if(status==google.maps.GeocoderStatus.OK){
			    	//処理
			    	alert(results);
			    }
			  }
			);

		},
		//地図の範囲変更
		//TODO
		change_area: function(){


			var that = this;
			google.maps.event.addListener(that.map, 'drag', dispLatLng);
			google.maps.event.addListener(that.map, "zoom_changed", dispLatLng);

			function dispLatLng(){

				  var latlng = that.map.getCenter();

				  var str = "[CENTER]=[" + latlng.lat() + "," + latlng.lng() + "]<br />";

				  var latlngBounds = that.map.getBounds();
				  var swLatlng = latlngBounds.getSouthWest();
				  str = str + "[SouthWest]=[" + swLatlng.lat() + "," + swLatlng.lng() + "]<br />";

				  var neLatlng = latlngBounds.getNorthEast();
				  str = str + "[NorthEast]=[" + neLatlng.lat() + "," + neLatlng.lng() + "]";


				$("body").data("lat",latlng.lat());
				$("body").data("lng",latlng.lng());

				//送信用
				var defaultBounds = new google.maps.LatLngBounds(
					new google.maps.LatLng(swLatlng.lat(),swLatlng.lng()),
					new google.maps.LatLng(neLatlng.lat(),neLatlng.lng()));


				$("body").data("defaultBounds",defaultBounds);

				document.getElementById("latlng").innerHTML = str;
			}
		},
		//File APIs 対応チェック
		check_browser: function(){
			if (window.File && window.FileReader && window.FileList && window.Blob) {
				$('#files').displayBlock();
				document.getElementById('files').addEventListener('change', this._handleFileSelect, false);
			}

		},
		//File 選択時の処理
		_handleFileSelect: function(event){

			var files = event.target.files;

			if( 1 < files.length){
				//TODO エラー処理
				alert('1ファイル選択してください');
			}else{
				var f = files[0];
				// 画像ファイルかテキスト・ファイルかを判定
				if (!f.type.match('image.*')) {
					alert("画像ファイルとテキスト・ファイル以外は表示できません。");
				}else{
					// FileReaderオブジェクトの生成
					var reader = new FileReader();
					// エラー発生時の処理
					reader.onerror = function (evt) {
						alert("読みとりに失敗しました");
					}

					var disp = $(".js-disp-img");

					// 画像ファイルの場合の処理
					if (f.type.match('image.*')) {
						// ファイル読取が完了した際に呼ばれる処理
						reader.onload = function (evt) {
						var src = evt.target.result;
							$('.js-disp-img').attr("src",src);
							$('.js-post-data-url').val(src);
						}

						// readAsDataURLメソッドでファイルの内容を取得
						reader.readAsDataURL(f);

					}
				}
			}

		}



	});




