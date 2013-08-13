(function() {
	$("#generate").click( function(){
		subject = $("#subject").val().trim();
		$.get(
			"/_get_text",
			{ 'subject': subject }
		)
		.done( function(data) {
			if(subject.length > 0) {
				regex = new RegExp(subject, "g");
				data = data.replace(regex, "<strong>"+subject+"</strong>");	
			}
			$("#troll-text").html(data);
		});
		return false;
	});

}).call(this);
	
