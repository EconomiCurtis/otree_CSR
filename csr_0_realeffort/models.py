# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

# </standard imports>



author = 'Curtis Kephart'

doc = """
CSR Experiment
This experiment ...
Designed by Chetan Dave and Alicja Reuben.
First implementation by Curtis Kephart (curtiskephart@gmail.com) 2016.11
"""

class Constants(BaseConstants):
    name_in_url = 'csr_realEffort'
    players_per_group = 4
    task_timer = 30
    num_rounds = 200

    reference_texts = [
		'KJe783yzU3Ca',
		'l9veLG7stT3P',
		'CQH7uKzEgNk0',
		'Fx8l6AbsZuMs',
		'EmBMxrAy03J1',
		'bzu52aHa1Qoa',
		'hWIk3zeIQYy8',
		'p8Eyf9rExbfq',
		't1IVvlgzxnKF',
		'CzU4HQAWYsyD',
		'YxRhyujFASW3',
		'MwRTjhzaFAjn',
		'qf1YvFXH3Lu7',
		'3tFi2GNPRD3A',
		'uZo8XO7LYoFy',
		'yUTg6MDpXcvB',
		'sGR6IROq027U',
		'8X78WIlP8daO',
		'v0PIyCNNU4Vh',
		'MPETsO8yh691',
		'Xx7QPUJ0fY7D',
		'wI01DIlrefVL',
		'1KsvfrHBeYso',
		'T6F7j1ChPwYJ',
		'KUNmRKlwd0Yk',
		'erLnhgW0KcLp',
		'R70l5SQ8guz4',
		'UiVqjH6iKnHi',
		'hQmonmRjHlyC',
		'vWlnom8WkCaU',
		'Eic7OSdDmIOB',
		'ZLMxBdChnv52',
		'JVpSqHuMTa69',
		'hGFHrC2bVPG9',
		'1bNJUTehHf6S',
		'm9h4bjfqdg1D',
		'neC3YySwdy7l',
		'1YnebhoASSKZ',
		'C8fNpXHTOm0X',
		'JoXW7Ha1Rmbp',
		'3aBNO7u4ripj',
		'lRqeo2zqcR9V',
		'YiIO5UPBbfIK',
		'FtpBw4SniDsD',
		'UblqBTFPLJUW',
		'dsRkfSGPuvyX',
		'jGI5TtfhXrz6',
		'4QxBRzXwFeXu',
		'HPxA3xCa0sgz',
		'iweAsv967BBs',
		'JxpWBDWmDxAG',
		'pDRFDttDzN9q',
		'0V6gq54T9qga',
		'sgTI0yNShF85',
		'vexoIvPtncMq',
		'44CGXygnQ0NV',
		'TiRRxmNfUQRI',
		'6XPCx37lZCKD',
		'XqSTjDv6dqEb',
		'7x26HZCoTT0n',
		'2UzDrqnIA26e',
		'4AxNz3gAGrcl',
		'pPBFV8E69FCr',
		'HeOtzDJ7XpZD',
		'oWtEHrxktbpI',
		'lS9NKkvY7KnG',
		'xdUYWA8HDK7x',
		'9XxdV5SHikWu',
		'ZdO2e2HhM1Hx',
		'qvhgeNnGGJbP',
		'ZyPiIDJe7ZYg',
		'7NXE8SNHNYCu',
		'p4TZOCbrDlpz',
		'jvyc3wljT7jo',
		'cAO83uOjEIrN',
		'F8El8ueLBU5V',
		'ZAhtrzONppLG',
		'lSfbuzgH4QKQ',
		'DaoctzvTAvf7',
		'9A1xkOeNZhFb',
		'xxuUnAZxbsTa',
		'ZBG02ZyRjrPW',
		'yXnV2KQh5iAq',
		'ZyZEKfP4r3oR',
		'hOydsUgtp6gG',
		'wJ7cEYeXkgSD',
		'Cpi7S6ttweoZ',
		'6CUq5kpZS9Ri',
		'rwWqmGlCrhxd',
		'RXd8MyGKe53S',
		'GQExSI5n3j1u',
		'l8YiQUCblTeY',
		'pLfZ1ggYdf9h',
		'ddVAVbf1tyQm',
		'0B8TP5IVzXxO',
		'6qYU3iEGUrci',
		'Te1Ne2s1gNrv',
		'RAAXuUn4fZ7Z',
		'R3kMthN5YWFe',
		'3cXKfldMd5Yu',
		'4p6GUgOfff8D',
		'nvUStLglmaKJ',
		'N2wBcTNrpzSz',
		'NXSNwlmK6BiB',
		'HyBTbvPOXgAa',
		'AY0u0tt5NRlQ',
		'LSNb50vbEpqY',
		'VAt42hAF5tyO',
		'0bp1WYwjZNiL',
		'30sJtQWIVWvl',
		'FD6vUGgWoFj4',
		'HTWy8Ov4dlTn',
		'ucx2nB3jK8rG',
		'KSZSTwXM6oR8',
		'AXEAIspX2Qs6',
		'z4RbD41nC01l',
		'PW32ZRSzbBNQ',
		'GT4PzXYQEJkN',
		'W8ysLWLfAprE',
		'CphpRAuHfhW1',
		'7pgi9N6zbHJN',
		'GnVG3APRzmEN',
		'4wjcvMQd9Dv5',
		'Usi02VLQemsJ',
		'6ClGbSYi8z4l',
		'SuTQMR1BkkCj',
		'2zUuSrTb8QH8',
		'ZlrtehBDqvm6',
		'dI5jSvkGJD4K',
		'efjT5bcST6yX',
		'hBUQXANajqQp',
		'Q1CGCm8olGyt',
		'peRtMSvSgw8M',
		'fMwPoD7n6R17',
		'3iLKNUhF4cUt',
		'6yg67oYHzCat',
		'YYpS1GM52tSa',
		'M3Nb8H0Odvnp',
		'qsCo1bAGrOau',
		'AtkJdPaExOup',
		'krErPxX4IijN',
		'9MDF31Ssv0gc',
		'DuBK0XYAYz8J',
		'tCaOA3oW5PTV',
		'doRGWqk3UOwt',
		'S9InKmJCZXYA',
		'kakLlGTHTCbN',
		'CGK03uGbI7wo',
		'xLUb9IvB9n21',
		'dMWZNtCDOpSS',
		'UpWHoFbSDpT6',
		'FFlGYLih0421',
		'DkbmLOYglnjf',
		'zofDaeQTgHEO',
		'PjriVQtiV1dd',
		'NRNY4ZsJRXx3',
		'usrVGzkvPIXL',
		'WvBSWTJiAHKP',
		'QxeGYTzC2UZi',
		'6EDWSKtCF3SN',
		'VVLfq7pUko9z',
		'wwsS58MHX7ap',
		'F19C0cLgBxAs',
		'aKaSIGHN6B78',
		'ntDDnqsyKaIa',
		'cB6FsHIx1dVp',
		'HK92BzuLDWcW',
		'SnAaHKBPi6lg',
		'E2LEA4XZQ3UJ',
		'hCgrTTLJTxHf',
		'hYpoNJebVg7g',
		'Jcurz0zNqugY',
		'LWtvvp6cvnqS',
		'nfexLqFV876a',
		'HHIZE4yU1Ugn',
		'nqDRgDhwpKJF',
		'BTaFdc2r2lZe',
		'UiDqUrjEWbMN',
		'GxE13sUuzGUo',
		'crU51ejBJwji',
		'f9NQMYYWihEW',
		'Ft8MQMUaVqhS',
		'wLeuZ8f2v29t',
		'B2tiv55Bf1VC',
		'8sF8F10GRZmk',
		'gpTLLM6xaqg9',
		'D1MxKEDK60LX',
		'pLqe8RFfIEZa',
		'Ia1hEiETdrSk',
		'IWR1vWUuJX5C',
		'kq5sjIB8r8ei',
		'MApwOSDkfnnD',
		'W79e9Wgrzgmb',
		'GYQKoMVE1RSL',
		'4bAXIJbiv2fv',
		'TCR5mGp1ZLRV',
		'NaTvHfbNbXry',
		'j0LRF5UAaY1L',
		'x16oN55m4LIW',
		'bBYUnY3ppKTA',
		'VBE9lx9UGu1i',
		'Dnhu8lVyr6aA',
		'yfV2At1jeTtU',
		'4dItV2RnDGgJ',
		'eukPzLsp0XCU',
		'6qzg2h8ezjNu',
		'wke1cSU9prgV',
		'WUAh3CNJmKGf',
		'YXthklBEH3tG',
		'D3AYPUPfC5Pe',
		'U3Z9woy9wXjo',
		'3xsSak6CuOx1',
		'fYL0WUgc8qRZ',
		'epiOMsJcYZLA',
		'cLXhTFRBj92K',
		'SFwlPMmXLnrD',
		'AuJjiZ0hr5kS',
		'iWI5SDjHdWdc'
	]



class Subsession(BaseSubsession):
	def before_session_starts(self):

		# how long is the real effort task time? 
		# refer to settings.py settings. 
		for p in self.get_players():
		    if 'ret_time' in self.session.config:
		        p.ret_timer = self.session.config['ret_time']
		    else:
		        p.ret_timer = Constants.task_timer


class Group(BaseGroup):
	pass



class Player(BasePlayer):


	ret_timer = models.PositiveIntegerField(
	    doc="""The length of the real effort task timer."""
	)

	user_text = models.CharField(
		doc="user's transcribed text")
	is_correct = models.BooleanField(
		doc="did the user get the task correct?")
	ret_final_score = models.IntegerField(
		doc="player's total score up to this round")

	round_payoff = models.FloatField(
		doc="total number of correct real effort tasks, completed before timer expired")




	def set_final_score(self):
		correct_cnt = 0
		for p in self.in_all_rounds():
			if p.round_payoff != None: 
				correct_cnt = correct_cnt + p.round_payoff
			else:
				correct_cnt = correct_cnt + 0

		if correct_cnt == None: 
			self.ret_final_score = 40
		elif correct_cnt <= 10:
			self.ret_final_score = 40
		elif (correct_cnt > 10) & (correct_cnt < 20): 
			self.ret_final_score = 20 + (2 * correct_cnt)
		else:
			self.ret_final_score = 60





