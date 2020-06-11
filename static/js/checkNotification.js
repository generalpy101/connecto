$(document).ready(()=>{
	var href = $('input[name=href]').val()
	function CheckNotification() {
		$.ajax({
			url: href,
			type: 'POST',
			data: {
				'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
			},
			success : data => {
				if(data.notification) {
					$('.notifier').css({
						"display": 'inline-block',
					});
				}
				else {
					$('.notifier').css({
						"display": 'none',
					});
				}
			}
		})
	}
	CheckNotification()
	setInterval(CheckNotification, 10000)
})