code = f.open("gsrseg.png")

# exercise 2
class C32:

    # cur_dict = {}
    # a_dict = {}
    # b_dict = {}
    # c_dict = {}
    # d_dict = {}
    # e_dict = {}
    # f_dict = {}


    def __init__(self):
        self.cur_dict = {}
        self.a_dict = {}
        self.b_dict = {}
        self.c_dict = {}
        self.d_dict = {}
        self.e_dict = {}
        self.f_dict = {}
        self.f_dict = {'step': [self.f_dict,'9'],'trace': ['2','8']}
        self.e_dict = {'step': [self.f_dict,'7']}
        self.d_dict = {'snap': [self.e_dict,'6']}
        self.c_dict = {'snap': [self.d_dict,'5']}
        self.b_dict = {'view': [self.c_dict,'4']}
        self.a_dict = {'step': [self.b_dict,'0'],'trace': [self.d_dict,'2'],'snap': [self.e_dict,'3'],'view': [self.f_dict,'1']}
        self.cur_dict = self.a_dict

    #@classmethod
    def step(self):
        if 'step' in self.cur_dict:
            if self.cur_dict is self.f_dict:
                print(self.cur_dict['step'][1])
                return
            print(self.cur_dict['step'][1])
            self.cur_dict = self.cur_dict['step'][0]
            return

        if 'step' not in self.cur_dict:
            print("RuntimeError")
            return

    def view(self):
        if 'view' in self.cur_dict:
            print(self.cur_dict['view'][1])
            self.cur_dict = self.cur_dict['view'][0]
            return

        if 'view' not in self.cur_dict:
            print("RuntimeError")
            return

    def snap(self):
        if 'snap' in self.cur_dict:
            print(self.cur_dict['snap'][1])
            self.cur_dict = self.cur_dict['snap'][0]
            return

        if 'snap' not in self.cur_dict:
            print("RuntimeError")
            return

    def trace(self):
        if 'trace' in self.cur_dict:
            print(self.cur_dict['trace'][1])
            self.cur_dict = self.cur_dict['trace'][0]
            return

        if 'trace' not in self.cur_dict:
            print("RuntimeError")
            return

o = C32()
# print(o.cur_dict)
o.step()
o.view()
o.snap()
o.snap()
o.step()
o.view()
o.step()
o.step()
o.trace()