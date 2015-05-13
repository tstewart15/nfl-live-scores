/*
 * Update views and dependent lists when changing year/season/week
 */
$("#yearSelector").change(function() {
	window.location.href = '/week/' + this.value + '/' + $('#weekTypeSelector').val() + '/' + $('#weekSelector').val();
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
$(document).ready(function() {
	$(window).resize(function() {

		var completedGamesWidth = $('#completedGames').innerWidth();
		var viewletWidth = $('.gameViewlet').outerWidth();
		var numViewletsPerRow = Math.floor(completedGamesWidth / viewletWidth);
		var numCompletedGames = $('#completedGames .gameViewlet').length;

		var marginVal, spaceVal;
		if (numViewletsPerRow < numCompletedGames) {
			spaceVal = completedGamesWidth % viewletWidth;
			marginVal = Math.floor(spaceVal / numViewletsPerRow / 2);
		} else {
			spaceVal = completedGamesWidth - numCompletedGames*viewletWidth;
			marginVal = Math.floor(spaceVal / numCompletedGames / 2);
		}

		$('.gameViewlet').css('margin-left', marginVal);
		$('.gameViewlet').css('margin-right', marginVal);
		
	}).resize();
});