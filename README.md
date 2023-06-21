# artiPHISHial
![Artiphishial_75](https://github.com/gingapower/artiPHISHial/assets/87360317/013e1409-b728-428f-855c-48ca27d5a1eb)

Automatic Login Page Generator for Phishing purposes. 
this tool sets up a phishing mail with Flask in about 2 minutes. The tool clones the original page, inserts all necessary components, and sets up the Flaskapp.

# Tool
react frontend version:

![image](https://github.com/gingapower/artiPHISHial/assets/87360317/bbd2f2ac-e963-472a-ac42-a7011eb1dc0d)

terminal version:

![image](https://github.com/gingapower/artiPHISHial/assets/87360317/b84c7d09-574a-4cc3-8744-be8dabb03387)




# setup
## Terminal version
```
cd terminal
pip install -r requirements.txt
python scraper.py
```
optinal you can setup an python virtuel environment
```
python -m venv myenv
```
## frontend version
you have to install node.js:
https://www.knowledgehut.com/blog/web-development/install-nodejs-npm-on-windows
```
cd frontend/frontend
npm install
npm start
```
you also have to start the flask api at the same time:
```
cd frontend/backend
python backend.py
```

# ussage
```
py flaskapp.py
```
by default, flaskapp is started on localhost:5000.
You can change the setting in the flaskapp.py file

change
```
 app.run(port=5000,debug=True)
```
to 
```
 app.run(ip=1.2.3.4, port=5000,debug=True)
```

with the gui version, you have the possibility to download an executable file to launch the phishing webpage on windows:

![image](https://github.com/gingapower/artiPHISHial/assets/87360317/56701c3c-a23c-451f-97d3-c45a94858596)

You can also just download the cloned files:

![image](https://github.com/gingapower/artiPHISHial/assets/87360317/0cf27131-c2a7-4858-a27d-1052017f208a)

# Succes rate
| Webapage  | succes |
| ------------- | ------------- |
https://www.google.com| 	works
https://www.facebook.com |	works
https://twitter.com	|fail
https://www.instagram.com |	fail
https://www.linkedin.com  |	works
https://github.com |	works
https://www.amazon.com |	fail
https://www.netflix.com | works
https://www.dropbox.com | fail
https://www.paypal.com |	works
https://www.reddit.com	|	works
https://www.ebay.com |	fail



# DISCLAIMER
```
TO BE USED FOR EDUCATIONAL PURPOSES ONLY
```
The use of the artiPHISHial is COMPLETE RESPONSIBILITY of the END-USER. Developers assume NO liability and are NOT responsible for any misuse or damage caused by this program.
