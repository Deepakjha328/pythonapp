pipeline {
    
    environment {
        
        buildNUMBER = currentBuild.getNumber()
    }
    
    agent any
    
    stages {
        
        stage ('clone from git-hub') {
            
            steps {
                
                script {
                    
                    checkout scmGit(branches: [[name: '*/main']], 
                    extensions: [], 
                    userRemoteConfigs: [[credentialsId: 'jenkins', 
                    url: 'https://github.com/Deepakjha328/pythonapp.git']])
                }
            }
        }
        
        stage ('Build docker image') {
            
            steps {
                
                script {
                    
                    sh 'docker build -t docker-jenkins-python:${buildNUMBER} .'
                    sh 'docker tag docker-jenkins-python:${buildNUMBER} jenkin21/pythonapp:${buildNUMBER}'
                }
            }
        }
        
        stage ('Docker hub login') {
            
            steps {
                
                script {
                    
                    withCredentials([string(credentialsId: 'Docker_Creditial', variable: 'Docker_PWD')]) {
                        
                        sh 'docker login -u jenkin21 -p ${Docker_PWD}'
                    }
                }
            }
        }
        
        stage ('Push image Docker-Hub') {
            
            steps {
                
                script {
                    
                    sh 'docker push jenkin21/pythonapp:${buildNUMBER}'
                }
            }
        }
        
        stage ('Deploy') {
            
            steps {
                
                script {
                    
                    sh 'docker rm -f docker-jenkins-python || true'
                    sh 'docker run -d -it --name docker-jenkins-python -p 5000:5000 jenkin21/pythonapp:${buildNUMBER}'
                }
            }
        }
    }
}
