import requests

# url = 'http://stgapiint64.corbis.pre/search/V3/Search?ActivityId=fa913ec9-8aae-469c-8bed-a17087074390&ClientIp=127.0.0.1&Plan=SolrImage&EnableSlotting=True&IsAnonymous=True&EnableOutlineForAll=False&Permissions=HasPermissionSearchRF,HasPermissionSearchRM,HasPermissionSearchRS&CountryCode=US&Language=en-US&PageNumber=1&SearchText=fishsticks&PageLength=25&SessionId=7d4e5bc7-f6cc-41ee-be9c-6be6eaeb192f&Sort=score'
#url = 'http://localhost.corbisimages.corbis.pre/ajax/search/results'
url = 'http://localhost.corbisimages.corbis.pre/ajax/search/navigator?_=1326391281792&parameters=q%3Dcat%26p%3D1%26cat%3D21'
#url = 'http://localhost.corbisimages.corbis.pre/MotionSearch/GetMotionSearchResultsCount'
#data = {'query': 'cat'}
#r = requests.post(url, data)

#url = 'http://localhost.corbisimages.corbis.pre/SearchTools/GetMinSearchResultsData'

headers = {'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': str(len(url)),
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'Profile=UserName=sqacax&Culture=en%2DUS; CorbisAnonymousAuth=ZNjSyDoDzQEkAAAAN2EzZjRlZmYtYWJlZS00MGIyLWExMzYtMDFlNDQ3YTMxOGQ2yXP9pjXADb9bH1vxND-f-_jOE341; LightboxCart=lightboxId=11049097; NavigatorOptions.NewUser=ClarifiedToolTip=true; __utma=235954910.1536178947.1325877928.1326225028.1326228538.8; __utmz=235954910.1325877928.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); SessionData=SessionUid=%3cguid%3e9151de77%2D1f04%2D4b00%2D8797%2D297ff87e6e6b%3c%2fguid%3e; CheckSums=SessionData=diRZoFGFwVSUuEtGQSkMiw%3d%3d&Profile=qpRLId1oEpSqs%2fkY6Lc1vQ%3d%3d; ASP.NET_SessionId=5ohxyhbzbgc1pail0hsp3r22; NavigatorOptions.FirstSession=FirstSession=true; NavigatorOptions.CollapsedLists=header-Composition,header-Orientation,header-Ethnicity,header-AgeAll; s_sq=%5B%5BB%5D%5D; s_cc=true; Search=sort=&cl=1&image_preview=1&AutoComplete=True&def=cat%3D21; resultsSearchSortParam=0; PagePrefs=SearchResults.aspx_Layout=standard&MyLightboxes.aspx_Layout=Unknown&PageSize=items50; searchOptions=%7B%22q%22%3A%22cat%22%2C%22cat%22%3A%2221%22%7D; minResultsSortParam=0; resultsDisplayOptionsCookie=%7B%22layout%22%3A%22detail_inline%22%2C%22category%22%3Atrue%2C%22collection%22%3Atrue%2C%22image_number%22%3Atrue%2C%22title_caption%22%3Atrue%2C%22date%22%3Atrue%2C%22credit_photo%22%3Afalse%2C%22autocomplete%22%3Atrue%2C%22term_clarify%22%3Atrue%2C%22image_preview%22%3Atrue%2C%22page_size%22%3A25%7D; UserSearchOptions=q=cat&p=1&cat=21'
    }

r = requests.get(url, headers=headers)
print r.content