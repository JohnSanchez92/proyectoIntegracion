pipeline {
    agent any
    environment{
        DOCKER_HOST = 'unix:///var/run/docker.sock'
    }

    stages {
        stage('Clonar repositorio') {
            steps {
                echo 'Código clonado por Jenkins automáticamente.'
            }
        }

        stage('Construir imágenes Docker') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Levantar contenedores') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }

    post {
        always {
            echo 'Pipeline terminado.'
        }
    }
}
