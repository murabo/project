$(function() {

	var vali = new Validate(),
	$error = $(".js-error"),
	$nick_name = $("#js-nick-name"),
	$email = $("#js-email"),
	$form1 = $("#form1");


	//ログインボタン押下
	$(".js-submit").click(function(e){

		e.preventDefault();
		var chk_cnt = 2;
		$error.html("");

		if(!vali.count($nick_name,1,10,err_txt['txt2'])) chk_cnt--;
		if(!vali.email($email,err_txt['txt4'])) chk_cnt--;
 		if(chk_cnt == 0) $form1.submit();

	});


});