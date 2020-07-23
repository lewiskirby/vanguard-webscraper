from selenium import webdriver
import smtplib
from creds import email_address, email_password, vanguard_username, vanguard_password

#Details
name = 'Lewis'
currency = 'GBP'

#Scrape the data needed from Vanguard

driver = webdriver.Chrome('C:\\Users\\lewis\\Anaconda3\\chromedriver.exe')
driver.set_page_load_timeout(10)
driver.get('https://secure.vanguardinvestor.co.uk/Login?intcmpgn=header_login_link')

username = driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div/div/div[2]/div/form/div[2]/div[1]/div[1]/div[2]/input')
username.click()
username.send_keys(vanguard_username)

password = driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div/div/div[2]/div/form/div[2]/div[2]/div[1]/div[2]/input')
password.click()
password.send_keys(vanguard_password)

#click login
driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/div/div/div[2]/div/form/div[2]/div[3]/button').click()

driver.implicitly_wait(10)

balance = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/span/span').text
balance = balance.replace('£','')
balance = balance.replace(',','')
balance = float(balance)

driver.quit()

#Send the email

#create connection object
conn = smtplib.SMTP('smtp-mail.outlook.com', 587) #(domain name, port number)

#check if set up correctly
conn.ehlo()
#encryption for passwords
conn.starttls()
#log in
conn.login(email_address, email_password)
#send the email
conn.sendmail(email_address, email_address, "Subject: Vanguard Balance\n\nDear {n},\n\nToday's Vanguard balance is {b}{c}.\n\nHave a good day!".format(n=name,b=balance,c=currency).encode('utf-8'))
#disconnect from smtp server
conn.quit()