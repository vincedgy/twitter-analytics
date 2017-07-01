# ```Python Twitter streams to AWS Kinesis```

## Objectives

Develop a Python program that collects tweets from twitter API (Streams) and push them into Kinesis for further analysis using AWS tools. 
Tweets are stored into record, saved in files into an S3 bucket.
S3 will be used a our datalake for future usage of Athena or RedShift Spectrum or any other analytic that can read on S3
We also use a DynamodDB table for file indexation and twittos (user who tweets)

Python program will use AWS assets such as S3, DynamoDB, Kinesis etc...
This mean that you'll need to have ans AWS API Key and Secret Key (create from your AWS account on AWS IAM) and configure it as a default profile (or a specific profile, as you wish).

:shipit:

![Schema](https://cdn-images-1.medium.com/max/1600/0*JzY8ZMS9r_JzxIpy.png)

### Development environment 

#### Virtualenv for python

This projetct use Python 2.7 for this current release.
Use virtualenv for your Python developmement and libraries installation

```
virtualenv -p python venv
source ./venv/bin/activate
pip install -r requirements.txt
``` 

#### DynamoDB installed and used locally

By the way, we'll also install DynamoDB locally in order to test our program more easily 
You'll need to download
[https://s3.eu-central-1.amazonaws.com/dynamodb-local-frankfurt/dynamodb_local_latest.tar.gz]

#### Lambda 

We will also push the program that will run python program in an AWS lambda.

For this sake, during developement, we will use a framework for developping lambda localy : lambda-toolkit
[ https://github.com/lucioveloso/lambda-toolkit ]

For Lambda running (production) environnement we will need to push a deployement package will all dependencies using this guide [http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html]


#### IAM Role

*IAM Role* is necessary EC2 you'll need to create a IAM Role in order to give access to EC2 to Kinesis, S3, DynamoDB etc...

## Installation

You'll need to install libraries which are located in the ```requirements.txt``` file

```
pip install -r requirements.txt
python install.py
```

### Twitter credentials

Twitter credentials are stored in a file named 'twitterCreds.py' that is used during program lauching.

This is its typical content with which you need to replace place holders with your credentials.

```python
consumer_key = "XXXxxxXXXxxxXXXX"
consumer_secret = "XXXxxxXXXxxxXXXX"
access_token_key = "XXXxxxXXXxxxXXXX"
access_token_secret = "XXXxxxXXXxxxXXXX"
``` 

## Running locally

Locally (or on any VM, EC2, Docker VM etc...) it is simple as launching twitter-kinesis.py

```
python twitter-kinesis.py
```

/!\ Warning : if you decide to run the python script on EC2 or Docker VM executed on EC2 or ECS you'll need to create the appropriate IAM Role, allowing the usage of S3, DynamodDB and Kinesis to the program

## References

Check out this page which was very useful[https://blog.insightdatascience.com/getting-started-with-aws-serverless-architecture-tutorial-on-kinesis-and-dynamodb-using-twitter-38a1352ca16d

## TODO
- [X] Kinesis, S3, DynamoDB creation script
- [ ] Lambda Python package creation script
- [ ] Program development and testing