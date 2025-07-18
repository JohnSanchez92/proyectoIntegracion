pipeline {
    agent any
    environment{
        DOCKER_HOST = 'unix:///var/run/docker.sock'
        CODECOV_TOKEN = credentials('CODECOV_TOKEN')
    }

    stages {
        stage('Clonar repositorio') {
            steps {
                echo 'Código clonado por Jenkins automáticamente.'
            }
        }

        stage('Construir contenedores') {
            steps {
                sh 'docker-compose build --no-cache'
            }
        }

        stage('Verificar archivos en contenedor') {
            steps {
                sh 'docker-compose exec --rm frontend ls -R /usr/share/nginx/html'
            }
        }

        stage('Pruebas unitarias backend') {
            steps {
                sh 'docker-compose exec --rm backend pytest --cov=app --cov-report=xml'
            }
        }

        stage('Download Codecov CLI') {
            steps {
                sh '''
                curl -Os https://uploader.codecov.io/latest/linux/codecov
                chmod +x codecov
                '''
            }
        }

        stage('Upload to Codecov') {
            steps {
                sh './codecov --token=$CODECOV_TOKEN --file=coverage.xml --flags=unittests'
            }
        }

        stage('Desplegar') {
            when {
                expression { currentBuild.currentResult == 'SUCCESS' }
            }
            steps {
                echo 'Desplegando aplicación...'
            }
        }
    }

    post {
        always {
            echo "Limpieza de contenedores temporales si es necesario."
            sh 'docker-compose down --volumes --remove-orphans || true'
        }
    }
}
