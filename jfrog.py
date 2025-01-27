
#!/usr/bin/env python3

import  requests
import  subprocess

def jfrogUpload() :
    url = 'http://34.204.61.228:8082/artifactory/example-repo-local/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    file_path = '/var/lib/jenkins/workspace/Jfrog/target/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'
    username = 'admin'
    password = 'Surya#dad1'

    with open(file_path, 'rb') as file:
        response = requests.put(url, auth=(username, password), data=file)

    if response.status_code == 201:
        print("\nPUT request was successful")
    else:
        print("PUT request failed with status code(response.status_code)")
        print("response content:")
        print(response.text)
def mvnBuild() :
    maven_command = "mvn clean install -DskipTests"

    try:
        subprocess.run(maven_command, check=True, shell=True)
        print("\nMaven build completed successfully")
    except subprocess.CalledProcessError as e:
        print("Error: Maven build failed with exit code {e.returncode}")

def main():
    jfrogUpload()

if __name__ == "__main__":
    main()                
