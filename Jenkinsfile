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
                sh 'docker compose up -d'
                echo "Despliegue completado desde GitHub"
            }
        }
        stage('Health Check') {
            steps {
                echo "Esperando a que la app responda..."
                sleep 5 
                sh 'curl -f http://localhost:5000'
        }
    }
    
    post {
        always {
            echo "Limpiando espacio de trabajo..."
            deleteDir()
        }
    }
}
}