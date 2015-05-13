import nfldb
from django.shortcuts import render
from forms import WeekForm
from mainapp import WEEK_TYPE_MAP, LAST_YEAR

CURRENT_WEEK = 1
CURRENT_WEEK_TYPE = 'reg'
CURRENT_YEAR = LAST_YEAR


def game(request, gsis):
    db = nfldb.connect()
    q = nfldb.Query(db)

    q.game(gsis_id=gsis)
    game = q.as_games()

    return render(request, 'game.html', {'game': game[0]})


def index(request):
    return week_selection(request)


def week_selection(request,
                   year=CURRENT_YEAR,
                   week_type=CURRENT_WEEK_TYPE,
                   week_num=CURRENT_WEEK):
    db = nfldb.connect()
    q = nfldb.Query(db)

    if week_type == 'post' and week_num in ['4', '5']:
        # Super bowl is either week 4 or 5 based on year
        q.game(season_year=year,
               season_type=WEEK_TYPE_MAP[week_type],
               week=[4, 5])
    else:
        q.game(season_year=year,
               season_type=WEEK_TYPE_MAP[week_type],
               week=week_num)
    q.sort(('start_time', 'asc'))
    games = q.as_games()

    week_form = WeekForm(
        initial={
            'week': week_num,
            'week_type': week_type,
            'year': year
        },
        year_val=year,
        week_type_val=week_type
    )

    teams = nfldb.types.Team.all_teams(db)

    return render(request,
                  'index.html',
                  {
                      'games': games,
                      'teams': teams,
                      'weekForm': week_form,
                      'weekNum': week_num
                  })
