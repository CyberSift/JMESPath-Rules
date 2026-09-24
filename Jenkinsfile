/*
 * Declarative Jenkins pipeline for the CyberSift JMESPath Rules repository.
 * Multibranch Pipeline job — branches + PRs discovered via the GitHub
 * Branch Source plugin (Discover branches, Discover pull requests from origin).
 *
 * The only stage defined is the AI PR review, which runs on pull requests.
 * There are no build, test, or publish stages in this pipeline.
 *
 * Prerequisites on the Jenkins agent:
 *   - Jenkins Global Tool Configuration: NodeJS named "NodeJS-24" (for pi/npm)
 *   - pi CLI installed under ~/.pi/bin (prepended to PATH below)
 *   - gh CLI installed on the agent (for pi-pr-review to post reviews)
 *   - Jenkins credentials:
 *       github-pat    — Username/Password; password is the GitHub PAT (repo scope)
 *                       used for checkout AND gh auth (password only → GH_TOKEN)
 *       spark-api-key — API key for the internal Spark (cyberbot) endpoint
 *
 */

 @Library('cybersift') _

pipeline {
    agent any

    tools {
        nodejs 'NodeJS-24'
    }

    options {
        timestamps()
        disableConcurrentBuilds(abortPrevious: true)
        buildDiscarder(logRotator(numToKeepStr: '20'))
    }
   
    environment {        
        SPARK_API_KEY     = credentials('spark-api-key')
        PATH              = "${env.HOME}/.pi/bin:${env.PATH}"
    }

    stages {        
        
        stage('AI PR review') {
            when { changeRequest() }
            steps {
                aiPrReview(
                    credentialsId: 'github-pat',
                    googleChatSpaceId: 'AAQAvFxDcSg',
                    googleChatKeyCredentialsId: 'google-chat-rules-key',
                    googleChatTokenCredentialsId: 'google-chat-rules-token',
                    reviewPromptFile: 'pi/soc-rules-review-prompt.txt'
                )
            }
            post {
                always {
                    archiveArtifacts artifacts: 'pi-pr-review.md', allowEmptyArchive: true
                }
            }
        }        
        
    }

    post {                        

        cleanup {
            cleanWs(cleanWhenNotBuilt: false,
                    deleteDirs: true,
                    disableDeferredWipeout: true,
                    notFailBuild: true
            )
        }       
        
    
    }
}
