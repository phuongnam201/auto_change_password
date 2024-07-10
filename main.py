import requests
import pandas as pd

# Đường dẫn tới file Excel của bạn
excel_file = 'C:/Users/Admin/Documents/listaccount.xlsx'
#file excel chứa thông tin thành công hoặc thất bại ( file này không cần tạo )
updated_excel_file = 'C:/Users/Admin/Documents/listaccount_updated.xlsx'

df = pd.read_excel(excel_file)

df['status'] = ''

url = 'http://dd.ninjaschool.vn/app/index.php?for=event&do=changepass'


for index, row in df.iterrows():
    data = {
        'username': row['username'],
        'pass': row['curpassword'],
        'npass': row['npass'],
        'repass': row['rnpass']
    }
    response = requests.post(url, data=data)
    response_length = len(response.text)
    if response.status_code == 200:
        if response_length == 10664:
            print(f"Đổi mật khẩu thành công nick thứ {index + 1}")
            df.at[index, 'status'] = 'success'
        else:
            print(f"Đổi mật khẩu thất bại nick thứ {index + 1}")
            df.at[index, 'status'] = 'failed'
    else:
        print(f"Request cho dòng {index + 1} thất bại với mã trạng thái: {response.status_code}")
        df.at[index, 'status'] = 'failed'

# Lưu DataFrame đã cập nhật với tên file mới
df.to_excel(updated_excel_file, index=False)
