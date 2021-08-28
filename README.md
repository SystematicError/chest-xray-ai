<h2 align="center">Blaze</h2>

**Note:** This project is just a proof of concept prototype and should not be used for Medical use.

&nbsp;

### What is Blaze?
Blaze is a webapp designed to predict the probabilities of different pathologies visible under a human chest xray. It aims to co-pilot and assist medical professionals to diagnose patients accurately and efficiently. This project was made as a submission for a competition and is based on the [torchxrayvision](https://pypi.org/project/torchxrayvision/) library.

&nbsp;

### How can I use it?
Firstly, you need to make sure you have installed and started up the server. After you start it you get one of two URL's, which will look like the following: `http://0.0.0.0:13520` or something similar to `http://90eu-285-11-20-34.ngrok.io`. After that, you can simply visit the url to use the webapp. Note that the first type of URL is only accessible from the host device.

&nbsp;

### Downloading

#### Downloading without python
To get a pre-compiled version, you can visit the [releases](https://github.com/SystematicError/Chest-Xray-AI/releases) section and download the latest version. The rest of the instructions will be given in the following sections. For MacOS, you will need to download as a python project, this is due to Apple only allowing the execution of apps compiled on Apple Hardware.


#### Downloading as python project
Firstly, you need to install python, you can get this from the [python website](https://www.python.org/downloads/release/python-396/). When running the installer, please check the "Add to PATH" option, otherwise python will not work. You may also install python from a commandline package manager (if you are make sure to install pip as well)

If you have the [Git Version Control](https://git-scm.com) software installed then you can you can type the following in your terminal:
```
git clone https://github.com/SystematicError/Chest-Xray-AI
```
If you do not have git installed or wish to do it in a more graphical way, then you can also get a zip file containing the project from [here](https://github.com/SystematicError/Chest-Xray-AI/archive/refs/heads/master.zip); afterwards extract this zip file.

Now, open your terminal, and navigate to the extracted directory using command prompt or your appropriate terminal ([here](https://www.watchingthenet.com/how-to-navigate-through-folders-when-using-windows-command-prompt.html) you can find a guide for windows or go [here](https://www.lifewire.com/linux-commands-for-navigating-file-system-4027320) for a Linux/MacOS guide)

When you have navigated to the right directory, type the following; it may take a minute to install depending on your internet speed:

```
pip install -r requirements.txt
```

&nbsp;

### Starting the server
When starting the server for the first time, it will download the AI Models and generate some cache. There are 2 ways you can start the server:

#### Starting the server graphically
To open it graphically, you can open it via your file explorer. Navigate to the project folder and double click the `main.py` file (it could also be `main.exe` or simply `main`), make sure that when you double click that the program it opens with python and not some text editor. A terminal window should pop up if everything is done correct. If the window opens and quickly closes that means there is some error, try running the server via commandline to find the root of the issue.

####  Starting the server via commandline
Firstly open your terminal of choice and navigate to the project directory, instructions on how to do so is given in the "Downloading as python project" section.

If you installed as a python project, then run the following:
```
python main.py
```

Otherwise, run the these commands instead:

##### Windows:
```
main.exe
```

##### Linux:
```
./main
```

If all goes well you should see something like this:

```
[xray] Importing libraries
[xray] Loading model
[server] Running locally at http://0.0.0.0:13520
[tunnel] Created tunnel at http://90eu-285-11-20-34.ngrok.io
```

The first URL, `http://0.0.0.0:13520` is your local URL, you can only visit this website from the computer the server is running from. This URL will always be the same.

The next URL, `http://90eu-285-11-20-34.ngrok.io` is your public URL, this can be visited from any device as long as the server is running. This URL will change whenever you restart the server.

**Note:** You can press `Ctrl+C` in the terminal to stop the server

&nbsp;

### Troubleshooting
If you face an error while launching the server, try re-doing the command, if there is still an issue please create a issue on our [bug tracker](https://github.com/SystematicError/Chest-Xray-AI/issues).