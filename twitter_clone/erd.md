```mermaid
erDiagram
    Users {
        string USERNAME
        string PASSWORD
    }
    Tweets {
        string USERNAME
        string STATUS
        string TWEET
    }
    Users }o..o{ Tweets : yhteys
```
  