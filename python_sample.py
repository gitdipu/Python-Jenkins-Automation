#1) REST API Automation Using requests to interact with a REST API.

import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Failed to fetch data")

#2) Web Scraping Using BeautifulSoup to extract titles from a webpage.

import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

titles = soup.find_all("h1")
for title in titles:
    print(title.get_text())

#3) SSH Connection Using paramiko to connect to a remote server
import paramiko

hostname = "your.server.com"
username = "your_user"
password = "your_password"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname, username=username, password=password)

stdin, stdout, stderr = client.exec_command("ls -l")
print(stdout.read().decode())

client.close()

#4) Docker Containers Lifecycle Handling Using docker Python SDK to list running containers.

import docker

client = docker.from_env()

# List all containers
for container in client.containers.list():
    print(container.name, container.status)

# Create and run a new container
container = client.containers.run("nginx", detach=True)
print("Started container:", container.id)

#5) GitHub Automation Using PyGitHub to create a new repository.

from github import Github

token = "your_github_token"
g = Github(token)

user = g.get_user()
repo = user.create_repo("my-new-repo")
print("Created repo:", repo.full_name)

#6) Database Automation Using sqlite3 to interact with an SQLite database.

import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
conn.commit()

cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conn.close()

#7) CPU and Memory Utilization Check Using psutil to check system resources.

import psutil

print("CPU Usage:", psutil.cpu_percent(interval=1), "%")
print("Memory Usage:", psutil.virtual_memory().percent, "%")

#8) CI/CD Automation Triggering a Jenkins job using requests.

import requests

jenkins_url = "http://jenkins.example.com/job/my-job/build"
headers = {"Authorization": "Bearer your_api_token"}

response = requests.post(jenkins_url, headers=headers)
print("Triggered job:", response.status_code)

#9) AWS Boto3 Automation Creating an S3 bucket.

import boto3

s3 = boto3.client("s3")
bucket_name = "my-bucket-12345"

s3.create_bucket(Bucket=bucket_name)
print("Bucket created:", bucket_name)

#11) AWS Boto3 Automation (EC2 Example) Starting an EC2 instance.
import boto3

ec2 = boto3.client("ec2")
response = ec2.run_instances(
    ImageId="ami-12345678",
    InstanceType="t2.micro",
    MinCount=1,
    MaxCount=1
)
print("Instance started:", response["Instances"][0]["InstanceId"])

#12) Terraform Automation Applying a Terraform configuration.

import subprocess

subprocess.run(["terraform", "init"])
subprocess.run(["terraform", "apply", "-auto-approve"])

#13) Flask-Based Application A simple Flask API.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)

#14) Cache Automation Using functools.lru_cache for function caching.

from functools import lru_cache

@lru_cache(maxsize=5)
def expensive_function(x):
    print(f"Calculating {x}...")
    return x * x

print(expensive_function(2))
print(expensive_function(2))  # Cached

#15) Web Scraping (Selenium) Using Selenium to scrape dynamic content

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")

print(driver.title)
driver.quit()