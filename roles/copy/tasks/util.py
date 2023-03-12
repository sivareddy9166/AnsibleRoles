import psutil

def get_cpu_temp():
    sensors = psutil.sensors_temperatures()
    if sensors.get('coretemp'):
        temp = sensors['coretemp'][0].current
        return temp
    else:
        return None

if __name__ == '__main__':
    cpu_temp = get_cpu_temp()
    if cpu_temp:
        print(f'CPU temperature: {cpu_temp}C')
      else:
        print('Unable to retrieve CPU temperature.')
