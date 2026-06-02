"""Launch the Ch05 Agentic VLA full node stack.

HuNavSim/Webots and Nav2 are started from the simulator environment first.
This top-level launch delegates to system2_bringup's full-stack launch.
"""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    full_stack_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [
                    FindPackageShare("system2_bringup"),
                    "launch",
                    "system2_full_stack.launch.py",
                ]
            )
        ),
        launch_arguments={
            "backend": LaunchConfiguration("backend"),
            "model": LaunchConfiguration("model"),
            "go_home_location": LaunchConfiguration("go_home_location"),
        }.items(),
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "backend",
                default_value="",
                description="LLM backend override. Empty value uses system2 config.",
            ),
            DeclareLaunchArgument(
                "model",
                default_value="",
                description="LLM model override. Empty value uses system2 config.",
            ),
            DeclareLaunchArgument(
                "go_home_location",
                default_value="charging_station",
                description="Fallback semantic location for recovery.",
            ),
            full_stack_launch,
        ]
    )
