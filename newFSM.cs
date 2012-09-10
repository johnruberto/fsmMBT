using System;
using System.Collections.Generic;
using System.Text;
using System.Xml;

namespace StateTableModel
{
    class newFSM
    {
        private XmlDocument fsm = new XmlDocument(); 

        public newFSM(string filename)
        {
           fsm.Load(filename);
        }

        public newFSM()
        {
            fsm.Load("sbcDemo.xml");
        }

        public void displayStates()
        {

            //Display all the states.
            XmlNodeList elemList = fsm.GetElementsByTagName("transis");
            for (int i = 0; i < elemList.Count; i++)
            {
                Console.WriteLine(elemList[i].InnerXml);
            }  
        }




  }

    
}
