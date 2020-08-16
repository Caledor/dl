from core.advbase import *
from slot.a import *

def module():
    return Gauld

class Gauld(Adv):
    comment = 's2 after s1'
    a1 = ('a', 0.10, 'hp70')
    a3 = ('k_frostbite', 0.20)

    conf = {}
    conf['slots.a'] = Resounding_Rendition()+His_Clever_Brother()
    conf['slots.frostbite.a'] = conf['slots.a']
    conf['slots.d'] = Gaibhne_and_Creidhne()
    conf['acl'] = """
        `dragon.act('c3 s c3 end'), s and (not s2.check() or not s=2)
        `s1, s=2
        `s4
        `s3
        `s1, cancel
        `s2, s=1
        `fs, x=5
        """
    coab = ['Blade', 'Xander', 'Summer_Estelle']
    share = ['Gala_Elisanne', 'Ranzal']
    conf['afflict_res.frostbite'] = 0

    def prerun(self):
        self.phase['s1'] = 0
        self.s1_frostbite = [(120,0.37),(160,0.74),(160,0.74)]

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.phase[dst] = 0
        adv.s1_frostbite = [(120,0.37),(160,0.74),(160,0.74)]

    def s1_proc(self, e):
        with KillerModifier('s1_killer', 'hit', 0.20, ['frostbite']):
            self.dmg_make(e.name, 2.11)
            self.hits += 1
            self.afflics.frostbite(e.name,*self.s1_frostbite[self.phase[e.name]])
            self.dmg_make(e.name, 2.11)
            self.hits += 1
        if self.phase[e.name] == 2:
            Selfbuff(e.name,0.15,10).on()
        self.phase[e.name] = (self.phase[e.name] + 1) % 3

    def s2_proc(self, e):
        Selfbuff(e.name,0.25,5).on()
        self.s1.charge(self.s1.sp)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)