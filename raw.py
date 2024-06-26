import requests
import pandas as pd 

# URL của tệp CSV
url = 'https://raw.githubusercontent.com/minhpqn/vietner/master/vlsp2016_exp/data/test_sample-tab.txt'

# Gửi yêu cầu GET để tải tệp
response = requests.get(url)
sum = 0
data = []
# Kiểm tra nếu yêu cầu thành công
if response.status_code == 200:
    # Tách nội dung tệp theo dòng
    lines = response.text.splitlines()

    # Hiển thị 10 dòng đầu tiên
    for line in lines[:]:
            data.append(line.split())
print(data)
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3', 'Column4'])
df.shape
df.to_csv('test.csv', index=False, encoding='utf-8')