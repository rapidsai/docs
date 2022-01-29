pipeline {
  agent any
  stages {
    stage("Build") {
      steps {
        sh "echo 'hello, world'"
        sh "sleep 20s"
        sh "exit 1"
      }
    }
  }
}
