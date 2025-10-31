# From the Deep

In this problem, you'll write freeform responses to the questions provided in the specification.


## Random Partitioning

Argument in favour is that it is easy to do, implementing it would be easy as we just have to send information to any available boat. Also might be in some case if it is required to anonymize data then its a useful approach.

Argument against it is that there is no organisation of data, so any of CRUD operation is harder to perform and would require more time and computing resource.


## Partitioning by Hour

FAVOUR: Better organisation of data, easier to search and manage information.

AGAINST: Information load is unevenly distributed, some will be overloaded and some underloaded. Not best usage of available resource.


## Partitioning by Hash Value

Its the best overall approach so far, evenly ditributed the data to all boats and querying is also more organised.

The only downside is when looking for some value in a time range we still have to querry multiple boats.
