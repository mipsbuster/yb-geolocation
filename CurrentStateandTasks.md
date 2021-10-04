# Current State and Tasks Geo-Location



- **infrastructure** - Develop/fix the YB multi-region setup
  - need a simple way to allow users to spin up a 3 region demo cluster
    - Complete to include vpc peering, security etc. 
    - AWS? 
      - Cloudformation, AWS CDK?
- **business use cases** - Add workloads/SQL/transactions simulating busness process for geo-location
  - Query account balance
  - debit account
  - credit account
  - close account
  - open account
- **db infrastructure** - Update and refactor database build and seed of core data
- **operations** - Develop 3-4 use case s and demo examples of geo-location in action
  - loss and then restoe of a region
  - usage of default tablespace
  - adding new geo-location and data migration
- **operations** - Load testing geo-location. 
  - large data sets
    - TPS
    - latencies
- Add additional language examples for YB geo-location?
  - Java Spring Boot
  - Javascript
  - Go

