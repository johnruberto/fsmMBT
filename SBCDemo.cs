using System;
using System.Collections;
using workingcode.util;
using StateTableModel;

class SBCDemo {



    public void verifyState(string state, string verifyString)
    {
        // writes watir code to verify the state
    }

    static void otherMain()
    {

        newFSM mach = new newFSM("SBCDemo.xml");
        mach.displayStates();

    }

	static void Main() {

		XMLStateMachine fsm = new XMLStateMachine();
		fsm.StateTable = "sbcDemo.xml";
		fsm.CurrentState ="login";
        Int32 loopCount = 0;
        String[] actions = { "clicklogout", "clickhome", "clickrolo", "clickbi" };
        string[] loginActions = { "validPass", "invalidPass" };

        Hashtable verifyStrings = new Hashtable();
        Hashtable actionlinks = new Hashtable();

        string nextaction = String.Empty;

		Random rnd = new Random();

        verifyStrings["login"] = "Sign In";
        verifyStrings["home"] = "Home";
        verifyStrings["rolo"] = "Other ways";
        verifyStrings["bi"] = "Open Quickbooks";

        actionlinks["clicklogout"] = "Sign Out";
        actionlinks["clickhome"] = "Home";
        actionlinks["clickrolo"] = "Company Directory";
        actionlinks["clickbi"] = "Business Intelligence";

        Console.WriteLine("# Model Based Testing Example: John Ruberto, Updated on 9/18/07 with SBConnect Portal");
        Console.WriteLine("require \'watir\'");
        Console.WriteLine("ie = Watir::IE.new");
        Console.WriteLine("ie.goto(\"https://businessconnectqa.oss.intuit.com/portal/\")");
        Console.WriteLine("sleep 6");
        Console.WriteLine();
        Console.WriteLine("testsPassed = 0");
        Console.WriteLine("testsExecuted = 0");
        Console.WriteLine("# start of generated tests ");
        Console.WriteLine();



        for (loopCount = 0; loopCount < 25; loopCount++)
        {
            Console.WriteLine("# Test {0}", loopCount+1);

            if (fsm.CurrentState == "login")
            {
                // choose random action
                nextaction = loginActions[rnd.Next(0, 2)];
                
                // determine the next state
                fsm.Next(nextaction);
                Console.WriteLine("# Action = {0},  NewState = {1}", nextaction, fsm.CurrentState);

                // perform the action
                if ("validPass" == nextaction)
                {

                    Console.WriteLine("ie.text_field(:name, \"wapLoginForm:wap-login-memberID\").set(\"jbossqa\")");
                    Console.WriteLine("ie.text_field(:name,\"wapLoginForm:wap-login-password\").set(\"intuit.com\")");
                    Console.WriteLine("ie.button(:name, \"wapLoginForm:wap-login-loginPageSignIn\").click");
                    Console.WriteLine("sleep 6");
                }
                else if ("invalidPass" == nextaction)
                {
                    Console.WriteLine("ie.text_field(:name, \"wapLoginForm:wap-login-memberID\").set(\"jbossqa\")");
                    Console.WriteLine("ie.text_field(:name,\"wapLoginForm:wap-login-password\").set(\"int\")");
                    Console.WriteLine("ie.button(:name, \"wapLoginForm:wap-login-loginPageSignIn\").click");
                    Console.WriteLine("sleep 6");
                }

            }

            else
            {
                nextaction = actions[rnd.Next(0, 4)];
                fsm.Next(nextaction);
                Console.WriteLine("# Action = {0},  NewState = {1}", nextaction, fsm.CurrentState);
                Console.WriteLine("ie.link(:text, \"" + actionlinks[nextaction] + "\").click");
                Console.WriteLine("sleep 6");
            }

            //verify result

            Console.WriteLine("testsExecuted += 1");
            Console.WriteLine("if ie.contains_text(\"" + verifyStrings[fsm.CurrentState] + "\")");
            Console.WriteLine("  puts \"Test Passed\" ");
            Console.WriteLine("  testsPassed += 1");
            Console.WriteLine("else");
            Console.WriteLine("   puts \"Fail - expected: " + verifyStrings[fsm.CurrentState] + "\"");
            Console.WriteLine("end");
            Console.WriteLine();


          
        }

        Console.WriteLine("puts \"test passed= \" ");
        Console.WriteLine("puts testsPassed");
        Console.WriteLine("puts \"total tests=\"");
        Console.WriteLine("puts testsExecuted");
		
	}
}