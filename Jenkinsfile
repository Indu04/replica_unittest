pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'dir'
                bat 'pep8 . > peplint.log'
                step([
                        $class: 'WarningsPublisher',
                        parserConfigurations: [[
                            parserName: 'Pep8',
                            pattern: 'peplint.log']],
                        unstableTotalAll           : '0',
                        usePreviousBuildAsReference: true
                    ])
                bat 'echo "BUILD END"'
            }
        }
    }
}
