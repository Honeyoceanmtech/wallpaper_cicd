pipeline {
  agent any
  stages {
    stage('Git Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/Honeyoceanmtech/simple_project.git'
      }
    }
    stage('Deploy')
    {
      steps {
        echo "deploying the application wallpaper_cicd ...."
        sh " docker-compose up"
      }
    }
  }
}
