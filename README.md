# make_package

This repo tells us how to create a package in Python.
let's assume we have a setup.py in our project. Please have a look on how to create a setup.py or just look at my setup.py in case you just want to get started.

Move at the top level directory of your project, where you setup.py is present.
Create a virtual_env of your choice by executing "virtualenv $VirtualenvName"
then run "source $VirtualenvName/bin/active" to activate the virtual environment.
Run "pip install -e . "
And here you go, you are ready with your command line package, accessible inside your virtual environment.

For simple example, clone my repo.
and then perform the simple steps.
1) virtualenv make_package
2) source make_package/bin/active
3) Run pip install -e .

Now you are all setup.

  Try command : one_script
  
