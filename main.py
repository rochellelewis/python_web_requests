import requests
import urllib3

# Disable SSL warning messages
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Open the file containing the URLs
with open('domain_list.txt', 'r') as f:
    urls = f.readlines()

# Loop through the URLs and make GET requests to each
for url in urls:
    url = url.strip()  # Remove any whitespace or newline characters
    url = "http://" + url # set your protocol here :P

    # counter for retries - set as needed
    retries = 0

    while retries < 1:
        try:
            response = requests.get(url, verify=False)
            if response.status_code == 200:
                print(f'{response.status_code}: Success from {url}')
                break
            else:
                print(f'{response.status_code}: Error from {url}')
                break
        except requests.exceptions.ConnectionError as e:
            if isinstance(e, requests.exceptions.HTTPError) and 'HTTPConnectionPool' in str(e):
                # do something here, if you want
                pass
            else:
                # print(f'{str(e)} Error from {url}')
                retries += 1
        
        if retries == 1:
            print(f'Not retrying. Unable to connect to {url}')
