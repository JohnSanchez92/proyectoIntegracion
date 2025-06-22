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

        stage('Construir contenedores') {
            steps {
                sh 'docker-compose build --no-cache'
            }
        }

        stage('Verificar archivos en contenedor') {
            steps {
                sh 'docker-compose run --rm frontend ls -R /usr/share/nginx/html'
            }
        }

        stage('Pruebas unitarias backend') {
            steps {
                // Limpia red antigua para evitar conflicto
                sh 'docker network rm integracion-continua_default || true'
                // Ejecuta pruebas
                sh 'docker-compose run --rm backend pytest --cov=app --cov-report=term-missing'
            }
        }

        stage('Subir cobertura a Codecov') {
            environment {
                CODECOV_TOKEN = credentials('CODECOV_TOKEN')
            }
            steps {
                sh '''
                    docker-compose run --rm backend sh -c "
                        curl -Os https://uploader.codecov.io/latest/linux/codecov &&
                        chmod +x codecov &&
                        ./codecov
                    "
                '''
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
