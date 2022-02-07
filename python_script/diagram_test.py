from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.analytics import Spark
from diagrams.onprem.compute import Server
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.aggregator import Fluentd
from diagrams.onprem.monitoring import Grafana, Prometheus
from diagrams.onprem.network import Nginx, Vyos, Pfsense, Internet
from diagrams.onprem.queue import Kafka
from diagrams.generic.network import Firewall, Router, Switch, Subnet


with Diagram(name="Network Diagram", show=False):
#    ingress = Vyos("Router1")
#    attCloud = Internet("AT&T cloud")
#
#    metrics = Pfsense("Firewall1")
#    attCloud >> metrics >> ingress
    
    
    

    with Cluster("Small Site"):
        routers = [Router("Router3"), Router("Router4")]
        switch1 = Switch("Switch1")
        switch2 = Switch("Switch2")
        switch3 = Switch("Switch3")
        switch31 = Switch("Switch31")
        switch32 = Switch("Switch32")
        switch4 = Switch("Switch4")
        switch5 = Switch("Switch5")
        subnet = Subnet("10.0.0.0/8,\n192.168.1.0/24")
        dist = [switch2, switch3, switch31, switch32]
        att = Internet("AT&T cloud")
        vsat = Internet("vsat cloud")
        #firewalls = (Firewall("Firewall3"), Firewall("Firewall4"))
        att - routers[0]
        vsat - routers[1]
        routers - Firewall("Firewall3") - subnet
        routers - Firewall("Firewall4") - subnet
        routers[0] - switch1 - dist
        dist[0] - switch4
        dist[1] - switch5


            
    
    #with Cluster("Service Cluster"):
    #    grpcsvc = [
    #        Server("grpc1"),
    #        Server("grpc2"),
    #        Server("grpc3")]
#
    #with Cluster("Sessions HA"):
    #    main = Redis("session")
    #    main - Edge(color="brown", style="dashed") - Redis("replica") << Edge(label="collect") << metrics
    #    grpcsvc >> Edge(color="brown") >> main
#
    #with Cluster("Database HA"):
    #    main = PostgreSQL("users")
    #    main - Edge(color="brown", style="dotted") - PostgreSQL("replica") << Edge(label="collect") << metrics
    #    grpcsvc >> Edge(color="black") >> main
#
    #aggregator = Fluentd("logging")
    #aggregator >> Edge(label="parse") >> Kafka("stream") >> Edge(color="black", style="bold") >> Spark("analytics")
#
    #ingress >> Edge(color="darkgreen") << grpcsvc >> Edge(color="darkorange") >> aggregator