(function ($, document, window) {

	$(document).ready(function () {
		//Prompt geolocation 
		$(window).load(function () {
			if (navigator.geolocation)
				navigator.geolocation.getCurrentPosition(function (position) {
					console.log(position);
					$.ajax({
						url: "http://api.openweathermap.org/data/2.5/weather?lat=" + position.coords.latitude + "&lon=" + position.coords.longitude + "&mode=html&appid=a35445183178ae9855606a62f31eba44",
						type: 'GET',
						beforeSend: function (xhr) {
							$(".today").html("<div><span class='fa fa-spinner'></span> Loading</div>")
						},
						dataType: 'html', // added data type
						success: function (res) {
							var body = res.replace(/^.*?<body>(.*?)<\/body>.*?$/s, "$1");
							var htmlObject = document.createElement('div');
							htmlObject.style.margin = "5px";
							htmlObject.innerHTML = body;
							var divs = htmlObject.getElementsByTagName("div");
							for (var i = 0; i < divs.length; i++) {
								if (divs[i].hasAttribute("title")) {
									divs[i].style.fontSize = "20pt"
									divs[i].style.width = "100px"
								} else {
									divs[i].style.fontSize = "10pt"
								}
								divs[i].style.width = "100%"
								divs[i].style.textAlign = "center"
							}
							console.log(divs)
							$(".today").html(htmlObject)
						},
						error: function (request, status, error) {
							$(".today").html("<div>An error occured, please try again.</div>");
						}
					});
				})
			else
				$(".today").html("<div>Geolocation is not supported.</div>");
		});

		// Cloning main navigation for mobile menu
		$(".mobile-navigation").append($(".main-navigation .menu").clone());

		// Mobile menu toggle 
		$(".menu-toggle").click(function () {
			$(".mobile-navigation").slideToggle();
		});

		var map = $(".map");
		var latitude = map.data("latitude");
		var longitude = map.data("longitude");
		if (map.length) {

			map.gmap3({
				map: {
					options: {
						center: [latitude, longitude],
						zoom: 15,
						scrollwheel: false
					}
				},
				marker: {
					latLng: [latitude, longitude],
				}
			});

		}
	});

	$(window).load(function () {

	});

})(jQuery, document, window);