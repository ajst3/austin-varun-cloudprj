# Project Option 1 Austin Tercha, Varun Devulapalli  

## Dependencies:  
  - Docker  
  - Docker-Compose (Requires version 3 at least)
  - Way to allow docker containers to run GUI applications:  
    - XQuartz (for Mac OS)  
    - Xming (for Windows)
        - must have Xming configured properly
    - docker-compose file already accounts for Linux  
  - Adequate space to have application on machine  

## Steps to Run Overall Application:  
  1. Meet all of the dependencies  
  2. Download this repository  
  3. Open a terminal  
  4. Enter the correct directory  
    - Windows/MAC: enter directory named src/windows_yaml  
    - Linux: enter directory named src
  5. Run the command: docker-compose up  
    - The docker-compose.yml enables all of our created images to be pulled
    from dockerhub  
  6. Main GUI will automatically start running, which contains the buttons for
  each application  
    - Applications can be slow and buttons can take a long time to execute, if
    there is an issue press the button again  
  7. See instructions below to run each application  

## Steps to Run Applications  
#### RStudio  
  1. Presss button labeled Rstudio  
  2. Application will open  
    - RStudio does not support X11 forwarding in general, so there may be an
    issue running RStudio using Xming
#### Spyder  
  1. Press button labeled Spyder  
  2. Application will open  
#### IBM SAS  
  1. Press button labeled IBM SAS    
  2. Firefox will open with IBM SAS login page loaded  
#### Git  
  1. Press button that is labeled Git  
  2. A shell will open where you can type git commands  
#### Jupyter Notebook  
  1. Press button labeled Jupyter Notebook  
  2. Firefox will open to Jupyter Notebook page that asks for a token  
  3. This token is in the output earlier in the terminal under the
  application jserver    
#### Orange  
  1. Press button labeled Orange  
  2. Application will open  
#### Atom IDE  
  1. Press button labeled Atom IDE  
  2. Terminal will open  
  3. Type atom into terminal and press enter  
  4. Application will open  
    - Similarly to RStudio, Xming may not run Atom IDE  
    - You may need another X11 forwarding application  
#### Apache Hadoop  
  1. Press button labeled Apache Hadoop  
  2. Terminal will open
  3. run command: cd $HADOOP_PREFIX  
  4. to run hadoop commands: bin/hadoop <hadoop command>  
#### Apache Spark  
  1. Press button labeled Apache Spark  
  2. terminal will open  
  3. enter the command spark-shell to open a spark shell or run an execution
  in the terminal such as /opt/bitnami/spark/bin/./run-example SparkPi  
#### Tableau  
  1. Press button labeled Tableau  
  2. Firefox browser will open with tableau online login page loaded  
#### Sonar Qube and Binaries  
  1. Press button labeled Sonar Qube and Binaries  
  2. terminal will open  
  3. to run sonar scanner: sonar-scanner  
    - to scan a specific dir, -Dsonar.projectBaseDir=/path_you_want_to_scan
#### Tensorflow  
  1. Press button labeled Tensorflow  
  2. terminal will open with Tensorflow shell  
#### Mardown  
  1. Press button labeled Markdown  
  2. The application retext will open  
    - retext is a Markdown text editor to write and view Markdown files
