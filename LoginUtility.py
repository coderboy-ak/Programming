import xml.etree.ElementTree as ET
tree= ET.parse('SiteElement.xml')
root=tree.getroot()
class WebElement(object):

    def getSearchValue(pagenameattribute, elementKeystring):
        xpathstring = "./pages/page[@name=" + pagenameattribute + "']/element[@Key='" + elementKeystring + "']"
        # print(xpathstring)
        for element in root.findall(xpathstring):
            value = element.find('value').text
            return value


    def getSearchBy(pagenameattribute, elementKeystring):
        xpathstring = "./pages/page[@name=" + pagenameattribute + "']/element[@Key='" + elementKeystring + "']"
        # print(xpathstring)
        for element in root.findall(xpathstring):
            searchby = element.find('searchby').text
            return searchby