$(function(){



  // ユーザー情報を格納するモデル
    var User = Backbone.Model.extend({
        // 属性指定が無いインスタンス生成の際のデフォルト属性（本サンプルでは無くてもいい）
        defaults : function() {
            return {
                'data' : {
                    'create_datetime' : null,
                    'name' : null,
                    'message' : null
                }
            };
        }
    });

    // ユーザー情報モデルを複数格納するためのコレクション
    var UserList = Backbone.Collection.extend({
        // リソースから取得した結果を格納するモデル
        model : User,
        // モデルの内容取得先リソース
        url : api_path['timeline'],
        // リソースから取得した結果をモデルに格納する前に参照できる。
        // returnされた値のみがモデルに格納される
        parse : function(resp) {
            if (resp.error) {
                // エラーがあればエラーメッセージ表示
                alert(resp.error.message);
            }
            // モデルに格納するデータ部分を返す

            return resp.response.result.list;
        }
    });

    // ユーザー一覧表示領域のビュー
    var UserView = Backbone.View.extend({
        el : '#list',
        model : User,
        collection : UserList,
        initialize : function(options) {
            _.bindAll(this, 'render');
            this.reset();
        },
        reset : function() {
            this.collection = new UserList();
        },
        render : function() {

            // リソースから取得
            // （collectionのurlにGETリクエストを送信する）
            this.collection.fetch({
                data : {
                    user_id : "123"
                },
                dataType : 'json',
                success : $.proxy(this.add, this)
            });


        },
        add : function(collection, resp) {

            var that = this;
            if (collection.length == 0) {
            	alert("0件");
                return;
            }
            collection.each(function(model) {
                // コレクションに格納されたモデルの内容を1件ずつテンプレートに当てはめて表示
                $(that.el).append(_.template($('#user_row_template').html(), model.attributes));
            });
        },
        test2 : function(msg) {

            $("#msg_list").prepend("<div class='msg'>" + msg + "</div>");

        }
    });

    
    var BtnShowView = Backbone.View.extend({
        el : $('.js-btn_more'),
        userView : null,
        initialize : function(data) {
            this.userView = data.userView;
			//とりあえずココに！！！！！！！！
			$(document).post();//投稿
        },
        events: {
            // clickイベントの登録
            'click' : 'get_list'
        },
        get_list : function(e) {
            // ユーザー一覧を描画する
            this.userView.render();
        }
    });



    var userView = new UserView();
    var btnShowView = new BtnShowView({userView: userView});



});




