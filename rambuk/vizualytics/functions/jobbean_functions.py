# a webscraper test area for facebook scraping events
import requests
import json

# funktion, der håndterer cookies, headers og json_data parametre til brug i get_jobs_municipality
# man kan ændre på søgeordet, postnr hvor jobbet skal være, samt afstand fra postnr.
# MAXDISTANCE AND ZIPCODE GØR INTET LIGE NU
def jobnet_search_params(search_key, maxdistance, zipcode):
    cookies = {
    'CookieInformationConsent': '%7B%22website_uuid%22%3A%227d629e59-7688-4881-b4b6-00f106e8cccc%22%2C%22timestamp%22%3A%222022-06-02T10%3A10%3A53.774Z%22%2C%22consent_url%22%3A%22https%3A%2F%2Fjob.jobnet.dk%2FCV%2Ffrontpage%22%2C%22consent_website%22%3A%22Jobnet%20Prod%22%2C%22consent_domain%22%3A%22job.jobnet.dk%22%2C%22user_uid%22%3A%227362b098-db9b-46ce-b324-9f3fa3608616%22%2C%22consents_approved%22%3A%5B%22cookie_cat_necessary%22%2C%22cookie_cat_functional%22%2C%22cookie_cat_statistic%22%2C%22cookie_cat_marketing%22%2C%22cookie_cat_unclassified%22%5D%2C%22consents_denied%22%3A%5B%5D%2C%22user_agent%22%3A%22Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F101.0.4951.67%20Safari%2F537.36%22%7D',
    'Jobnet': 'zszuacemtkslrk3i53pcx3s1',
    'FrontPageBackgroundImageId': '6',
    }
    headers = {
        'authority': 'job.jobnet.dk',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'da-DK,da;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': 'CookieInformationConsent=%7B%22website_uuid%22%3A%227d629e59-7688-4881-b4b6-00f106e8cccc%22%2C%22timestamp%22%3A%222022-06-02T10%3A10%3A53.774Z%22%2C%22consent_url%22%3A%22https%3A%2F%2Fjob.jobnet.dk%2FCV%2Ffrontpage%22%2C%22consent_website%22%3A%22Jobnet%20Prod%22%2C%22consent_domain%22%3A%22job.jobnet.dk%22%2C%22user_uid%22%3A%227362b098-db9b-46ce-b324-9f3fa3608616%22%2C%22consents_approved%22%3A%5B%22cookie_cat_necessary%22%2C%22cookie_cat_functional%22%2C%22cookie_cat_statistic%22%2C%22cookie_cat_marketing%22%2C%22cookie_cat_unclassified%22%5D%2C%22consents_denied%22%3A%5B%5D%2C%22user_agent%22%3A%22Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F101.0.4951.67%20Safari%2F537.36%22%7D; Jobnet=zszuacemtkslrk3i53pcx3s1; FrontPageBackgroundImageId=6',
        'jobnet-angular-handle-errors-generically': 'true',
        'origin': 'https://job.jobnet.dk',
        'referer': f'https://job.jobnet.dk/CV/FindWork?SearchString=Underviser&Offset=0&SortValue=BestMatch&LocationZip={zipcode}&SearchInGeoDistance={maxdistance}',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'x-csrf-token': '6a22e1d3-548e-4671-a38e-302224c04402',
        'x-requested-with': 'XMLHttpRequest',
    }
    json_data = {
        'model': {
            'Offset': 0,
            'Count': 1,
            'SearchString': f'{search_key}',
            'SortValue': 'BestMatch',
            'Id': [],
            'EarliestPublicationDate': None,
            'HotJob': None,
            'Abroad': None,
            'NearBy': '',
            'OnlyGeoPoints': False,
            'WorkPlaceNotStatic': None,
            'WorkHourMin': None,
            'WorkHourMax': None,
            'Facets': {
                'Region': None,
                'Country': None,
                'Municipality': None,
                'PostalCode': None,
                'OccupationAreas': None,
                'OccupationGroups': None,
                'Occupations': None,
                'EmploymentType': None,
                'WorkHours': None,
                'WorkHourPartTime': None,
                'JobAnnouncementType': None,
                'WorkPlaceNotStatic': None,
            },
            'LocatedIn': 'None',
            'LocationZip': '',
            'Location': None,
            'SearchInGeoDistance': 0,
        },
        'url': '',
    }
    return cookies, headers, json_data

# This function does the request, and returns json data as a python dictionary.    
def request_data_jobnet(cookies, headers, json_data):
    response = requests.post('https://job.jobnet.dk/CV/FindWork/Search', cookies=cookies, headers=headers, json=json_data)
    data = json.loads(response.text)
    #save_json(data)
    return data

# We can save dict data to a .json file
def save_json(data, filename="sample.json"):
    with open(filename, "w") as outfile:
        outfile.write(json.dumps(data, indent=2, ensure_ascii=False))

def get_jobs_municipality(search_key, maxdistance=50, zipcode=6400):
    cookies, headers, json_data = jobnet_search_params(search_key, maxdistance, zipcode)
    job_data = request_data_jobnet(cookies, headers, json_data)
    len(job_data['JobPositionPostings'])
    city_jobs_dict = {}
    
    muni = job_data['Facets']['Municipality']
    total_jobs = 0;
    for by in muni:
        city_jobs_dict[by['Value']] = by['Count']
        total_jobs += int(by['Count'])
    return city_jobs_dict, total_jobs
    

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"model":{"Offset":0,"Count":20,"SearchString":"IT","SortValue":"BestMatch","Id":[],"EarliestPublicationDate":null,"HotJob":null,"Abroad":null,"NearBy":"","OnlyGeoPoints":false,"WorkPlaceNotStatic":null,"WorkHourMin":null,"WorkHourMax":null,"Facets":{"Region":null,"Country":null,"Municipality":null,"PostalCode":null,"OccupationAreas":null,"OccupationGroups":null,"Occupations":null,"EmploymentType":null,"WorkHours":null,"WorkHourPartTime":null,"JobAnnouncementType":null,"WorkPlaceNotStatic":null},"LocatedIn":null,"LocationZip":null,"Location":null,"SearchInGeoDistance":0},"url":"/CV/FindWork?SearchString=IT&Offset=0&SortValue=BestMatch"}'
#response = requests.post('https://job.jobnet.dk/CV/FindWork/Search', cookies=cookies, headers=headers, data=data)

if __name__ == "__main__":
    print(get_jobs_municipality("lærer"))