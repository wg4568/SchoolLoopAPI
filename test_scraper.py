import requests
from lxml import html
from bs4 import BeautifulSoup

url = "https://branham.schoolloop.com/portal/student_home"
login_url = "https://branham.schoolloop.com/portal/guest_home?etarget=login_form"
login_page_url = "https://branham.schoolloop.com/"
session_requests = requests.session()

result = session_requests.get(login_page_url)
form_data_id = result.text.split('<input type="hidden" name="form_data_id" id="form_data_id" value="')[1].split('"')[0]

username, password = open("login_info.txt", "r").read().split(" ")

payload = {
	"login_name": username,
	"password": password,
	"event.login":"https://cdn.schoolloop.com/1608130957/img/spacer.gif",
	"form_data_id": form_data_id
}

result = session_requests.post(
	login_url,
	data = payload, 
	headers = dict(referer=login_url)
)

result = session_requests.get(
	url,
	headers = dict(referer = login_url)
)

soup = BeautifulSoup(result.text, "lxml")
print soup.find_all("title")[0]