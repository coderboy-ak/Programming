#error in this program
import unittest
import json
import urllib3
class RestApiTest(unittest.TestCase):
    def setUp(self):
        #define Api URL and API key
        self.ApiUrl="http://api.openweathermap.org/data/2.5/forecast"
        self.ApiKey="70926ddfd37fdf454548dbi3695995"
    def test_weather_api_by_city_name1(self):
        #define  api response
        testurl=(self.ApiUrl+"?q=London,uk"+"&"+"APIID="+self.ApiKey)
        print(testurl)
        response=urllib3.urlopen(testurl)
        #read response
        html=response.read()
        #print response
        print(html)
        #assert response
        self.assertTrue("London" in html)
    def test_weather_api_by_City_name2(self):
        #define api response
        testurl=(self.ApiUrl+"?q=London,uk"+"&"+"APIID="+self.ApiKey)
        print(testurl)
        response= urllib3.urlopen(testurl)
        #read response
        html=response.read()
        #print response
        print(html)
        #load response as json
        json_data=json.loads(html)
        #get the key "name" value
        city_name=json_data("name")
        #assert city name
        self.assertTrue(city_name="London")

    def tearDown(self):
        print("-------- test is Over ---------")
        print("---------------------")
if __name__ == "__main__":
    unittest.main()


