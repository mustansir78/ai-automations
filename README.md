# General Setup Guidelines

This document serves as a guide to setting up the environment needed to run the AI automations in this repository.

Follow the instructions carefully. The guide is targeted to install the AI automation toolkit locally on a Mac OS X environment, but the commands are similar for other platforms as well.

## Clone this Git Repo
Open your terminal, change to the folder where you want to clone this repo and run:
```
git clone git@github.com:mustansir78/ai-automations.git
```
*Note: If you do not have Git installed, then install it from https://git-scm.com/downloads*

## Install Docker
We will be using containerized approach of setting up the AI solutions. This approach avoid issues arising on invdividual systems due to different configurations.

Docker provides a consistent operating environment that is exactly the same on every computer it runs on.

Install Docker from https://www.docker.com/ and select your target OS.
Follow the instructions for your specific OS.

## Install AI Automation Tookit
Once docker is installed, visit https://github.com/n8n-io/n8n-hosting/tree/main/docker-compose/withPostgres and follow the instructions on the page to install the AI Automation Toolkit locally.

## Setting up Python environment
Once your Docker environment is up and running properly, follow the instructions below to setup your Python local environment.

1. Install **Python 3.12** from https://www.python.org/downloads/release/python-3129/
2. Once Python is installed, open the terminal.
3. Change to the folder where you have downloaded this Git repo and run
```
python3 -m venv .venv

pip install -r requirements.txt
```


## Running the automations
Each automation is organized inside it's own folder. The instructions specific to running each automation is in their respective Readme.md file.

# Support and Assistance
In case you need assistance to setup the environment on your local machine or on your cloud server, you can reach out to me on the following:
|Platform|Link|
|---|---|
|**LinkedIn**|https://www.linkedin.com/in/mustansirhusain|
|**Facebook**|https://www.facebook.com/mustansir.husain|

I will provide an hour's worth of support for **USD 50.00** to setup the entire automation environment for you. You can use this environment not just for the AI automations here, but also for other N8N automations you create yourself later on.