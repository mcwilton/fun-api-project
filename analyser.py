import requests
from datetime import datetime

    
class Analyser():
    def __init__(self, base_url="https://prophetapis.pythonanywhere.com/v1"):
        self.base_url = base_url

    def _make_request(self, endpoint, params=None):
        response = requests.get(f"{self.api_url}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()
    
    def signals(self, base_url):
        self.base_url = base_url
        get_signal_ids = f"{self.base_url}/signals"
        id_list = []
        response = requests.get(get_signal_ids)
        responses = response.json()
        for response in responses:
            id_list.append(response['id'])           
        return id_list  
    
    def single_signal(self, id):
        get_one_signal = f"{self.base_url}/signals/{id}"
        sig_res= requests.get(get_one_signal)
        results = sig_res.json()   
        group = [results['group'], results.get('subsection')]   
        return {'name': results['name'], 'group': group}
        
    def get_signal_values(self, signal_id, start, end, page_size, offset):
        get_signal_values = f"{self.base_url}/signals/{id}/values"
        params = {
            'start': start,
            'end': end,
            'page_size': page_size,
            'offset': offset
        }
        response = requests.get(get_signal_values, params=params)
        return response.json()      
    
    def get_mean_value(self, name):
        mean_value_url = requests.get(f"{api_base_url}/filtered-data/{name}/")
        mean_val = mean_value_url.json()
        return f"the mean for {name} is {mean_val[0]['mean']}"   
    
    def get_std_value(self, name):
        mean_value_url = requests.get(f"{api_base_url}/filtered-data/{name}/")
        mean_val = mean_value_url.json()
        return f"the STD for {name} is {mean_val[0]['std']}"   
    
    def get_stats_value(self, name):
        mean_value_url = requests.get(f"{api_base_url}/filtered-data/{name}/")
        mean_val = mean_value_url.json()
        return f"the stats for {name} are, mean = {mean_val[0]['mean']} and std is {mean_val[0]['std']}"
      
    def raw(self, group, batch_size=1000):
        raw_value_url = requests.get(f"{api_base_url}/raw/{group}/")
        raw_value = raw_value_url.json()
        return raw_value
    

  
# Example Usage
api_base_url = "https://prophetapis.pythonanywhere.com/v1" 
analyser = Analyser(api_base_url)

signal_ids = analyser.signals(api_base_url)
print(signal_ids)

signal_info = analyser.single_signal(1)
print(signal_info)

signal_values = analyser.get_signal_values(signal_id=1, start="2023-07-10T00:00:00.000Z", end="2023-07-10T03:00:00.000Z", page_size=1, offset=0)
print(signal_values)

get_mean = analyser.get_mean_value(name = "signal1" )
print(get_mean)

get_std = analyser.get_std_value(name = "signal3" )
print(get_std)

get_stats = analyser.get_stats_value(name = "signal2" )
print(get_stats)

get_raw = analyser.raw(batch_size=1000, group='laboratory1')
print(get_raw)