import os
from os import environ

import dj_database_url
from boto.mturk import qualification

import decimal

import otree.settings



BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the environment variable OTREE_PRODUCTION controls whether Django runs in
# DEBUG mode. If OTREE_PRODUCTION==1, then DEBUG=False
if environ.get('OTREE_PRODUCTION') not in {None, '', '0'}:
    DEBUG = False
else:
    DEBUG = True


# don't share this with anybody.
SECRET_KEY = '+q02kxs2*)m+@0#9j*qo%pkpl=2_!hl%$&jdwzqb&746(soy8z'

# To use a database other than sqlite,
# set the DATABASE_URL environment variable.
# Examples:
# postgres://USER:PASSWORD@HOST:PORT/NAME
# mysql://USER:PASSWORD@HOST:PORT/NAME

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    )
}



# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

# for flexibility, you can set it in the environment variable OTREE_AUTH_LEVEL
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# setting for integration with AWS Mturk
AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')


# e.g. EUR, CAD, GBP, CHF, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'AED '
USE_POINTS = True


# e.g. en, de, fr, it, ja, zh-hans
# see: https://docs.djangoproject.com/en/1.9/topics/i18n/#term-language-code
LANGUAGE_CODE = 'en'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

# SENTRY_DSN = ''

DEMO_PAGE_INTRO_TEXT = """
<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            oTree on GitHub
        </a>.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            oTree homepage
        </a>.
    </li>
</ul>
<p>
    Here are various games implemented with oTree.
</p>
"""

ROOMS = [
    # {
    #     'name': 'econ101',
    #     'display_name': 'Econ 101 class',
    #     'participant_label_file': '_rooms/econ101.txt',
    # },
    # {
    #     'name': 'live_demo',
    #     'display_name': 'Room for live demo (no participant labels)',
    # },
    {
        'name': 'ssel_b_side',
        'display_name': 'SSEL Desktops B01 - B24',
        'participant_label_file': '_rooms/ssel_b_side.txt',
    },
]
 

# from here on are qualifications requirements for workers
# see description for requirements on Amazon Mechanical Turk website:
# http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_QualificationRequirementDataStructureArticle.html
# and also in docs for boto:
# https://boto.readthedocs.org/en/latest/ref/mturk.html?highlight=mturk#module-boto.mturk.qualification

mturk_hit_settings = {
    'keywords': ['easy', 'bonus', 'choice', 'study'],
    'title': 'Title for your experiment',
    'description': 'Description for your experiment',
    'frame_height': 500,
    'preview_template': 'global/MTurkPreview.html',
    'minutes_allotted_per_assignment': 60,
    'expiration_hours': 7*24, # 7 days
    #'grant_qualification_id': 'YOUR_QUALIFICATION_ID_HERE',# to prevent retakes
    'qualification_requirements': [
        # qualification.LocaleRequirement("EqualTo", "US"),
        # qualification.PercentAssignmentsApprovedRequirement("GreaterThanOrEqualTo", 50),
        # qualification.NumberHitsApprovedRequirement("GreaterThanOrEqualTo", 5),
        # qualification.Requirement('YOUR_QUALIFICATION_ID_HERE', 'DoesNotExist')
    ]
}


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = {

    'real_world_currency_per_point': 1.0,
    'participation_fee': 30.0,
    'doc': "CSR Testing",
    'mturk_hit_settings': mturk_hit_settings,
}

SESSION_CONFIGS = [



    {
        'name': 'csr_cp',
        'display_name': "CSR ❄️🌯 - Intructions, RET, VCM (Cold Prickle ❄🌯️), Stage, Payment",
        'num_demo_participants': 4,
        'app_sequence': [
            'csr_0_realeffort','csr_1_quiz_coldPrickle','csr_2_vcm_coldPrickle','csr_3_stageT',
        ],
        'real_world_currency_per_point': 1.0,
        'ret_time': 300,
        'vcm_round_count': 10,
        'participation_fee': 30.0,
        'final_score_discounter':0.25,
    },
    {
        'name': 'csr_wg',
        'display_name': "CSR ☀🌅 - Intructions, RET, VCM (Warm Glow ☀🌅), Stage, Payment",
        'num_demo_participants': 4,
        'app_sequence': [
            'csr_0_realeffort','csr_1_quiz_warmGlow','csr_2_vcm_warmGlow','csr_3_stageT',
        ],
        'real_world_currency_per_point': 1.0,
        'ret_time': 300,
        'vcm_round_count': 10,
        'participation_fee': 30.0,
        'final_score_discounter':0.25,
    },


    
    {
        'name': 'csr_0_realeffort',
        'display_name': "CSR: Just Real Effort",
        'num_demo_participants': 4,
        'app_sequence': [
            'csr_0_realeffort',
        ],
        'ret_time': 180,
    },
    {
        'name': 'csr_1_quiz_cp',
        'display_name': "CSR: Just ❄️🌯-VCM Quiz",
        'num_demo_participants': 4,
        'app_sequence': [
            'csr_1_quiz_coldPrickle',
        ],
    },
    {
        'name': 'csr_1_quiz_wg',
        'display_name': "CSR: Just ☀🌅-VCM Quiz",
        'num_demo_participants': 4,
        'app_sequence': [
            'csr_1_quiz_warmGlow',
        ],
    },
    {
        'name': 'csr_vcmstage_cp',
        'display_name': "Just CSR ❄🌯️ VCM: ❄️🌯-VCM (2Rounds/short) -> Stage -> Payment",
        'num_demo_participants': 4,
        'app_sequence': [
        'csr_2_vcm_coldPrickle','csr_3_stageT',
        ],
        'real_world_currency_per_point': 0.01,
        'ret_time': 180,
        'vcm_round_count': 2,
    },
    {
        'name': 'csr_vcmstage_wp',
        'display_name': "Just CSR ☀🌅 VCM: ☀🌅-VCM (2Rounds/short) -> Stage -> Payment",
        'num_demo_participants': 4,
        'app_sequence': [
        'csr_2_vcm_warmGlow','csr_3_stageT',
        ],
        'real_world_currency_per_point': 0.01,
        'ret_time': 180,
        'vcm_round_count': 5,
    },
    # {
    #     'name': 'csr_3_stageQuiz',
    #     'display_name': "CSR: Just Stage Game Quiz",
    #     'num_demo_participants': 4,
    #     'app_sequence': [
    #         'csr_3_stageQuiz',
    #     ],
    # },



    {
        'name': 'public_goods',
        'display_name': "Demo - Public Goods",
        'num_demo_participants': 3,
        'app_sequence': ['public_goods', 'payment_info'],
    },
    {
        'name': 'trust',
        'display_name': "Demo - Trust Game",
        'num_demo_participants': 2,
        'app_sequence': ['trust', 'payment_info'],
    },
    {
        'name': 'guess_two_thirds',
        'display_name': "Demo - Guess 2/3 of the Average",
        'num_demo_participants': 3,
        'app_sequence': ['guess_two_thirds', 'payment_info'],
    },
    {
        'name': 'survey',
        'display_name': "Demo - Survey",
        'num_demo_participants': 1,
        'app_sequence': ['survey', 'payment_info'],
    },
    {
        'name': 'quiz',
        'display_name': "Demo - Quiz",
        'num_demo_participants': 1,
        'app_sequence': ['quiz'],
    },
    {
        'name': 'prisoner',
        'display_name': "Demo - Prisoner's Dilemma",
        'num_demo_participants': 2,
        'app_sequence': ['prisoner', 'payment_info'],
    },
    {
        'name': 'ultimatum',
        'display_name': "Demo - Ultimatum (randomized: strategy vs. direct response)",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum', 'payment_info'],
    },
    {
        'name': 'ultimatum_strategy',
        'display_name': "Demo - Ultimatum (strategy method treatment)",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum', 'payment_info'],
        'treatment': 'strategy',
    },
    {
        'name': 'ultimatum_non_strategy',
        'display_name': "Demo - Ultimatum (direct response treatment)",
        'num_demo_participants': 2,
        'app_sequence': ['ultimatum', 'payment_info'],
        'treatment': 'direct_response',
    },
    {
        'name': 'vickrey_auction',
        'display_name': "Demo - Vickrey Auction",
        'num_demo_participants': 3,
        'app_sequence': ['vickrey_auction', 'payment_info'],
    },
    {
        'name': 'volunteer_dilemma',
        'display_name': "Demo - Volunteer's Dilemma",
        'num_demo_participants': 3,
        'app_sequence': ['volunteer_dilemma', 'payment_info'],
    },
    {
        'name': 'cournot',
        'display_name': "Demo - Cournot Competition",
        'num_demo_participants': 2,
        'app_sequence': [
            'cournot', 'payment_info'
        ],
    },
    {
        'name': 'principal_agent',
        'display_name': "Demo - Principal Agent",
        'num_demo_participants': 2,
        'app_sequence': ['principal_agent', 'payment_info'],
    },
    {
        'name': 'dictator',
        'display_name': "Demo - Dictator Game",
        'num_demo_participants': 2,
        'app_sequence': ['dictator', 'payment_info'],
    },
    {
        'name': 'matching_pennies',
        'display_name': "Demo - Matching Pennies",
        'num_demo_participants': 2,
        'app_sequence': [
            'matching_pennies',
        ],
    },
    {
        'name': 'traveler_dilemma',
        'display_name': "Demo - Traveler's Dilemma",
        'num_demo_participants': 2,
        'app_sequence': ['traveler_dilemma', 'payment_info'],
    },
    {
        'name': 'bargaining',
        'display_name': "Demo - Bargaining Game",
        'num_demo_participants': 2,
        'app_sequence': ['bargaining', 'payment_info'],
    },
    {
        'name': 'common_value_auction',
        'display_name': "Demo - Common Value Auction",
        'num_demo_participants': 3,
        'app_sequence': ['common_value_auction', 'payment_info'],
    },
    {
        'name': 'stackelberg',
        'display_name': "Demo - Stackelberg Competition",
        'real_world_currency_per_point': 0.01,
        'num_demo_participants': 2,
        'app_sequence': [
            'stackelberg', 'payment_info'
        ],
    },
    {
        'name': 'bertrand',
        'display_name': "Demo - Bertrand Competition",
        'num_demo_participants': 2,
        'app_sequence': [
            'bertrand', 'payment_info'
        ],
    },
    {
        'name': 'real_effort',
        'display_name': "Demo - Real-effort transcription task",
        'num_demo_participants': 1,
        'app_sequence': [
            'real_effort',
        ],
    },
    {
        'name': 'lemon_market',
        'display_name': "Demo - Lemon Market Game",
        'num_demo_participants': 3,
        'app_sequence': [
            'lemon_market', 'payment_info'
        ],
    },
    {
        'name': 'battle_of_the_sexes',
        'display_name': "Demo - Battle of the Sexes",
        'num_demo_participants': 2,
        'app_sequence': [
            'battle_of_the_sexes', 'payment_info'
        ],
    },
    {
        'name': 'public_goods_simple',
        'display_name': "Demo - Public Goods (simple version from tutorial)",
        'num_demo_participants': 3,
        'app_sequence': ['public_goods_simple', 'survey', 'payment_info'],
    },
    {
        'name': 'trust_simple',
        'display_name': "Demo - Trust Game (simple version from tutorial)",
        'num_demo_participants': 2,
        'app_sequence': ['trust_simple'],
    },

]

# anything you put after the below line will override
# oTree's default settings. Use with caution.
otree.settings.augment_settings(globals())
