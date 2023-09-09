from diagrams import Diagram, Cluster, Edge
from diagrams.k8s.compute import Pod
from diagrams.onprem.network import Nginx
from diagrams.onprem.database import MySQL 
from diagrams.onprem.storage import CEPH
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.queue import Kafka
from diagrams.onprem.monitoring import Prometheus
from diagrams.elastic.elasticsearch import Elasticsearch

with Diagram("crm", show=True, direction="TB"):
    ingress = Nginx("ingress")
    # ingress >> Pod("frontend")

    with Cluster("microservices in k8s"):
        api_gateway = Pod("api gateway")

        account = Pod("account")
        leads = Pod("leads")
        ticket = Pod("ticket")
        checkin = Pod("checkin")
        other = Pod("...")
        search = Pod("search service")

        grpc = Edge(label="grpc")

        api_gateway >> grpc >> account
        api_gateway >> grpc >> leads
        api_gateway >> grpc >> ticket
        api_gateway >> grpc >> checkin
        api_gateway >> grpc >> other
        api_gateway >> grpc >> search

    with Cluster("data", direction="LR"):
        es = Elasticsearch("search")
        db = MySQL("db")
        kafka = Kafka("kafka")
        ceph = CEPH("ceph")
        redis = Redis("redis")
        prometheus = Prometheus("prometheus")

    ingress >> api_gateway
    search >> es