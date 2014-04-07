define([
  "jquery",
  "underscore",
  "backbone",
  "userModels",
  "userCollections",
  'hbars!templates/test'
], function($, _, Backbone,User,UserList,template) {

   // ユーザー一覧表示領域のビュー
    var UserView = Backbone.View.extend({
        el : '#user_list_body',
        model : User,
        collection : UserList,
        template : template,
        initialize : function(options) {
            _.bindAll(this, 'render');
            this.reset();
        },
        reset : function() {
            this.collection = new UserList();
        },
        render : function() {
            $(this.el).empty();
            this.collection.fetch({
                data : {
                    user_id : $('#user_id').val()
                },
                dataType : 'json',
                success : $.proxy(this.add, this)
            });
        },
        add : function(collection, resp) {
            var that = this;
            if (collection.length == 0) {
                //$(that.el).append(_.template($('#user_norow_template').html(), null));
                return;
            }
            collection.each(function(model) {
                
                $(that.el).append(template(model.attributes));

            });


        }
    });


    return UserView;

});