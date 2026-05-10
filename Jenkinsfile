pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Probar Docker') {
            steps {
                sh 'docker --version'
            }
        }

        stage('Construir Imagen') {
            steps {
                sh 'docker build -t flask-app:latest .'
            }
        }

        stage('Desplegar') {
            steps {
                sh 'docker compose up --detach'
                echo "Despliegue completado desde GitHub"
            }
        }
    }
    
    post {
        always {
            echo "Limpiando espacio de trabajo..."
            deleteDir()
        }
    }
}