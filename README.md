# RViz Marker Demo

A ROS 2 package demonstrating the usage of visualization markers in RViz2.

## Description

This package provides examples of publishing visualization markers that can be displayed in RViz2. It serves as a demonstration of how to create and publish various types of markers in ROS 2.

## Prerequisites

* ROS 2 (tested on Humble)
* RViz2
* Python 3.8+

## Installation

1. Create a ROS 2 workspace (if you haven't already):
```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```

2. Clone this repository:
```bash
git clone https://github.com/parvej-mosaraf/rviz_marker_demo.git
```

3. Install dependencies:
```bash
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y
```

4. Build the package:
```bash
colcon build --packages-select rviz_marker_demo
```

5. Source the setup file:
```bash
source ~/ros2_ws/install/setup.bash
```

## Usage

1. Start the marker publisher node:
```bash
ros2 run rviz_marker_demo marker_publisher
```

2. Launch RViz2:
```bash
rviz2
```

3. In RViz2:
   - Add a MarkerArray display type
   - Set the topic to `/visualization_marker_array`
   - Set the Fixed Frame to the appropriate frame (default: `map`)

## Package Structure

```
rviz_marker_demo/
├── package.xml        # Package manifest
├── setup.py          # Package setup file
├── setup.cfg         # Package configuration
├── resource/         # Package resources
├── rviz_marker_demo/ # Source directory
│   ├── __init__.py
│   └── marker_publisher.py
└── test/            # Test files
    ├── test_copyright.py
    ├── test_flake8.py
    └── test_pep257.py
```

## Testing

To run the tests:

```bash
colcon test --packages-select rviz_marker_demo
```

## License

TODO: Add license information

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Authors

* **Your Name** - *Initial work*

## Acknowledgments

* ROS 2 Development Team
* RViz2 Development Team
