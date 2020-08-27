import adv.adv_test
from core.advbase import *
from slot.a.all import The_Bridal_Dragon, From_Whence_He_Comes
from slot.d import PopStar_Siren

def module():
    return Halloween_Lowen

class Halloween_Lowen(Adv):
    comment = 'hlowen dps <= burn DoT'
    a1 = ('fsprep', 3)
    a3 = ('prep', 0.75)

    conf = {}
    conf['slots.a'] = From_Whence_He_Comes()+The_Bridal_Dragon()
    conf['slots.burn.a'] = conf['slots.a']
    conf['slots.d'] = PopStar_Siren()
    conf['acl'] = """
        `dragon
        `s2, pin='prep' or x=5 and self.hp_stack < 3
        `s1, x=5
        `s3, x=5
        `s4, x=5
        `fs, s=3 and self.fs_prep_c > 0
    """
    coab = ['Tobias', 'Euden', 'Yuya']
    share = ['Patia', 'Summer_Cleo']

    def init(self):
        self.hp_stack = 0
    
    def s1_proc(self, e):
        self.Teambuff('defchain',0.10,15).on()
    
    def s2_proc(self, e):
        self.buff_max_hp(f'{e.name}_hp', 0.10, True)

if __name__ == '__main__':
    import sys
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
