# Steps for Jenkins installation:

1. Ssh into the virtual machine
	
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

7. Click on New Item on top left corner

8. Add name, select Freestyle project and click OK
	
9. Configue the project - Add a description
	
10. In Source Code Management, select Git and add repository URL to link to GitHub
Note: This repository is public, so it does not require credentials
	
11. Under Branches to build, in Branch Specifier replace */master with */main
		
12. Under Build Steps, click on Add Build Steps dropdown and select Execute shell

13. In commands, paste the following commands to run pytest
	
>pip install coverage
>
>coverage run -m pytest
>	
>coverage report
	
14. Click Save
	
15. Click Build Now from left menu 
	
16. In Build History, green tick shows the build is successful. Click on build for details.
	
17. Click on Console Output from left menu 
	
18. Observe the test cases have passed

# Steps for GitHub Actions:
	
1. Click on Actions tab

2. Click on New workflow and then click on set up a workflow yourself

3. Set up yaml file

4. Green ticks signifies successful build
	

	
