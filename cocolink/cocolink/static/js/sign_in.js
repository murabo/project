$(function() {

	var vali = new Validate(),
	$error = $(".js-error");
	err_txt = "8〜16文字で入力してください。",
	$username = $("#js-user-name"),
	$password = $("#js-password"),
	$form1 = $("#form1");


	//ログインボタン押下
	$(".js-submit").click(function(){

		var chk_cnt = 2;
		$error.html("");
		
		if(!vali.count($username,8,16,err_txt)) chk_cnt--;
		if(!vali.count($password,8,16,err_txt)) chk_cnt--;

 		if(chk_cnt == 0) $form1.submit();

	});


});



