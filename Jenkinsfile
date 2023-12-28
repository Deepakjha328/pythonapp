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
                    sh 'docker tag docker-jenkins-python:${buildNUMBER} samba642/docker-jenkins-python:${buildNUMBER}'
                }
            }
        }
        
        stage ('Docker hub login') {
            
            steps {
                
                script {
                    
                    withCredentials([string(credentialsId: 'Docker_Creditial', variable: 'Docker_PWD')]) {
                        
                        sh 'docker login -u samba642 -p ${Docker_PWD}'
                    }
                }
            }
        }
        
        stage ('Push image Docker-Hub') {
            
            steps {
                
                script {
                    
                    sh 'docker push samba642/docker-jenkins-python:${buildNUMBER}'
                }
            }
        }
        
        stage ('Deploy') {
            
            steps {
                
                script {
                    
                    sh 'docker rm -f docker-jenkins-python || true'
                    sh 'docker run -d -it --name docker-jenkins-python -p 3333:3333 samba642/docker-jenkins-python:${buildNUMBER}'
                }
            }
        }
    }
}
