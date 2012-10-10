fsmMBT Update
Refactoring to use Python & WebDriver
the intial prototype code is now removed. Contact me if you are interested in seeing very hacky c# and ruby code
 

fsmMBT Readme
======

Finite State Machine - Model Based Testing

This demonstrates model based testing, using a finite state machine 


Files:
======
fsm.py  : implements a finite state machine. The current implementation uses nested lists to describe the machine:
- machine has a list of states
- each state has a name, an oracle, and a list of transitions
- each transition has a name, a key, and a next state

fsm has a variety of methods to get state & transition information, as well as to advance to the next state (given a transition)
TODO: implement reading of the state machine from a file. This demo uses a machine definition in the constructor


generate.py  : generates webdriver tests based on the finite state machine
Creates a file, demo.py, which contains:
- test_setup(): Header information (comment, import statement, webdriver initialization)
- random_walk(machine, n): "walks" the machine n number of random steps, and adds the webdriver code to the file
    - One of the available transitions are followed. The transition is chosen randomly at runtime
    - The generated code will find the link specified in the machine defintion, click it, and verify that
      the browser navigated to the target page (the verification is by page title, which is defined by the "oracle" in the machine
    - Expected title and actual title are printed. This is where we could count the successes
- test_teardown(): write a webdriver command to close the browser and then close the file

generate.py generates a file called demo.py
demo.py is executable at terminal command line: python demo.py

Why:
====
Several reasons for this project:
- Demonstrate the concept of Model Based Testing with a real example
- Revive my original demo, which no longer worked. (C# for FSM & test generation, WATIR/Ruby for the tests)
- Practice for using webdriver python bindings
- Practice with python
- For fun

Why model based testing:
- Automatically generating tests from a model allows the creation of high volumes of test input
- randomly generating test, along with oracles, can allow finding interesting things that may not be found on purpose
- enhancing the test suite involves enhancing the model, not refactoring/writing a lot of code.
- This demo is a trivial example, though, when I used it originally on the SBConnect project, it did find errors in the system
- There should be more applications to this concept.
- Next demo will be to model accounting principles, and generate random web-service tests based on that model




