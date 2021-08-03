NoMoreNotes
=================================================

The next step in note software: sit back, relax, and emjoy the AI doing it for you!

[![License](https://img.shields.io/badge/License-Apache%202.0-lightgray.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Latest release](https://img.shields.io/badge/Release-Latest-orange.svg?style=flat-square)](https://github.com/flancast90/NoMoreNotes/releases)


Table of contents
-----------------

* [Introduction](#introduction)
* [Installation](#installation)
* [Getting help](#getting-help)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgments](#acknowledgments)


Introduction
------------

NoMoreNotes is an application of the Google Cloud Speech-to-Text AI, with some handy python code wrapping it (as well as a great developer :)). The program ensures maximum storage-space kept by optimizing code, as well as deleting unused program-files it creates, and organizing files for user-convenience. In addition to this, NoMoreNotes allows ease-of-access to EVERY user by outputting the notes it creates to a USER-NAMED html file which ANY web-browser can open and run!


Installation
------------

As-stated, NoMoreNotes is reliant on several well-known and documented external libraries, including Google Speech-to-Text. A list to any of these services can be found below, as well as links to their documentation pages. Any questions about these libraries should be routed to their respective dev teams.

1. To get started with NoMoreNotes, first make sure Python is downloaded as per https://www.python.org/downloads/, and then download PIP [here](https://pip.pypa.io/en/stable/cli/pip_download/)
2. Next, make sure that the necessary libraries are installed using Pip
```bash
pip install speech_recognition
pip install pyaudio
pip install tqdm
pip install datetime
```
3. Once these libraries are downloaded, start Pythune as follows:
```bash
cd path/to/NoMoreNotes-main
cd src
python NoMoreNotes.py
```


Getting help
------------

Hopefully you don't need this section, but in case something goes wrong, feel free to drop me an email at ```flancast90@gmail.com```, or [open a new issue on this GitHub Repo](https://github.com/flancast90/NoMoreNotes/issues/new). I will do my best to respond ASAP to these problems!


Contributing
------------

Contributions to this file can be done as a [Pull Request](https://github.com/flancast90/NoMoreNotes/compare), or by shooting an email to ```flancast90@gmail.com```. If anyone would like to be added as a Collaborator to this repo, please send an email to the same address given above. 


License
-------

This README file is distributed under the terms of the [Apache 2.0 License](https://opensource.org/licenses/Apache-2.0). The license applies to this file and other files in the [GitHub repository](http://github.com/flancast90/NoMoreNotes) hosting this file.


Acknowledgments
---------------

Thanks to everyone in the list below! Each of them helped me on my journey to create NoMoreNotes, and their knowledge and expertise in the subject of AI, text-to-speech, or programming, respectively, taught me something new that is now implemented in NoMoreNotes. You all are awesome!

* https://github.com/badges/shields
* https://github.com/mhucka/readmine/
* https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
* https://pypi.org/project/SpeechRecognition/
* http://people.csail.mit.edu/hubert/pyaudio/
