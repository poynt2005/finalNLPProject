$(document).ready(function(){
  'use strict';

  new WOW().init();

  //bind enter key to click
  $("#inputStr").keydown(function(event){
    if(event.which == 13)
      $("#btn-clicked").click();
  });

  //check input string
  $("#btn-clicked").click(function(){
    var inputStrValue = $("#inputStr").val();
    var inputAccuracy = parseInt($("#inputAccuracy").val());

    var queryAccuracy = 50;

    if(!isNaN(inputAccuracy))
      if(inputAccuracy)
        queryAccuracy = inputAccuracy;
    else
      $("#inputAccuracy").val("");

    if(!inputStrValue){
      alert("請輸入拼音!!");
      $("#inputStr").focus();
    }
    else if((function(){
      var mandarinTest = new RegExp("[\u4e00-\u9fa5]");
      return mandarinTest.test(inputStrValue);})()){
        alert("不允許中文，請重新輸入拼音!!");
        $("#inputStr").val("");
        $("#inputStr").focus();
    }
    else
      sentQuery(inputStrValue.toLowerCase() , queryAccuracy);

  });



  //show jquery ui dialog
  function showdialog(dataObj , strError){
		let result = new String("");

    if(!strError)
      for(let i = 0 ; i < dataObj.length ; i++){
        if(i >= 15) break;
        for(let j in dataObj[i])
          result = result + ("可能的句子情況有 : " + j + "，機率為 : " + dataObj[i][j] + "<br>");
      }
    else{
      result = "結果錯誤 : 拼音錯誤或是資料庫無該拼音，請重新輸入";
      $("#inputStr").val("");
      $("#inputStr").focus();
    }

		$("#result_string").html(result);

		var dialogWidth = $(window).width() > 800 ? 800 : 'auto';

		$(function(){
			$( "#dialog" ).dialog({
				width: dialogWidth,
        /*buttons:[{
                    text : "關閉視窗",
                    class : "btn btn-danger dialogCloseBtn",
                    click : function(){
                      $( "#dialog" ).dialog("close");
                    }
                }],*/
				show:{
					effect: "puff",
					duration: 600
					},
				hide:{
					effect: "explode",
					duration: 600
				}
			});
		});
	};

  //ajax call server
  function sentQuery(inputStr , queryAccuracy){

      //spinner
      var opts = {
          lines: 13 // The number of lines to draw
        , length: 28 // The length of each line
        , width: 14 // The line thickness
        , radius: 42 // The radius of the inner circle
        , scale: 1 // Scales overall size of the spinner
        , corners: 1 // Corner roundness (0..1)
        , color: '#000' // #rgb or #rrggbb or array of colors
        , opacity: 0.25 // Opacity of the lines
        , rotate: 0 // The rotation offset
        , direction: 1 // 1: clockwise, -1: counterclockwise
        , speed: 1 // Rounds per second
        , trail: 60 // Afterglow percentage
        , fps: 20 // Frames per second when using setTimeout() as a fallback for CSS
        , zIndex: 2e9 // The z-index (defaults to 2000000000)
        , className: 'spinner' // The CSS class to assign to the spinner
        , top: '50%' // Top position relative to parent
        , left: '50%' // Left position relative to parent
        , shadow: false // Whether to render a shadow
        , hwaccel: false // Whether to use hardware acceleration
        , position: 'absolute' // Element positioning
      };
      //spinner target
      var spinner = new Spinner(opts);
      var target = $(".main-content").get(0);



    $.ajax({
      url : "/getQuery",
      type : "POST",
      data  : { 'param' : inputStr,
                'accuracyNum' : queryAccuracy
              },

      beforeSend : function(mes){
        spinner.spin(target);
      },

      success : function(res){

        spinner.spin();

        var resultError = (function(){
          return (res === "error");
        })();
        showdialog(res , resultError);
      },

      error : function(err){
		spinner.spin();
        console.log(err);
      }
    });
  }
});
