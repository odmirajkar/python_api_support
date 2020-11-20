import unittest
from selenium_support import selenium_support
import time
import sys
import HtmlTestRunner
from os import path

class Test_ATT(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #time.sleep(80)
        cls.support=selenium_support()
        #cls.support.init()
        
    def test_api(self):
        import requests
        response=requests.get("http://ergast.com/api/f1/2017/circuits.json")    
        self.assertEqual(response.status_code,200)
        print(response.json())
    

        

        
def main(out = sys.stderr, verbosity = 2): 
    loader = unittest.TestLoader() 
    #import os

    #module=os.path.splitext(os.path.basename(__file__))[0]
    #suite = loader.loadTestsFromName(module+'.TestCases.test_b')
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    print(suite)
    #unittest.TextTestRunner(out, verbosity = verbosity).run(suite) 
    #output_file = open("HTML_Test_Runner_ReportTest.txt", "w")
    if path.exists("/tmp"):
        report_filder='/tmp/report'
    else:
        report_filder='./report'

    html_runner = HtmlTestRunner.HTMLTestRunner(
        #    stream=output_file,
            report_title='HTML Reporting using PyUnit',
            descriptions='HTML Reporting using PyUnit & HTMLTestRunner',
            output=report_filder
        )
    #unittest.TestRunner()
    html_runner.run(suite)


if __name__ == "__main__":
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store', dest='config_value',help='Store a simple value')
    results = parser.parse_args()
    print ('config_value     =', results.config_value)
    Test_Zypher.config=results.config_value
    #unittest.main(verbosity=2)
    """
    
    #time.sleep(30)
    main()
    #with open('testing.out', 'w') as f: 
    #    main(f)
