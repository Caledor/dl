from core.advbase import *
from slot.d import *
from slot.a import *

def module():
    return Zace

class Zace(Adv):
    a1 = ('s',0.2)
    conf = {}
    conf['slots.a'] = Resounding_Rendition()+Jewels_of_the_Sun()
    conf['acl'] = """
        `dragon
        `s3, not self.s3_buff
        `s4
        `s1
        `s2
        `fs, x=5
    """
    coab = ['Ieyasu','Wand','Dagger2']
    share = ['Ranzal']

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)