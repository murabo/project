'use strict'

requirejs.config({

  shim: {
    jquery: {
      exports: "$"
    },
    underscore: {
      exports: "_"
    },
    backbone: {
      deps: ["jquery", "underscore"],
      exports: "Backbone"
    },
    Handlebars: {
      exports: 'Handlebars'
    }
  },
  onBuildWrite : function(moduleName, path, content){

        if (moduleName === 'Handlebars') {
            path = path.replace('handlebars.js','handlebars.runtime.js');
            content = fs.readFileSync(path).toString();
            content = content.replace(/(define\()(function)/, '$1"handlebars", $2');
        }
        return content;
  },

  paths: {
    jquery: './libs/jquery-1.8.2.min',
    underscore:'./libs/underscore-min',
    backbone: './libs/backbone-min',
    templates: '../templates',
    Handlebars: './libs/handlebars',
    text:'./libs/text',
    hbars:'./libs/hbars'
  }

});


require([
  "userView",
  "btnView"
], function( UserView, BtnShowView) {

    var userView = new UserView();
    var btnShowView = new BtnShowView({userView: userView});

});