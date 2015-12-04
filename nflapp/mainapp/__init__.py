from collections import OrderedDict

"""
'mainapp' Package Constants
"""
FIRST_PRE_WEEK = 1
LAST_PRE_WEEK = 4

FIRST_REG_WEEK = 1
LAST_REG_WEEK = 17

FIRST_YEAR = 2009
LAST_YEAR = 2015

POSTSEASON_WEEK_LABELS = [
    'Wild Card',
    'Divisional Round',
    'Conference Championships',
    'Super Bowl'
]

WEEK_TYPE_MAP = OrderedDict([
    ('pre', 'Preseason'),
    ('reg', 'Regular'),
    ('post', 'Postseason')
])

POSTSEASON_WEEKS_FOR_YEAR = dict.fromkeys(
    map(str, range(FIRST_YEAR, LAST_YEAR+1)),
    zip(range(1, 5), POSTSEASON_WEEK_LABELS))

WEEKS_FOR_WEEK_TYPE = {
    'pre': dict.fromkeys(map(str, range(FIRST_YEAR, LAST_YEAR+1)),
                         [(x, 'Week ' + str(x))
                             for x in range(FIRST_PRE_WEEK, LAST_PRE_WEEK+1)]),
    'reg': dict.fromkeys(map(str, range(FIRST_YEAR, LAST_YEAR+1)),
                         [(x, 'Week ' + str(x))
                             for x in range(FIRST_REG_WEEK, LAST_REG_WEEK+1)]),
    'post': POSTSEASON_WEEKS_FOR_YEAR
}
