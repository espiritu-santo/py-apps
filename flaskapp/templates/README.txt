1.From a terminal such as BASH, run the following commands:
(Note: the paths in the python scripts are set to ~/Downloads/py-apps-main/flaskapp/ extracting the flaskapp directory somewhere other than your Downloads folder will require additional setup)

	$ python --version (Where to download the latest version of python for your OS: https://realpython.com/installing-python/)
	$ python3 -m venv /path/to/flaskapp/ (setup a virtual environment)
	$ source venv/bin/activate (run the virtual environment)
	$ pip install pandas matplotlib PyQt6 scipy (install package dependencies separately)
	$ pip freeze (check that all of the depencies were installed)
	$ export PYTHONPATH=/path/to/venv/.../site-packages/ (tell python where to find the modules for import)
	$ env | grep -i python (check the python environment variables)

2.CD into the flaskapp directory and enter "flask run" at the command prompt.
3.This will start the flask server on the localhost:port.
4.Right-click on the ip address in the terminal to open the link in a web browser. Alternatively you can enter the ip address into the web browser address bar.
5.The Data Explorer page is where you will select your csv file to upload. The data must be in xyz format and the file type must be a comma delimited file.
6.There is an example dataset, "YB_01_YB1_20221115_CS.csv" in the uploads folder.
7.Once you click the upload file button at the bottom of the page you will be redirected. If the success page does not load it is likely because the file is not a csv file.
8.Click the "View Instructions" link to continue.
9.The success page will load. Follow the instructions on the webpage to start the python interpreter.
10.To get out of the python interpreter type "quit()" to return to the terminal.
11.Run the flask app again in the terminal (go back to step 2 above). This time enter coordinates into the textbox to plot a profile.

Thanks for downloading the flaskapp! 
