var Get = Backbone.Collection.extend({
	url : null,
	model : null,
	initialize: function(data) { 
		this.url = data.url;
    	this.model = data.model;
	},
	parse : function(resp) {
		if (resp.error) {
            alert(resp.error.message);
        }
        return resp;
    }
});
