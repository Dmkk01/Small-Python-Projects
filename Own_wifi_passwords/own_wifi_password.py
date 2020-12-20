import subprocess

# Accessing the our results
result = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
# Splitting the results to obtain a list of all wifi names
all_wifi = [line.split(':')[1][1:-1] for line in result if 'All User Profile' in line]


print('Name                      | Password     ')
# Looping over each wifi to extract its password
for wifi in all_wifi:
    try:
        # Accessing the wifi information
        password = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
        # Obtaining the wifi
        password = [line.split(':')[1][1:-1] for line in password if 'Key Content' in line]
        # Printing out the results
        print('{:^25} | {:^25}'.format(wifi, password[0]))
    # If the wifi has no password, an error will be raised.
    except:
        print('{:^25} |       No Password'.format(wifi))