(function() {
	$("#generate").click( function(){
		subject = $("#subject").val()
		$.get(
			"/_get_text",
			{ 'subject': subject }
		)
		.done( function(data) {
			regex = new RegExp(subject, "g");
			data = data.replace(regex, "<strong>"+subject+"</strong>")	
			$("#troll-text").html(data);
		});
		return false;
	});

}).call(this);
	
