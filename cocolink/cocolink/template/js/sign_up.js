$(function() {

	var vali = new Validate(),
	$error = $(".js-error"),
	$username = $("#js-user-name"),
	$password = $("#js-password"),
	$con_password = $("#js-con-password"),
	$nick_name = $("#js-nick-name"),
	$email = $("#js-email"),
	$form1 = $("#form1");


	//ログインボタン押下
	$(".js-submit").click(function(){


		var chk_cnt = 5;
		$error.html("");

		if(!vali.count($username,6,16,err_txt['txt1'])) chk_cnt--;
		if(!vali.count($nick_name,1,10,err_txt['txt2'])) chk_cnt--;
		if(!vali.count($password,6,16,err_txt['txt1'])) chk_cnt--;
		if(!vali.email($email,err_txt['txt4'])) chk_cnt--;
		if(!vali.matchStr($password,$con_password,err_txt['txt3'])) chk_cnt--;

 		if(chk_cnt == 0) $form1.submit();

	});


});