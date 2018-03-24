from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://dantri.com.vn"
#
# 1. Download web page
# # 1.1 Open connection
# conn = urlopen(url)
# #1.2 Read
# data = conn.read()
# #1.3 Decode
# html_content = data.decode("utf8")

html_content = urlopen(url).read().decode('utf8')

# print(html_content)
# Save html_content to file
# html_file = open("dantri.html","wb")
# html_file.write(html_content)
# html_file.close()

# 2. Extract ROI (Region of Interest)
soup = BeautifulSoup(html_content, "html.parser") #xml, xhtml, html
ul = soup.find("ul","ul1 ulnew")

# print(ul.prettify())

# 3. Extract Info
li_list = ul.find_all("li")

datas = []

for li in li_list:
    # create a dictionary
    data = {}
    a = li.h4.a #What's "a" here?
    data["title"] = a.string
    data["link"] = url + a["href"]
    datas.append(data)

pyexcel.save_as(records=datas, dest_file_name = "dantri.xlsx")
