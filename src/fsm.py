'''
fsm is a class that implements a finite state machine, for use in fsbMBT
copyright 2012, John Ruberto

the finite state machine is represented as an indented list, of the following format:
all atomic data types are strings
machine has 1-n states, each state has 1-m transitions, each transition has a type, an action, and a next state name
[machine_name [ stateName stateOracle [[transistionType transistionAction statename]
                                       [...]]          #n-number of transitions
              [ stateName ... [transitionlist] ] 

for states, the first item in the list s[0] is always the state name.
the last item in the state is always a list of transitions

for transitions, the first item t[0] is the transition name. The last is the next state

the Fsb class will have a:
"current state" attribute
getNext(transition) method (which returns a stateName after taking the transition
getTransistions(state) method (which returns the available transitions for that state)
'''
import unittest


class Fsm:
    def __init__(self,file=None):
        if not file :
            self.mach = ['default' , [ ['s1' , 'ors1', [['test','t1a1','s2']]],        #temp, intent is to read from the filename
                                       ['s2' , 'ors2', [['test','t2a1','s2'],
                                                        ['test','t2a2','s1']]] ]]
        if file == "demo" :
            self.mach = ['ruberto.com', [ ['custState', 'Customers', [['management', 'tag-link-12', 'mgmtState' ],
                                                                      ['automation', 'tag-link-3', 'autoState' ] ] ],
                                          ['mgmtState', 'Management', [['automation', 'tag-link-3', 'autoState' ],
                                                                        ['customers', 'tag-link-9', 'custState' ] ]],
                                          ['autoState', 'Test Automation', [['automation', 'tag-link-3', 'autoState' ],
                                                                             ['customers', 'tag-link-9', 'custState' ],
                                                                             ['management', 'tag-link-12', 'mgmtState' ] ]] ] ]
                                        
            
        else:
            self.mach = ['TODOreadfromfile' , [ ['s1' ,'ors1', [['test' ,'t1a1' ,'s2']]] ,    
                                                ['s2' ,'ors2', [['test' ,'t2a1' ,'s2'],
                                                                ['test' ,'t2a2' ,'s1']]] ]]
        self.currentState = self.mach[1][0][0]                      #initialize to the first state
       
    def get_current_state_list (self):
        for s in self.mach[1:][0] :
            if s[0] == self.currentState :
                return s
        return None
    #returns the list that represents the current state (including all transitions


  
    def get_current_state_oracle(self):
        return self.get_current_state_list()[1]
    #returns the "oracle" of the current state
    
    
    
     
    def get_next_state (self,trans):                                
        tlist = self.get_current_state_list()[1:][-1]
        for t in tlist :
            if t[1] == trans :
                return t[-1]                                        # next state always last position in transistions
        return None
    #returns the next state, given the transition (assumes current state in self.currentstate 
    
    
    def set_next_state (self,trans):  
        self.currentState = self.get_next_state(trans)
        return self.currentState  
    #follows the transition and sets the currentState according to the state transitions (assumes current state in self.currentstate                          

            
    
    def get_trans_list(self,state):
        for s in self.mach[1:][0] :
            if s[0] == state :
                return s[-1]
        return None
    #returns a list of available transitions, given a current state
    


class TestFsm (unittest.TestCase):
    def setUp(self):
        self.test_d = Fsm()
        
    def test_initial_state(self):
        self.assertEqual(self.test_d.currentState, 's1')
    
    def test_get_next_state(self):
        self.assertEqual(self.test_d.get_next_state('t1a1'), 's2')
        
    def test_get_trans_list(self):
        self.assertEqual(self.test_d.get_trans_list('s1'), [['test','t1a1','s2']] )
        
    def test_demo(self):
        self.test_ruberto = Fsm('demo')
        self.assertEqual(self.test_ruberto.mach[0], 'ruberto.com')
        self.assertEqual(self.test_ruberto.currentState,'custState')
        self.assertEqual(self.test_ruberto.get_next_state('tag-link-12'),'mgmtState')
        nextstate = self.test_ruberto.set_next_state('tag-link-12')
        self.assertEqual(nextstate,'mgmtState')
        self.assertEqual(self.test_ruberto.get_current_state_oracle(),'Management')
        nextstate = self.test_ruberto.set_next_state('tag-link-3')
        self.assertEqual(self.test_ruberto.get_current_state_oracle(),'Test Automation')
        
        
#test = Fsm()
#print test.currentState
#print test.mach
#print test.get_current_state_list()
#print test.get_next_state('t1a1')
#print test.get_trans_list(test.currentState)


if __name__ == '__main__':
    unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFsm)
    unittest.TextTestRunner(verbosity=2).run(suite())              
        
