from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

html_content = urlopen(url).read().decode("utf8")
soup = BeautifulSoup(html_content, "html.parser")

table = soup.find("table", id="tableContent")
tr_list = table.find_all("tr")

datas = []
headlines = ["truoc_sau", "q4_2016", "q1_2017", "q2_2017", "q3_2017"]


for tr in tr_list:
    td_list = tr.find_all("td")
    if len(td_list) != 0:
        data = {}
        for i in range(len(headlines)):
            data[headlines[i]] = td_list[i].string
        datas.append(data)

pyexcel.save_as(records=datas, dest_file_name="cafef.xlsx")
