
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


			var that = this;

			//検索ボタン
			$(".js-search").click(function(){
				$(".js-result-list").html('');//検索結果一覧初期化
				that.crearMarker();//マーカー削除
				that.get_place_list();//検索結果一覧取得
			});

			//現在地に戻る
			$(".js-current").click(function(){
				$(".js-result-list").html('');
				that.crearMarker();//マーカー削除
				that.get_map();//現在地取得
			});

			//検索結果一覧画面、投稿画面切り替え
			$(".js−dsp_map_page").click(function() {
				$(".js-list-pege").toggleClass("disp_block disp_none");
				$(".js-map-page").toggleClass("disp_block disp_none");
			});

			//入力した住所へ地図移動
			$(".js-geocoding").click(function(){
				that.geocoding($("#js-geocoding-input").val());
			});

			//住所入力テキストボックス表示
			$(".js-dsp-zip-input-bx").click(function(){
				$(".js-zip-input-bx").toggleClass("disp_block disp_none");
			});

			//キーワード検索入力テキスト画面表示
			$(".js-dsp-category-input-bx").click(function(){
				$(".js-list-pege").toggleClass("disp_block disp_none");
				$(".js-map-page").toggleClass("disp_block disp_none");
			});

			//検索結果一覧から選択
			$(document).on('click', '.js-result-list li', function() {
				that._dsp_place_info($(this));
				$(".js-list-pege").toggleClass("disp_block disp_none");
				$(".js-map-page").toggleClass("disp_block disp_none");	
			});

			//mapをクリックして住所を取得、その住所で投稿
			$(document).on('click', '.js-post', function() {
			 	that._toggle_txt_page();
			// 	//self.map.geocoder($(this));//詳細住所はとりあえず取得なし！
			 });


			//キーワード検索入力テキスト画面表示
			$(".js-select-place-bx").click(function(){
				that._set_default_zip();
			});

			//キーワード検索入力テキスト画面表示
			$(".js-more-btn").click(function(){
				that.get_place_list();//検索結果一覧取得
			});


		},
		_map: '',
		_markersArray : [],
		//現在地の座標取得
		get_present_location: function() {



		},
		//指定した住所の地図表示
		get_map: function(latlng){

			var that = this;

			// 位置情報取得に成功したとき
			var position = function (position) {

				var lat = null,lng = null;

				if(!latlng){
					lat = position.coords.latitude;
					lng = position.coords.longitude;
					latlng = new google.maps.LatLng(lat, lng);
				}

				var myOptions = {
					zoom: 15,
					center: latlng,
					mapTypeId: google.maps.MapTypeId.ROADMAP
				};

				that.map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
				var marker = new google.maps.Marker({
					position: latlng,
					map: that.map,
				});
				that._markersArray.push(marker);

				$("body").data("lat",lat);
				$("body").data("lng",lng);

				//TODO 共通化する
				var request = { 
                	latLng: latlng
            	}; 
 				var geocoder = new google.maps.Geocoder(); 
            	geocoder.geocode(request, function(results, status) { 
                // ステータスがOKならマーカーを表示する。 
	                if (status == google.maps.GeocoderStatus.OK) { 
		                $(".js-place-text").html(results[0].formatted_address);

						// var loc = results[0]['geometry']['location'].toString();
						// loc = loc.replace(/\(|\)|\s+/ig, '');
						// loc = loc.split(',');
						// $(".js-subumit-lat").val(loc[0]);
						// $(".js-subumit-lng").val(loc[1]);
	                } 
          		}); 


				google.maps.event.addListener(that.map, 'click', that.click_map);
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
		//地図のクリックイベント
		click_map: function (event){

      		//alert(event.latLng.toString());
			var that = this;
            // 東京タワーをジオコーディング 
            var request = { 
                latLng: event.latLng
            }; 
 
            var geocoder = new google.maps.Geocoder(); 
            geocoder.geocode(request, function(results, status) { 
                // ステータスがOKならマーカーを表示する。 
                if (status == google.maps.GeocoderStatus.OK) { 
                	$(".js-place-text").html(results[0].formatted_address);

					var loc = results[0]['geometry']['location'].toString();
					loc = loc.replace(/\(|\)|\s+/ig, '');
					loc = loc.split(',');
					//$(".js-subumit-lat").val(loc[0]);
					//$(".js-subumit-lng").val(loc[1]);
					
					$("body").data("lat",loc[0]);
					$("body").data("lng",loc[1]);

					//TODO クリックした箇所にマーカー表示
					//that.setMarkers('yes', that.map, loc);
                } 
           }); 

		},

		//一覧取得
		get_place_list: function(){

			var that = this;
			var locations = new Array();

			var template = $.trim($('#template').html());
			var pyrmont = new google.maps.LatLng($("body").data("lat"),$("body").data("lng"));

			var types = new Array();
			if ( $('#category option:selected').val() != '' ){
				types.push($('#category option:selected').val());
			};

 			 var request = {
			    location: pyrmont,
			    radius: '500',
			    bounds : $("body").data("defaultBounds"),
			    types: types,
			  　keyword : $('#js-q-input').val(),//中華手をキーワード検索
			    //query: $('#js-q-input').val()
			  };

			var service = new google.maps.places.PlacesService(that.map);
			service.search(request, createList);

			function createList(results, status,pagination){

 			 	if (status == google.maps.places.PlacesServiceStatus.OK) {

					var frag ="";
					var len= results.length;
					for (var i = 0; i < len; i++){

					    var properties = '';
					    var g = results[i].geometry['location'];
					    for (var prop in g){
					        properties += g[prop];
					    }

						var loc = results[i]['geometry']['location'].toString();
						loc = loc.replace(/\(|\)|\s+/ig, '');
						loc = loc.split(',');	

						locations.push(['Bondi',loc[0],loc[1],i+1]);	

						frag+= template.replace( /{name}/ig, results[i].name)
										.replace( /{index}/ig, i+1)
										.replace( /{icon}/ig, results[i].icon)
										.replace( /{lat}/ig, loc[0])
										.replace( /{lng}/ig, loc[1])
										.replace( /{reference}/ig, results[i].id)
										.replace( /{location}/ig, results[i]['geometry']['location'])
										.replace( /{{formatted_address}}/ig, results[i].formatted_address)
										.replace( /{vicinity}/ig, (undefined == results[i].vicinity)?"":results[i].vicinity );
					}

 					that.setMarkers('yes', that.map, locations);					
					$(".js-result-list").append(frag);


				}


				 if (pagination.hasNextPage) {

				    var bx = $(".js-result-list-bx").find(".js-more-btn-bx");
					var btn = bx.find(".js-more-btn");
				    bx.displayBlock();

					   btn.on("click",function(){
							pagination.nextPage();
						}); 
				    
				 }

			}

		},
		//地図にマーカー設定
		setMarkers : function(isNumberPin, map, locations) {
		   	var that = this;

			  var image = new google.maps.MarkerImage('images/beachflag.png',
			      // This marker is 20 pixels wide by 32 pixels tall.
			      new google.maps.Size(20, 32),
			      // The origin for this image is 0,0.
			      new google.maps.Point(0,0),
			      // The anchor for this image is the base of the flagpole at 0,32.
			      new google.maps.Point(0, 32));
			  var shadow = new google.maps.MarkerImage('images/beachflag_shadow.png',
			      // The shadow image is larger in the horizontal dimension
			      // while the position and offset are the same as for the main image.
			      new google.maps.Size(37, 32),
			      new google.maps.Point(0,0),
			      new google.maps.Point(0, 32));
			      // Shapes define the clickable region of the icon.
			      // The type defines an HTML <area> element 'poly' which
			      // traces out a polygon as a series of X,Y points. The final
			      // coordinate closes the poly by connecting to the first
			      // coordinate.
			  var shape = {
			      coord: [1, 1, 1, 20, 18, 20, 18 , 1],
			      type: 'poly'
			  };
			  for (var i = 0; i < locations.length; i++) {

			    var beach = locations[i];
			    var myLatLng = new google.maps.LatLng(beach[1], beach[2]);
			    var marker = new google.maps.Marker({
			        position: myLatLng,
			        map: map,
			        //shadow: shadow, //好きな画像をセット
			        icon: isNumberPin ? new google.maps.MarkerImage("http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld="+ (i + 1) + "|ff7e73|000000") : null,
			        shape: shape,
			        title: beach[0],
			        zIndex: beach[3]
			    });
			   
			    that._markersArray.push(marker);
			  
			  }
		 
		},


		//地図のマーカー削除
		crearMarker : function (){
		    
		   	var that = this;

		    if(that._markersArray == null) return;
		    
			for (var i = 0; i < that._markersArray.length; i++) {
		    	that._markersArray[i].setMap(null); 
		  	}
		    //that._markersArray = null;
		},

		//詳細住所取得
		geocoder: function(that){

			var lat =that.find('.js-lat').val();
			var lng =that.find('.js-lng').val();


			//ジオコードオブジェクト
			var geocoder = new google.maps.Geocoder();
			geocoder.geocode(
			  {
			    'latLng': '(' + lat+','+lng + ')'
			  },
			  function(results, status){
			    if(status==google.maps.GeocoderStatus.OK){
			    	//処理
			    	alert(results);
			    }
			  }
			);

		},
		//ジオコーディング
		geocoding: function(address){

			var that = this;
            // 東京タワーをジオコーディング 
            var request = { 
                address: address
            }; 
 
            var geocoder = new google.maps.Geocoder(); 
            geocoder.geocode(request, function(results, status) { 
                // ステータスがOKならマーカーを表示する。 
                if (status == google.maps.GeocoderStatus.OK) { 
                	//alert(results[0].geometry.location);
                	that.get_map(results[0].geometry.location);
                    // var marker = new google.maps.Marker({ 
                    //     position: results[0].geometry.location, 
                    //     title: request.address, 
                    //     map: mapObj 
                    // }); 
                } 
           }); 
 
		},
		//地図の範囲変更
		//TODO
		change_area: function(){

			var that = this;
			google.maps.event.addListener(that.map, 'drag', dispLatLng);
			//google.maps.event.addListener(that.map, "zoom_changed", dispLatLng);

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

			}
		},
		//選択したリストを投稿画面に表示
		_dsp_place_info: function(that) {
			$('.js-select-place-bx').toggleClass("disp_block disp_none");
			that.removeClass("arrow").find(".js-result-list-main").prepend('<i class="fa fa-times-circle-o fa-size-s floRight"></i>');
			$('.js-select-place').html(that);

			//送信用変数にセット
			$(".js-subumit-lng").val(that.find('.js-lng').val());
			$(".js-subumit-lat").val(that.find('.js-lat').val());
			$(".js-subumit-reference").val(that.find('.js-reference').val());

		},
		//選択したリストを削除
		_set_default_zip: function(that) {

			$('.js-select-place-bx').toggleClass("disp_block disp_none");
			$('.js-select-place').html("");

			//送信用変数にセット
			$(".js-subumit-lng").val($("body").data("lng"));
			$(".js-subumit-lat").val($("body").data("lat"));
			$(".js-subumit-reference").val("");

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




