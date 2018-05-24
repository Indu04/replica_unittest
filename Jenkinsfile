pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                bat 'dir'
                step([
                        $class: 'WarningsPublisher',
                        parserConfigurations: [[
                            parserName: 'PyLint',
                            pattern: 'lint.log']],
                        unstableTotalAll           : '0',
                        usePreviousBuildAsReference: true
                    ])
                bat 'pylint src/source_code > lint.log'
                bat 'echo "BUILD END"'
            }
        }
    }
}
