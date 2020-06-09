$(document).ready(()=>{
	$("#searcbar").on("submit", function (e) {
    	e.preventDefault();
		$.ajax({
			url: '/searchuser',
			type: 'POST',
			data: {query : $("#bar").val()}
		})
		.done(function(data) {
			$("#searhresults").empty()
			console.log(data.friends);
			for (var entry = data.users.length - 1; entry >= 0; entry--) {
				for (var friend = data.friends.length - 1; friend >= 0; friend--) {
					console.log(data.friends[friend].username)
					console.log(data.users[entry].username)
					if (data.friends[friend].username==data.users[entry].username) {
						console.log("True")
						html = `
						<div class="col-12 mt-3">
							<div class ="card">
								<div class="card-horizontal">
									<div id="circle" >
													
									</div>
									<div class="card-body">
										<h5 class="card-title">${data.users[entry].username}</h5>
										<a class="btn btn-outline-danger" href="#" style="float:right">Remove??
										<i class="fas fa-trash-alt"></i></a>
										<a href="/user/${data.users[entry].id}" class="btn btn-outline-success" style="float:right">
										Friend</a>
									</div>
								</div>
							</div>
						</div>`
						$("#searhresults").append(html)		
						continue					
						}
						else{
							console.log("False")
							html = `
							<div class="col-12 mt-3">
								<div class ="card">
									<div class="card-horizontal">
										<div id="circle" >
													
										</div>
										<div class="card-body">
											<h5 class="card-title">${data.users[entry].username}</h5>
											<a href="/user/${data.users[entry].id}" class="btn btn-outline-success" style="float:right">
											Add Friend</a>
										</div>
									</div>
								</div>
							</div>`
							$("#searhresults").append(html)	
							continue			
						}	
					}
				}
				
		})
		.fail(function() {
			console.log("error");
		})
	})
})