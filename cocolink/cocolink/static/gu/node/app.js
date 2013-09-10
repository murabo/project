var http = require("http");
//var socketio = require("socket.io");
var fs = require("fs");

var sys = require ('sys'),
url = require('url'),
http = require('http'),
qs = require('querystring');

// mysql接続
var mysql = require('mysql');
var TABLE = 'gu_gupost',
	TABLE2 = 'myuser';
//mysqlクライアント作成
var client = mysql.createConnection({
  user: 'root',
  password: 'mrk31229',
  database: 'cocolink'
});
 

var server = http.createServer(function(req, res) {
    
    console.log('Request received');

    res.writeHead(200, { 
        'Content-Type': 'html/text',
        'Access-Control-Allow-Origin': '*' // implementation of CORS
    });

    var body='';
    req.on('data', function (data) {
        body +=data;
    });

    if(req.method=='POST') {

      req.on('end', function　(chunk) {
        var prm =  qs.parse(body);
        set(prm.message);
        console.log(prm.message);
      });

    }else{

  
        var prm = url.parse(req.url,true);
        console.log(prm.query.offset);
        var where = "";
        if(undefined != prm.query.offset) where = ' WHERE '+ TABLE +.'ID < '+ prm.query.offset;
        console.log(prm.message);
        //データの検索
        client.query(
         'select '+TABLE2 +'.username,'+ TABLE +'.body_text,'+ TABLE +'.created_at from ' + TABLE +' LEFT JOIN '+  TABLE2 + where +' ORDER BY '+ TABLE +'.ID DESC LIMIT 3 ;',
   
          function (err, result, field) {
            if (err) {
              throw err;
            }
            
            if (!err) {
              var json = JSON.stringify(result);
              res.end(json);
            }
          }
        );

    }

  
}).listen(process.env.VMC_APP_PORT || 3000);


function set (argument) {
  //テストデータ作成
  client.query(
    'INSERT INTO '+ TABLE +' '+
    '(user_id,body_text,created_at) '+ 'values("1","'+ argument +'","1998-02-02")',
    function(err, info) { 
      if (err) {
        throw err;
      }
    }
  );
}


// var io = socketio.listen(server);

// io.sockets.on("connection", function (socket) {

//   // メッセージ送信（送信者にも送られる）
//   socket.on("C_to_S_message", function (data) {
//     io.sockets.emit("S_to_C_message", {value:data.value});
//   });

//   // ブロードキャスト（送信者以外の全員に送信）
//   socket.on("C_to_S_broadcast", function (data) {
//     socket.broadcast.emit("S_to_C_message", {value:data.value});
//   });

//   // 切断したときに送信
//   socket.on("disconnect", function () {
// //    io.sockets.emit("S_to_C_message", {value:"user disconnected"});
//   });
// });


