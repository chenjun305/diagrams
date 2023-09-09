from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.network import Nginx
from diagrams.alibabacloud.network import Cdn
from diagrams.aws.mobile import Mobile
from diagrams.programming.language import Java
from diagrams.onprem.client import Client
from diagrams.onprem.aggregator import Fluentd
from diagrams.onprem.queue import Kafka
from diagrams.onprem.analytics import Hadoop


with Diagram("tracking system", show=True, direction="TB"):
    app = Mobile("App with tracking SDK")
    tracking_cluster = Nginx("nginx")
    config_cluster = Nginx("nginx")
    cdn = Cdn("CDN")
    backend = Java("backend")
    admin = Client("admin")
    log_collector = Fluentd("log collector")
    kafka = Kafka("event stream")
    hadoop = Hadoop("hdfs")

    config = Edge(label="config", color="darkorange")
    event  = Edge(label="event log", color="brown")

    app << config << cdn << config_cluster << backend << admin
    app >> event >> tracking_cluster >> event >> log_collector >> kafka >> hadoop