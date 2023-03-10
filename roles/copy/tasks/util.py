import psutil

def get_cpu_temp():
    temp = psutil.sensors_temperatures().get('coretemp')[0].current
    return temp

if __name__ == '__main__':
    print(f'CPU temperature: {get_cpu_temp()}C')
