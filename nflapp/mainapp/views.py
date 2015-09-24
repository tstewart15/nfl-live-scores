import nfldb, json
from django.http import JsonResponse
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
    # week_form = WeekForm(
    #     initial={
    #         'week': CURRENT_WEEK,
    #         'week_type': CURRENT_WEEK_TYPE,
    #         'year': CURRENT_YEAR
    #     },
    #     year_val=CURRENT_YEAR,
    #     week_type_val=CURRENT_WEEK_TYPE
    # )

    # db = nfldb.connect()
    # teams = nfldb.types.Team.all_teams(db)

    # return render(request,
    #               'index.html',
    #               {
    #                   'games': games,
    #                   'teams': teams,
    #                   'weekForm': week_form,
    #                   'weekNum': week_num
    #               })
    return get_games_for_week(request)


def get_games_for_week(request,
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


def games(request):
    year = request.GET.get("year")
    week_type = request.GET.get("weekType")
    week_num = request.GET.get("week")
    print "Received request for " + year + " " + week_type + " " + week_num

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
    gamesJSON = []
    for g in games:
        game = {"gsis_id": g.gsis_id,
                "away_team": g.away_team,
                "away_score": g.away_score,
                "home_team": g.home_team,
                "home_score": g.home_score,
                "day_of_week": str(g.day_of_week),
                "start_month": g.start_time.month,
                "start_date": g.start_time.day,
                "start_hour": g.start_time.hour,
                "start_minute": g.start_time.minute}
        gamesJSON.append(game)

    return JsonResponse(gamesJSON, safe=False)
