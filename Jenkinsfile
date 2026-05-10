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
                script {
                    echo "Esperando a que la app responda..."
                    // Esperamos unos segundos para que Flask arranque
                    sleep 5 
                    
                    // Intentamos conectar hasta 5 veces
                    def response = sh(script: 'curl -s -o /dev/null -w "%{http_code}" http://localhost:5000', returnStdout: true).trim()
                    
                    if (response == "200") {
                        echo "¡Éxito! La aplicación respondió con HTTP 200"
                    } else {
                        echo "Error: La aplicación respondió con código ${response}"
                        error "Fallo en el Health Check"
                    }
                }
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