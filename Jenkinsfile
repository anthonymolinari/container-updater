pipeline {
    agent any
    environment {
        DOCKERHUB_USERNAME = credentials("DOCKERHUB_USERNAME")
        DOCKERHUB_TOKEN    = credentials("DOCKERHUB_TOKEN")
        TF_VAR_docker_host = credentials("DOCKER_HOST") 
        TF_VAR_config_path = '/mnt/ssd-500GB/docker/container-updater/config'
        TF_VAR_logs_path   = '/mnt/ssd-500GB/docker/container-updater/logs'
    }
    stages {
        stage('run dagger ci') {
            steps {
                script {
                    sh 'pip install -r ./dagger/requirements.txt'

                    if ("${env.BRANCH_NAME}" == "main") {
                        sh 'python ./dagger/pipeline.py --tag=latest'
                    } else {
                        sh 'python ./dagger/pipeline.py --tag=dev'
                    }
                }   
            }
        }
        stage('deploy w/ terraform') {
            when {
                environment(name: 'BRANCH_NAME', value: 'main')
            }
            steps {
                sh '''
                    cd deploy
                    terraform init
                    terraform apply -auto-approve
                '''
            }
        }
    }
}
