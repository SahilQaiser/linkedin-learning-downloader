#!/usr/bin/python

USERNAME = ''
PASSWORD = ''

# Login to LinkedIn and get the cookie under www.linkedin.com with key li_at 
# COOKIE = 'AQEGAGMBAAAAAAgg-1wAAAGB7HC1cgAAAYMRlJYATQAARnVybjpsaTplbnRlcnByaXNlUHJvZmlsZToodXJuOmxpOmVudGVycHJpc2VBY2NvdW50Ojc0NDE1MDY4LDEzODAxNzA3NCm4FPGKh9s1Ykkj0kLR-9pRdn319C7kNhtpzmDxp6VCBbcMtYoOccipLyckXo03d4Ccey6ksT1cclxC-S347NqQoYvu4NpnNXJ1Yrj6CoEBTPCBR2M'
COOKIE = 'AQEGAGMBAAAAAAoGh5kAAAGFq0hBQAAAAYXPVMVATgAARnVybjpsaTplbnRlcnByaXNlUHJvZmlsZToodXJuOmxpOmVudGVycHJpc2VBY2NvdW50Ojc0NDE1MDY4LDE0MjIxMDIyNCmeqywxfcGA9ZCVqQ2yznjpEsmceOmsdEdzE-ih1Dj6k4IXEQWgomRHpHbxSD45t5EApHgWC27aJVHGex8jAl730ARcb76EGYUuzQO4rjyovCQu098'


# 1
# https://www.linkedin.com/learning/instructors/tj-guttormsen?u=74415068
# 0 is start and 50 is count, e.g blinkist has 68 videos
# Keep the count as multiple of 10
INSTRUCTORS = {
    # 'blinkist': '0_50',
    # 'blinkist': '50_20',
    # 'tj-guttormsen': '0_10'
    # 'jay-fields' : '0_10'
    # 'careercake' : '0_30',
    # 'london-app-brewery' : '0_10',
    # 'chill-anywhere': '0_10',
    # 'sounds-true': '0_30',
    # 'dave-crenshaw': '0_40',
    # 'desk-yogi': '0_10',
    # 'kevin-bowersox' : '0_20',
    # 'hiroko-nishimura' : '0_10',
    # 'bear-cahill' : '0_20',
    # 'raghavendra-dixit' : '0_10'
    # 'ketkee-aryamane' : '0_10'
}
# 2
# https://www.linkedin.com/learning/paths/become-a-financial-analyst?u=74415068
PATHS = [
    # 'become-a-financial-analyst',
    # 'become-a-react-developer',
    # 'become-a-javascript-developer'
]
# 3
# https://www.linkedin.com/learning/learning-redis/welcome?u=74415068
COURSES = [
    # 'learning-redis'
    # 'learning-procreate',
    # '20-habits-of-executive-leadership',
    # 'mongodb-essential-training',
    # 'introduction-to-docker-for-java-developers',
    # 'jenkins-essential-training-17420152',
    # 'learning-jenkins-14423877',
    # 'running-jenkins-on-aws-8591136',
    # 'learning-hashicorp-packer',
    # 'learning-python-14393370',
    # 'practice-java-arrays'
    # 'building-monorepos-on-github',
    # 'learning-github-actions-2',
    # 'advanced-github-actions',
    # 'git-branches-merges-and-remotes',
    # 'devops-with-aws',
    # 'monitoring-aws-with-cloudwatch',
    # 'aws-monitoring-and-reporting',
    # 'aws-monitoring-logging-and-remediation',
    # 'aws-for-devops-monitoring-metrics-and-logging',
    # 'arcgis-pro-essential-training-14681078',
    # 'creating-maps-with-r',
    # 'learning-r-2',
    # 'apache-kafka-essential-training-getting-started',
    # 'stream-processing-design-patterns-with-kafka-streams',
    # 'learn-apache-kafka-for-beginners'
    # 'spring-6-and-spring-boot-3-first-look'
    # 'advanced-java-development'
    # 'level-up-java'
]

CHOICE = 3

# If any Course needs to be skipped from the Learning Path or Instructor Courses.
# SKIP = [1,3,4] will only download 2nd and other courses with index+1 > 4
SKIP = []

# Location where to store the Videos
# LOCATION = 'Self-Help/CareerCake'
LOCATION = 'Tech/JAVA/Advanced/'

# 119
DOWNLOADED_COURSES = [
    # 'pro-level-photography-for-graphic-designers',
    # 'photography-foundations-mobile-photography',
    # 'the-elements-of-effective-photographs',
    # 'photography-foundations-lenses',
    # 'photography-foundations-exposure-part-1',
    # 'photography-foundations-exposure-part-2',
    # 'photography-advanced-composition',
    # '5-day-photo-challenge-composition',
    # 'travel-photography-mountains-and-snow-landscapes',
    # 'photography-foundations-night-and-low-light',
    # 'photography-101-shooting-macros-and-close-ups',
    # 'photography-101-shooting-in-low-light',
    # 'panasonic-lumix-gh5-tips-tricks-and-techniques'
    # 'advanced-photography-diptychs-triptychs-and-aspect-ratios'
    # 'landscape-photography-washington-s-palouse-region'
    # 'canva-web-and-digital-design-projects',
    # 'learning-canva-2',
    # 'microservices-security',
    # 'building-angular-and-django-apps',
    # 'building-react-and-django-apps'
    # 'python-projects-14276284'
    # 'java-database-access-with-hibernate',
    # 'spring-design-patterns',
    # 'spring-framework-in-depth-2',
    # 'spring-spring-data-2',
    # 'spring-messaging-with-jms',
    # 'spring-spring-security',
    # 'building-full-stack-apps-with-react-and-spring',
    # 'spring-spring-mvc-2',
    # 'building-a-full-stack-app-with-angular-2-plus-and-spring-boot',
    # 'advanced-spring-effective-integration-testing-with-spring-boot',
    # 'spring-spring-cloud-2',
    # 'advanced-spring-application-events',
    # 'spring-spring-batch',
    # 'spring-spring-integration',
    # 'spring-cloud-gcp-setting-up-a-cloud-sql-database',
    # 'spring-code-challenges',
    # 'running-spring-boot-in-production',
    # 'building-real-time-web-apps-with-spring-boot-and-websockets',
    # 'performance-tuning-in-spring-apps',
    # 'java-ee-contexts-and-dependency-injection',
    # 'spring-boot-2-0-essential-training-2',
    # 'software-design-modeling-with-uml',
    # 'programming-foundations-design-patterns-2',
    # 'sustainable-software-architecture,
    # 'software-architecture-patterns-for-developers',
    # 'software-architecture-domain-driven-design',
    # 'behavior-driven-development',
    # 'microservices-design-patterns',
    # 'microservices-asynchronous-messaging',
    # 'kubernetes-microservices',
    # 'software-architecture-from-developer-to-architect',
    # 'cloud-architecture-advanced-concepts-14595141',
    # 'cloud-architecture-core-concepts-15687584',
    # 'serverless-architecture',
    # 'serverless-and-microservices-for-aws',
    # 'enterprise-architecture-foundations',
    # 'enterprise-architecture-in-practice',
    # 'advanced-sql-for-application-development',
    # 'java-ee-design-patterns-and-architecture',
    # 'designing-highly-scalable-and-highly-available-sql-databases',
    # 'learn-api-programming-by-building-a-telegram-bot',
    # 'designing-restful-apis',
    # 'design-thinking-understanding-the-process',
    # 'software-architecture-breaking-a-monolith-into-microservices',
    # 'interaction-design-structure',
    # 'json-processing-with-java-ee',
    # 'websocket-programming-with-java-ee',
    # 'java-ee-8-javaserver-faces-jsf-2-3',
    # 'java-ee-bean-validation',
    # 'java-ee-javaserver-faces-jsf',
    # 'java-database-integration-with-jdbc',
    # 'java-generic-classes-14576260',
    # 'learning-java-collections',
    # 'java-exception-handling',
    # 'java-design-patterns-creational',
    # 'advanced-java-programming-2',
    # 'java-design-patterns-structural',
    # 'java-design-patterns-behavioral-part-1',
    # 'java-design-patterns-behavioral-part-2',
    # 'java-data-structures-14403471',
    # 'java-lambdas-and-streams',
    # 'java-code-challenges',
    # 'nail-your-java-interview-2',
    # 'java-algorithms',
    # 'java-persistence-api-jpa-2-inheritance-and-querying',
    # 'java-persistence-api-jpa-1-the-basics',
    # 'java-recursion',
    # 'learning-gwt',
    # 'learning-java-lambda-expressions',
    # 'multi-module-build-automation-with-maven',
    # 'java-build-automation-with-maven',
    # 'java-ee-8-web-services',
    # 'java-concurrency-troubleshooting-data-access-and-consistency',
    # 'java-concurrency-troubleshooting-latency-and-throughput',
    # 'code-clinic-java-2018',
    # 'java-with-json',
    # 'introduction-to-data-structures-algorithms-in-java',
    # 'java-memory-management',
    # 'parallel-and-concurrent-programming-with-java-1',
    # 'parallel-and-concurrent-programming-with-java-2',
    # 'java-memory-management-values-and-references',
    # 'java-memory-management-garbage-collection-jvm-tuning-and-spotting-memory-leaks',
    # 'building-restful-web-services-with-dropwizard',
    # 'java-ee-concurrency-and-multithreading',
    # 'java-microservices-with-graalvm',
    # 'learning-quarkus',
    # 'advanced-sql-high-performance-relational-divisions',
    # 'advanced-sql-solving-interpolation-challenges',
    # 'advanced-sql-for-application-development',
    # 'sql-code-challenges',
    # 'advanced-sql-logical-query-processing-part-1',
    # 'advanced-sql-logical-query-processing-part-2',
    # 'nail-your-sql-interview',
    # 'web-scraping-with-python',
    # 'python-xml-json-and-the-web',
    # 'advanced-python-working-with-databases'
    # 'advanced-django',
    # 'python-data-structures-trees' 
]