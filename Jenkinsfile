pipeline {
    agent any

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
