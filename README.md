<h2 align="center">Blaze</h2>

**Note:** This project is just a proof of concept prototype and should not be used for Medical use.

&nbsp;

### What is Blaze?
Blaze is a webapp designed to predict the probabilities of different pathologies visible under a human chest xray. It aims to co-pilot and assist medical professionals to diagnose patients accurately and efficiently.

### How can I use it?
Firstly, you need to make sure you have installed and started up the server. After you start it you get one of two URL's, which will look like the following: `http://0.0.0.0:13520` or something similar to `http://90eu-285-11-20-34.ngrok.io`. After that, you can simply visit the url to use the webapp. Note that the first type of URL is only accessible from the host device.

### Downloading (without python)
Unfortunately to build pre-compiled versions for MacOS, you need to compile on Apple Hardware, so only Windows & Linux versions are provided. If you are on MacOS, you can install Python and then run this project, kindly refer to the next section for that. To get a pre-compiled version, you can visit the [releases](https://github.com/SystematicError/Chest-Xray-AI/releases) section and download the latest version. The rest of the instructions will be given in the following sections.


### Downloading (as python project)
Firstly, you need to install python, you can get this from the [python website](https://www.python.org/downloads/release/python-396/). When running the installer, please check the "Add to PATH" option otherwise python will not work. You may also install python from a commandline package manager (if you are make sure to install pip as well)

If you have the [Git Version Control](https://git-scm.com) software installed then you can you can type the following in your terminal:
```
git clone https://github.com/SystematicError/Chest-Xray-AI
```
If you do not have git installed or wish to do it in a more graphical way, then you can also get a zip file containing the project from [here](https://github.com/SystematicError/Chest-Xray-AI/archive/refs/heads/master.zip); afterwards extract this zip file.

Now, open your terminal, and navigate to the extracted directory using command prompt or your appropriate terminal ([here](https://www.watchingthenet.com/how-to-navigate-through-folders-when-using-windows-command-prompt.html) you can find a guide for windows or go [here](https://www.lifewire.com/linux-commands-for-navigating-file-system-4027320) for a Linux/MacOS guide)

When you have navigated to the right directory, type the following:

```
pip install -r requirements.txt
```

It may take a minute to install depending on your wifi speed.