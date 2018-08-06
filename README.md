## Project: inova-log ##

Log service module created to integrate with a set of microservices deloped by CPS Inova.

(_in construction_)

Instructions to build the project:
*  Creating a new virtual environment (venv) to run with Python 3
    ```bash
    python3 -m venv venv
    ```
or
    ```bash
    virtualenv -p python3 venv
    ```
* Accessing virtual environment **venv**
    ```bash
    source venv/bin/activate
    ```
Updating "pip" tool
    ```bash
    pip install --upgrade pip
    ```
* Exiting of virtual environment **venv**
    ```bash
    deactivate
    ```
* Installing PyBuilder - Versioned project
    ```bash
    git clone https://github.com/cpsinova/inova-log.git
    cd inova-log
    python3 -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install pybuilder
    pyb install_dependencies
    pyb
    After: verifify if target/dist/inova-log* was created
    ```

### Optional instructions - Use if necessary: ###

* Creating a new project structure using PyBuilder
    ```bash
    pip intall pybuilder
    pyb --start-project
    pyb install_dependencies publish
    After: verifify if target/dist/inova-log* was created
    
    ```
* Updating all packages installed in "venv"
 	1. Access **venv**
 	2. Execute: 
    ```bash 
    pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U 
    ```
* Uploading the project do PyPi respository
    ```bash
    pip install twine
    pyb
    twine upload -r pypi <path and name of the package tar.gz created into the TARGET folder>
    ```
* Run the project
    * Execute:
    ```bash
    ./runserver.sh
    ```
    * To test the project, access the URL _http://localhost:8080/log_. The response will be:
    ```json
    {
        "message": "Log queried with success",
        "system": "pyetl-inova",
        "source_host": "172.45.67.89",
        "target_host": "192.168.9.2",
        "datetime": "2018-08-06 01:37:23.327827"
    }
    ```
   