
from gmail import GMail, Message
from random import choice
import datetime
now = datetime.datetime.now()

reasons = ["chán đời","chưa làm bài tập","rảnh rỗi sinh nông nổi"]

gmail = GMail("khanhlinh.omega93@gmail.com","omegateam123")
html_template = """
<p style="text-align: center;"><strong>Đơn xin nghỉ học</strong></p>
<p style="text-align: left;">Em ch&agrave;o thầy Tuấn Anh,</p>
<p style="text-align: left;">T&ecirc;n em l&agrave; Kh&aacute;nh Linh</p>
<p style="text-align: left;">H&ocirc;m nay em {{sickness}} em xin thầy cho e nghỉ 1 buổi.</p>
<p style="text-align: left;">Kh&aacute;nh Linh.</p>
"""

html_content_to_send = html_template.replace("{{sickness}}", choice(reasons))
#placeholder

msg = Message("Đơn xin nghỉ học",
to = "lukhach.giangho2910@gmail.com",
html = html_content_to_send)


while True:
    setup_time = now.hour
    if setup_time == 07:
        gmail.send(msg)
        break
