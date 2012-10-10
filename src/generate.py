'''
generate test cases based on walking through a finite state machine

'''
import fsm
from random import choice

demo = fsm.Fsm('demo')

#putting text_file in global scope for now. TODO refactor
text_file = open("demo.py", "w")
'''
Setup the test, by creating the code headers and initialization for the tests

'''
def test_setup():
    text_file.write("#demo.py, automatically generated webdriver code\n")
    text_file.write("from selenium import webdriver\n")
    text_file.write("driver = webdriver.Firefox()\n")
    text_file.write("driver.get(\"http://blog.ruberto.com\")\n")
    
    return

def test_teardown():
    text_file.write("driver.quit()\n")
    text_file.write("print \"So long, and thanks for all the fish\"")
    text_file.close()  
    return

'''
This block will randomly walk through the state machine

Grab the list of transitions from the current state, randomly choose one, then make that transition.
This will take a machine, and walk n number of transitions
First version will print the steps. Eventually modify to generate the test cases

customers_link = driver.find_element_by_class_name("tag-link-9")
customers_link.click()
print driver.title

'''
def random_walk(m, n):
    index = 0
    
    while index < n :
        t = choice(m.get_trans_list(m.currentState) )           #randomly choose from the available transitions
        s = m.set_next_state(t[1])                          #transition to the next state
        text_file.write("link = driver.find_element_by_class_name( \"")
        text_file.write(t[1])
        text_file.write("\" )\n")
        text_file.write("link.click()\n")
        oracle = m.get_current_state_oracle() 
        text_file.write("assert driver.title == \"")
        text_file.write(oracle)
        text_file.write("\"\n")
        text_file.write("print \"Expected: " + oracle + " Got: \"," + "driver.title\n" )
        index += 1
    return


test_setup()
random_walk(demo, 5)
test_teardown()


