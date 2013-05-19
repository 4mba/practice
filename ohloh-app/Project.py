#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import urllib
import elementtree.ElementTree as ET


class Project:
    search = str()
    api_key = "fUCeo1tkdu5ziEwCTO1A"
    url = "http://www.ohloh.net/p.xml?api_key="+api_key+"&query="
    license_base = "https://www.ohloh.net/licenses/"
    
    

    def __init__(self, search):
        """ 오픈소스 프로젝트 검색어인 'search'를 Project 멤버인 
            self.search에 초기화 한다.
        """
        self.search = search
    
    ## Return a list of OSS project information (JSON Type)
    def get_project(self, pageIndex):
        """ 클래스 생성자에 초기화된 search값의 오픈소스 프로젝트를 검색한다.
        pageIndex는 검색결과의 몇번째 페이지를 보여줄 것인지를 결정한다.  
         """
        url = self.url + self.search+"&page="+str(pageIndex)
        f = urllib.urlopen(url)
        
        # Parse the response into a structured XML object
        tree = ET.parse(f)
        
        # Did Ohloh return an error?
        elem = tree.getroot()
        error = elem.find("error")
        if error != None:
            print 'Ohloh returned:', ET.tostring(error),
            sys.exit()
        
        # project header
        header = dict()
        project_list = list()
        
        header['items_available'] = elem.find("items_available").text 
        header['items_returned'] = elem.find("items_returned").text 
        header['first_item_position'] = int(elem.find("first_item_position").text) 
        
        # Output all the immediate child properties of an Account
        for projects in elem.findall("result/project"):
            data = dict()
            data['header'] = header
            data['id'] = projects.find("id").text
            data['name'] = projects.find("name").text 
            data['homepage_url'] = projects.find("homepage_url").text
            #data['description'] = (projects.find("description").text).replace('"','')
            data['description'] = " TEST "

            # 로고 정보를 가지고 있지 않은 프로젝트도 있음 
            if(ET.iselement(projects.find("medium_logo_url"))):
                data['medium_logo_url'] = projects.find("medium_logo_url").text
                data['small_logo_url'] = projects.find("small_logo_url").text
            else:
                data['medium_logo_url'] = "#"
                data['small_logo_url'] = "#"
                
            data['ohloh_url'] = "https://www.ohloh.net/p/"+data['id']
        
            licenses = list()
            # Multi-License parsing
            for item in projects.findall("licenses/license"): 
                license = dict()
                license['name'] = item.find("name").text
                license['nice_name'] = item.find("nice_name").text
                license['license_url'] = self.license_base+item.find("name").text
                licenses.append(license)
              
            # 라이선스 정보가 아예 없을경우에는 'unknown' 으로 표시함      
            if (len(licenses) == 0):
                item = dict()
                item['name'] = 'unknown'
                item['nice_name'] = 'unknown'
                item['license_url'] = '#'
                licenses.append(item)

            data['licenses'] = licenses
            project_list.append(data)

        ## Return arrays of JSON type string data
        return project_list
    

        def save_result(search_result):
            """ do save """
            return None
            