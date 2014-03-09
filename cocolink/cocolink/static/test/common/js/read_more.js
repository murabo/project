// 非同期通信による次頁情報取得関数
function getNext()
{	
	try{
		jQuery.noConflict();
	}
	catch( e ){
	}
	
	// GETパラメータ取得
	var qsParm = new Array();
	var query = window.location.search.substring(1);
	var parms = query.split('&');
	for (var i=0; i<parms.length; i++) {
		var pos = parms[i].indexOf('=');
		if (pos > 0) {
			var key = parms[i].substring(0,pos);
			var val = parms[i].substring(pos+1);
			qsParm[key] = val;
		}
	}

	// 通信先のURL指定
	var url = './read_more.php';
	var placeHolder = 'pagination';

	// 通信中は、ロード画像を表示し、「もっと読む」ボタンを非表示にする
	$('ajaxbutton').style.display = 'none';
	$('div1').style.display = 'block';
	var rotateTimer = window.setTimeout(rotate, 2);	//画像回転開始

	// Updater でプレースホルダ部分を取得情報と置換
	var myAjax = new Ajax.Request(
		url ,
		{
			method: 'get',
			parameters: 'CATEGORY='+qsParm['CATEGORY'] + '&' + 'SUBCATEGORY='+qsParm['SUBCATEGORY'] + '&' + 'DATATYPE='+qsParm['DATATYPE'] + '&' + 'NOT_TOPPAGE='+qsParm['NOT_TOPPAGE'] + '&' + 'TOPICS_CODE='+qsParm['TOPICS_CODE'] + '&' + 'TOPICS_TYPE='+qsParm['TOPICS_TYPE'] + '&' + 'PAGE_NO='+(parseInt(document.getElementById("PAGE_NO").value) + 1) + '&' + 'PageNo='+(parseInt(document.getElementById("PAGE_NO").value) + 1) + '&' + 'SearchType='+qsParm['SearchType'] + '&' + 'Type='+qsParm['Type'] + '&' + 'SearchCondition='+qsParm['SearchCondition'], 
			// 受信成功
			onSuccess: function( request ) {
				var elems = document.getElementById('pagination');
				new Insertion.Bottom(placeHolder, request.responseText);
				document.getElementById("PAGE_NO").value = parseInt(document.getElementById("PAGE_NO").value) + 1;
				
				ajaxSuccessHandler();
			},
		
			// 終了
			onComplete: function( request ) {
				// 非表示にしていたボタンを表示、ロード画像を非表示に設定
				clearTimeout( rotateTimer );	//画像回転終了
				var currentPageElement = document.getElementById("PAGE_NO");
				var lastPageElement = document.getElementById("LAST_PAGE_NO");
				if ( lastPageElement != null && currentPageElement != null ) {
					var currentPage = currentPageElement.value;
					var lastPageNo = lastPageElement.value;
					if ( (lastPageNo-1) > currentPage ) {
						$('ajaxbutton').style.display = 'block';
					}
				}else{
					$('ajaxbutton').style.display = 'block';
				}
				$('div1').style.display = 'none';
			},
		});
	
	// 正常終了
	return true;
}

// 非同期通信による次頁情報取得関数(急上昇ワード用)
function getNextForTrendWord()
{	
	try{
		jQuery.noConflict();
	}
	catch( e ){
	}
	
	// GETパラメータ取得
	var qsParm = new Array();
	var query = window.location.search.substring(1);
	var parms = query.split('&');
	for (var i=0; i<parms.length; i++) {
		var pos = parms[i].indexOf('=');
		if (pos > 0) {
			var key = parms[i].substring(0,pos);
			var val = parms[i].substring(pos+1);
			qsParm[key] = val;
		}
	}

	// 通信先のURL指定
	var url = './read_more.php';
	var placeHolder = 'pagination';

	// 通信中は、ロード画像を表示し、「もっと読む」ボタンを非表示にする
	$('ajaxbutton').style.display = 'none';
	$('div1').style.display = 'block';
	var rotateTimer = window.setTimeout(rotate, 2);	//画像回転開始

	// Updater でプレースホルダ部分を取得情報と置換
	var myAjax = new Ajax.Request(
		url ,
		{
			method: 'get',
			parameters: 'PAGE_NO='+String(PAGE_NO + 1) , 
			// 受信成功
			onSuccess: function( request ) {
				var elems = document.getElementById('pagination');
				new Insertion.Bottom(placeHolder, request.responseText);
				PAGE_NO += 1;
				
				ajaxSuccessHandler();
			},
		
			// 終了
			onComplete: function( request ) {
				// 非表示にしていたボタンを表示、ロード画像を非表示に設定
				clearTimeout( rotateTimer );	//画像回転終了
				if ( LAST_PAGE_NO != null && PAGE_NO != null ) {
					if ( (LAST_PAGE_NO-1) > PAGE_NO ) {
						$('ajaxbutton').style.display = 'block';
					}
				}else{
					$('ajaxbutton').style.display = 'block';
				}
				$('div1').style.display = 'none';
			},
		});
	
	// 正常終了
	return true;
}
