import nfldb
# import pgpubsub
from django.http import JsonResponse
from django.shortcuts import render
# from forms import WeekForm
from mainapp import WEEK_TYPE_MAP


# def game(request, gsis):
#     db = nfldb.connect()
#     q = nfldb.Query(db)

#     q.game(gsis_id=gsis)
#     game = q.as_games()

#     return render(request, 'game.html', {'game': game[0]})


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
    # return get_games_for_week(request)
    return render(request, 'base.html')


# def get_games_for_week(request,
#                        year=CURRENT_YEAR,
#                        week_type=CURRENT_WEEK_TYPE,
#                        week_num=CURRENT_WEEK):
    # db = nfldb.connect()
    # q = nfldb.Query(db)

    # if week_type == 'post' and week_num in ['4', '5']:
    #     # Super bowl is either week 4 or 5 based on year
    #     q.game(season_year=year,
    #            season_type=WEEK_TYPE_MAP[week_type],
    #            week=[4, 5])
    # else:
    #     q.game(season_year=year,
    #            season_type=WEEK_TYPE_MAP[week_type],
    #            week=week_num)
    # q.sort(('start_time', 'asc'))
    # games = q.as_games()

    # week_form = WeekForm(
    #     initial={
    #         'week': week_num,
    #         'week_type': week_type,
    #         'year': year
    #     },
    #     year_val=year,
    #     week_type_val=week_type
    # )

    # teams = nfldb.types.Team.all_teams(db)

    # return render(request,
    #               'base.html',
    #               {
    #                   'games': games,
    #                   'teams': teams,
    #                   'weekForm': week_form,
    #                   'weekNum': week_num
    #               })


def games(request):
    """
    Return the Game objects as JSON for the given NFL week.
    Expected request parameters:
        `year` - The year of the games to return
        `weekType` - Either `pre`(season), `reg`(ular season), or
            `post`(season)
        `week` - The number of the week within the context of the given year
            and week type
    """
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
        game = {"gsisId": g.gsis_id,
                "awayTeam": g.away_team,
                "awayScore": g.away_score,
                "homeTeam": g.home_team,
                "homeScore": g.home_score,
                "dayOfWeek": str(g.day_of_week),
                "startYear": g.start_time.year,
                "startMonth": g.start_time.month,
                "startMonthName": g.start_time.strftime("%B"),
                "startDate": g.start_time.day,
                "startHour": g.start_time.strftime("%I").lstrip("0")
                             .replace(" 0", " "),
                "startMinute": g.start_time.strftime("%M"),
                "startAmPm": g.start_time.strftime("%p"),
                "timeZone": g.start_time.strftime("%Z"),
                "finished": g.finished,
                "isPlaying": g.is_playing}
        gamesJSON.append(game)

    return JsonResponse(gamesJSON, safe=False)
