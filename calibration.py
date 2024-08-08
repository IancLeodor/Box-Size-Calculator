import requests
import base64
import sys

def perform_calibration(image_path, known_width_cm, server_url):
    with open(image_path, 'rb') as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')

    data = {
        'image': f'data:image/jpeg;base64,{image_data}',
        'known_width_cm': known_width_cm
    }

    response = requests.post(f'{server_url}/calibrate', json=data, verify=False)

    if response.status_code == 200:
        calibration_data = response.json()
        print("Calibration successful:", calibration_data)
        return calibration_data
    else:
        print("Calibration failed:", response.json())
        return None

if __name__ == "__main__":
    result = perform_calibration('C:/Users/leodo/Desktop/cube_calculator/calibration.jpeg', 8.56, 'https://192.168.1.103:5000')
    if result:
        sys.exit(0)
    else:
        sys.exit(1)


# import requests
# import base64
# import sys


# # Use raw string to handle backslashes in the file path
# with open(r'C:\Users\leodo\Desktop\cube_calculator\calibration9.jpeg', 'rb') as image_file:
#     image_data = base64.b64encode(image_file.read()).decode('utf-8')

# known_width_cm = 9.56

# data = {
#     'image': f'data:image/jpeg;base64,{image_data}',
#     'known_width_cm': known_width_cm
# }

# # Send the POST request to the calibration endpoint with SSL verification disabled
# response = requests.post('https://192.168.1.103:5000/calibrate', json=data, verify=False)

# if response.status_code == 200:
#     calibration_data = response.json()
#     print("Calibration successful:", calibration_data)
# else:
#     print("Calibration failed:", response.json())
