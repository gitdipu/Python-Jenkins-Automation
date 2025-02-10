import requests
from requests.auth import HTTPBasicAuth
import time
import os
from dotenv import find_dotenv, load_dotenv

#find .env automatically by walkng up directories untill it's found
dotenv_path = find_dotenv()

#load the entries as an env variables
load_dotenv(dotenv_path)

# Configuration
JENKINS_URL = os.getenv('JENKINS_URL')
JOB_NAME = os.getenv('JOB_NAME')
JOB_TOKEN = os.getenv('JOB_TOKEN')
USER = os.getenv('USER')
USER_API_TOKEN = os.getenv('USER_API_TOKEN')

# Trigger the Jenkins job
try:
    url = f"{JENKINS_URL}/job/{JOB_NAME}/build?token={JOB_TOKEN}"
    response = requests.post(url, auth=(USER, USER_API_TOKEN))
    #response = requests.post(jenkins_url, auth=HTTPBasicAuth(username, token))
    time.sleep(10)
    if response.status_code == 201:
        print("Job triggered successfully!")
    else:
        print(f"Failed to trigger job: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

''' The HTTP 401 Unauthorized error indicates that the authentication credentials you're using to 

trigger the Jenkins job are incorrect or that the job is not configured to accept the token 

provided. Let's go through the necessary steps to troubleshoot and resolve this issue. 
 
### Steps to Resolve the 401 Unauthorized Error 


###Failed to trigger job: 403
Answer :

Share icon
The HTTP 403 Forbidden error indicates that the server understood the request but refuses to 

authorize it. This can happen for several reasons when trying to trigger a Jenkins job. Here are 

some steps to troubleshoot and resolve the issue: '''