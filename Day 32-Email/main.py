import smtplib

my_email = "notujjwal52@gmail.com"
password = ""         # create app password after turning on 2 step verification

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="prabalbaijal11@gmail.com",msg="Subject:Bhag le\n\nSde 3 at google-offer for you")
