from core.advbase import *
from slot.d import *

def module():
    return Dragonyule_Cleo

class Dragonyule_Cleo(Adv):
    a1 = ('a',0.13,'hp70')
    a3 = ('ecombo',30)

    conf = {}
    conf['slots.d'] = Gaibhne_and_Creidhne()
    conf['acl'] = """
        `dragon.act('c3 s end')
        `s1
        `s4
        `s3, cancel
        `s2, cancel
        `fs, x=5
    """
    coab = ['Blade', 'Xander', 'Summer_Estelle']
    share = ['Gala_Elisanne', 'Eugene']

    def prerun(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff
        self.phase['s1'] = 0

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.buff_class = Teambuff if adv.condition('buff all team') else Selfbuff
        adv.phase[dst] = 0

    def s1_proc(self, e):
        self.energy.add(1, team=self.condition('buff all team'))
        self.phase[e.name] += 1
        if self.phase[e.name] > 1:
            self.buff_class(e.name,0.1,10).on()
        if self.phase[e.name] > 2:
            self.buff_class(f'{e.name}_crit',0.08,10,'crit','chance').on()
        self.phase[e.name] %= 3

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
