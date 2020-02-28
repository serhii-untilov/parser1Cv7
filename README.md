How to parse files
==================

1. Download the <a href="https://drive.google.com/open?id=1irf-ojO_RuTRQigDempJp3J2KxSRkoeF" download target="_blank">parser1Cv7.exe</a>
2. Copy source DBF files in the same directory.
3. Run the [parser1Cv7.exe](https://drive.google.com/open?id=1irf-ojO_RuTRQigDempJp3J2KxSRkoeF)

Development
===========
1.  Download and install git.
    ```
    https://git-scm.com/downloads
    ```
2.  Choose your projects directory (like C:/Users/YourName/projects)   
3.  Clone the github project 'sergey-untilov/parser1Cv7'
    ```
    git clone https://github.com/sergey-untilov/parser1Cv7.git
    ```
4.  Choose project directory
    ```
    cd parser1Cv7
    ```
5.  Download and install Python 2.7.17.
    ```
    https://www.python.org/downloads/release/python-2717
    ```
6.  Install virtualenv.
    ```
    pip install virtualenv
    ```
7.  Setup a virtual environment for Python.
    ```
    virtualenv env
    ```
8.  Activate virtual environment.
    ```
    activate.cmd
    ```
9.  Copy source files into parser1Cv7\inp\ directory.
10. Run the programm.
    ```
    run.cmd
    ```
11. Output files will be in outp\ directory.

12. To make executable file for Windows run
    ```
    build.cmd
    ```
    That makes the dist\parser1Cv7.exe file.
