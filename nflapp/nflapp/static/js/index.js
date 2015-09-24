/*
 * Update views and dependent lists when changing year/season/week via AJAX
 */
$("#yearSelector").change(function() {
	$.ajax({
		url: '/week/' + this.value + '/' + $('#weekTypeSelector').val() + '/' + $('#weekSelector').val(),
		type: 'GET',

		// handle a successful response
		success: function(html) {
			// update html
			document.open();
			document.write(html);
			document.close();

			// update URL and browser history


			// reposition game viewlets
			setTimeout(positionViewlets, 1);
		},

		// handle a non-successful response
		// error: function(xhr,errmsg,err) {
		// 	$('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
		// 		" <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
		// 	console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
		// }
	});
});

$("#weekTypeSelector").change(function() {
	window.location.href = '/week/' + $('#yearSelector').val() + '/' + this.value + '/1';
});

$("#weekSelector").change(function() {
	window.location.href = '/week/' + $('#yearSelector').val() + '/' + $('#weekTypeSelector').val() + '/' + this.value;
});

/*
 * Evenly space gameViewlets on window load and resize
 */
function positionViewlets() {
	var completedGamesWidth = $('#completedGames').innerWidth();
	var viewletWidth = $('game-viewlet > paper-button').outerWidth();
	var numViewletsPerRow = Math.floor(completedGamesWidth / viewletWidth);
	var numCompletedGames = $('#completedGames game-viewlet').length;

	var marginVal, spaceVal;
	if (numViewletsPerRow < numCompletedGames) {
		spaceVal = completedGamesWidth % viewletWidth;
		marginVal = Math.floor(spaceVal / numViewletsPerRow / 2);
	} else {
		spaceVal = completedGamesWidth - numCompletedGames*viewletWidth;
		marginVal = Math.floor(spaceVal / numCompletedGames / 2);
	}

	$('game-viewlet').css('margin-left', marginVal);
	$('game-viewlet').css('margin-right', marginVal);
}

$(document).ready(function() {
	$(window).resize(positionViewlets).resize();
});