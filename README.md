# artiPHISHial
![Artiphishial_75](https://github.com/gingapower/artiPHISHial/assets/87360317/013e1409-b728-428f-855c-48ca27d5a1eb)

Automatic Login Page Generator for Phishing purposes. 
this tool sets up a phishing mail with Flask in about 2 minutes. The tool clones the original page, inserts all necessary components, and sets up the Flaskapp.

# Tool
![image](https://github.com/gingapower/artiPHISHial/assets/87360317/bbd2f2ac-e963-472a-ac42-a7011eb1dc0d)

you have the possibility to download an executable file to launch the phishing webpage on windows:

![image](https://github.com/gingapower/artiPHISHial/assets/87360317/56701c3c-a23c-451f-97d3-c45a94858596)

You can also just download the cloned files:

![image](https://github.com/gingapower/artiPHISHial/assets/87360317/0cf27131-c2a7-4858-a27d-1052017f208a)


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
