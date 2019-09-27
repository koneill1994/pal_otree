from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass
    
    
class SchoolTimeWaitPage(Page): 
    form_model='player'
    form_fields=['hovercount','hovertime','hover_json']  
    
 
    def before_next_page(self):
        self.group.get_pair()
        
class schooltime1(Page):
    form_model='player'
    form_fields=['pair_choice']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    def after_all_players_arrive(self):
        pass

class SchooltimeResults(Page):
    form_model='player'
    form_fields=['player_choice_final',
        'hovercount1','hovertime1','hover_json1',
        'hovercount2','hovertime2','hover_json2',
        'hovercount3','hovertime3','hover_json3',
        'hovercount4','hovertime4','hover_json4'
    ]

    pass

page_sequence = [
    SchoolTimeWaitPage,
    schooltime1,
    ResultsWaitPage,
    SchooltimeResults
]
