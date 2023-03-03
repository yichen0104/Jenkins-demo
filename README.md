# Steps for Jenkins installation:

1. Ssh into the virtual machine <username>@<ip-address>
	
	ssh seaidemo23@128.2.24.106

Skip step 2, 3 for the recitation demo. Already setup.

>2. Install Java Jdk
>	
>	sudo apt-get install java-1.8.0-openjdk
>	
>	java -version
>
>3. Install jenkins using a docker image
>	
>	docker pull jenkins/jenkins
>
>4. Run the war file on port 8089
>	
>	java -jar /usr/share/java/jenkins.war --httpPort=8089
>	
>		Message: Jenkins is fully up and running

5. Open http://128.2.24.106:8081/

6. Login 
	
	Username: admin
	
	Password: seaidemo23

7. Click on New Item

8. Add name, select Freestyle project and click OK
	
9. Configue the project - Add a description
	
10. In Source Code Management, select and add repository URL to link to GitHub
	
11. Under Branches to build, in Branch Specifier replace */master with */main
	
12. Under Build Steps, click on Add Build Steps dropdown and select Execute shell

13. In commands, paste the following commands to run pytest
	
>pip install coverage
>
>coverage run -m pytest
>	
>coverage report
	
