import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point


class MarkerPublisher(Node):
    def __init__(self):
        super().__init__("marker_publisher")
        self.publisher = self.create_publisher(Marker, "visualization_marker", 10)
        self.timer = self.create_timer(0.5, self.publish_marker)

    def publish_marker(self):
        marker = Marker()
        marker.header.frame_id = "base_link"
        marker.type = Marker.SPHERE
        marker.action = Marker.ADD

        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2

        marker.color.r = 0.0
        marker.color.g = 0.0
        marker.color.b = 1.0
        marker.color.a = 1.0

        marker.pose.orientation.w = 1.0
        marker.pose.position.x = 0.5
        marker.pose.position.y = 0.0
        marker.pose.position.z = 0.1

        self.publisher.publish(marker)
        self.get_logger().info("Published blue marker")


def main(args=None):
    rclpy.init(args=args)
    node = MarkerPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
