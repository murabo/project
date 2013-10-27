
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
				$("#js-result-list").html('');
				that.crearMarker();
				that.get_place_list();
			});

			//現在地に戻る
			$(".js-current").click(function(){
				$("#js-result-list").html('');
				that.crearMarker();
				that.get_map();
			});

			//入力した住所へ地図移動
			$(".js-geocoding").click(function(){
				that.geocoding($("#js-geocoding-input").val());
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
				//that.change_area();
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

			//TODO キーワード検索が上手くいってないよー！！！！	
 			 var request = {
			    location: pyrmont,
			    radius: '500',
			    types: types,
			    //query : $('#js-query').val()//
			    query: 'restaurant'
			  };

			var service = new google.maps.places.PlacesService(that.map);
			service.search(request, createList);

			function createList(results, status){

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
						loc = loc.replace(/\(|\)/ig, '');
						loc = loc.split(',');	

						locations.push(['Bondi',loc[0],loc[1],i+1]);	

						frag+= template.replace( /{name}/ig, results[i].name)
										.replace( /{index}/ig, i+1)
										.replace( /{icon}/ig, results[i].icon)
										.replace( /{lat}/ig, loc[0])
										.replace( /{lng}/ig, loc[1])
										.replace( /{id}/ig, results[i].id)
										.replace( /{location}/ig, results[i]['geometry']['location'])
										.replace( /{{formatted_address}}/ig, results[i].formatted_address)
										.replace( /{vicinity}/ig, (undefined == results[i].vicinity)?"":results[i].vicinity );
					}

 					that.setMarkers('yes', that.map, locations);					
					$("#js-result-list").append(frag);


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
		}
		,
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




