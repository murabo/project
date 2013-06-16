$(function() {

	var vali = new Validate(),
	$error = $(".js-error");
	err_txt1 = "6〜16文字で入力してください。",
	err_txt2 = "1〜10文字で入力してください。",
	$username = $("#js-user-name"),
	$password = $("#js-password"),
	$nick_name = $("#js-nick-name"),
	$form1 = $("#form1");


	//ログインボタン押下
	$(".js-submit").click(function(){

		var chk_cnt = 3;
		$error.html("");

		if(!vali.count($username,6,16,err_txt1)) chk_cnt--;
		if(!vali.count($password,6,16,err_txt1)) chk_cnt--;
		if(!vali.count($nick_name,1,10,err_txt2)) chk_cnt--;

 		if(chk_cnt == 0) $form1.submit();

	});


});