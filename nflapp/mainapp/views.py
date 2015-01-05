from django.shortcuts import render
import nfldb

CURRENT_WEEK = 17


def index(request):
    db = nfldb.connect()
    q = nfldb.Query(db)

    q.game(season_year=2014,
           season_type='Regular',
           week=CURRENT_WEEK)
    q.sort(('start_time', 'asc'))
    games = q.as_games()

    return render(request,
                  'index.html',
                  {
                      'games': games,
                      'weekNum': CURRENT_WEEK
                  })


def game(request, gsis):
    db = nfldb.connect()
    q = nfldb.Query(db)

    q.game(gsis_id=gsis)
    game = q.as_games()

    return render(request, 'game.html', {'game': game[0]})
