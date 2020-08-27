# versioning_task


The task is to design and implement a versioning mechanism for python packages.

It includes in-house packages that use 3rd party packages.

For this scope, lets say no prod/staging/dev etc… 

 

Some context and details:

We are working on python 3.6+

In python, packages are managed by app called pip, and requirements are managed by a requirements file (requirements.txt)

In addition, there is newer package version manager called pipenv that simulates a node/npm model of package versioning.

 

The purpose of the task is to implement and write some code of a tool that will utilize package versioning in order to allow safe CICD flow (specifically the part of building a python package and installing it.

For example:

 

We have 3 packages –

P1:

In house packages required (dependency): None

External packages required: requests

P2:

In house: P1

External: boto3

P3: 

In house: P2

External: None
 

## In addition we have 2 services:
S1:

Should install P2 package as the application


S2:

Should install P3 package as the application
 

 

Please design in detail the workflow of installation process, please take in mind the following and address them:

How to install dependencies of decencies 
How to avoid conflicts between versions
How to be able deploy fast but without errors (for example, if P1 changes, should we build and install both P2, P3?)
What will be the version number? 
How versions will be handled?
 

Please write code that will implement the base of your design. It should be simple and its ok if it wont cover all aspects. Only the core logic.

If you make any assumptions, please state them.

I’m here for any question or concern.

Thanks
