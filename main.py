import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

if request.method == 'POST':
    name = request.values['name']
    email = request.values['email']
    phone = request.values['phone']
    message = request.values['message']

    text = "姓名：{}\n信箱：{}\n電話：{}\n\n內容：\n{}".format(name, email, phone, message)
    text = MIMEText(text)

    content = MIMEMultipart() #建立 MIMEMultipart 物件
    content["subject"] = "有人在網站留言給你囉" #郵件標題
    content["from"] = "jaing885@gmail.com" #寄件者
    content["to"] = "jaing885@gmail.com" #收件者
    content.attach(text)


    smtp = smtplib.SMTP(host="smtp.gmail.com", port="587")
    with open("password.txt", "r") as f:
        mailToken = f.read()

    with smtp: # 利用 with 來自動釋放資源
        try:
            smtp.ehlo() # 驗證SMTP伺服器
            smtp.starttls() # 建立加密傳輸
            smtp.login("sender@gmail.com", mailToken)
            smtp.send_message(content) # 寄送郵件
            print("Email is Sended completely!")    
            smtp.quit()
        except Exception as e:
            print("Error message: ", e)
