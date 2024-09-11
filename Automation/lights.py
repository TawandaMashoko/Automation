import requests

def control_smart_lights(action):
    url = f'https://maker.ifttt.com/trigger/{action}/with/key/your_ifttt_key'
    response = requests.post(url)
    if response.status_code == 200:
        print(f'Successfully triggered {action}')
    else:
        print(f'Failed to trigger {action}, status code: {response.status_code}')

# Turn on lights when phone enters a specific location
control_smart_lights('lights_on')

# Turn off lights when you leave the location
control_smart_lights('lights_off')
