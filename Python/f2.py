Modern virtual machines, such as Java and Inferno, are emerging as network computing
platforms. While these virtual machines provide higher-level abstractions and more
sophisticated services than their predecessors from twenty years ago, their architecture has
essentially remained unchanged. State of the art virtual machines are still monolithic, that is,
they are comprised of closely-coupled service components, which are thus replicated over all
computers in an organization. This crude replication of services forms one of the weakest
points in today’s networked systems, as it creates widely acknowledged and well-publicized
problems of security, manageability and performance.
We have designed and implemented a new system architecture for network computing based
on distributed virtual machines. In our system, virtual machine services that perform rule
checking and code transformation are factored out of clients and are located in enterprisewide network servers. The services operate by intercepting application code and modifying it
on the fly to provide additional service functionality. This architecture reduces client resource
demands and the size of the trusted computing base, establishes physical isolation between
virtual machine services and creates a single point of administration. We demonstrate that
such a distributed virtual machine architecture can provide substantially better integrity and
manageability than a monolithic arc.

