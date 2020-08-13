from core.advbase import *
from slot.a import *

def module():
    return Fjorm

class Fjorm(Adv):
    comment = 'last bravery once at start'

    a3 = [('prep',1.00), ('scharge_all', 0.05)]

    conf = {}
    conf['slots.a'] = Resounding_Rendition()+His_Clever_Brother()
    conf['acl'] = """
        `s3, fsc
        `s4
        `s1
        `s2, fsc
        `fs, x=5
    """
    coab = ['Blade', 'Summer_Estelle', 'Xander']
    share = ['Gala_Elisanne', 'Ranzal']

    def prerun(self):
        Teambuff('last_bravery',0.3,15).on()
        Teambuff('last_bravery_defense', 0.40, 15, 'defense').on()

    def s1_proc(self, e):
        self.afflics.frostbite(e.name,120,0.41)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
