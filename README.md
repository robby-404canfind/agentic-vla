# Agentic VLA

Agentic VLA 최종 실습용 ROS2 workspace입니다. Ch02-Ch05에서 만든 핵심 패키지는 repository root 아래 submodule로 연결하고, 시나리오 자산과 실행 보조 파일은 `agentic_vla` 패키지에서 직접 관리합니다.

## 구조

| 경로 | 역할 |
| :-- | :-- |
| `social_nav_bringup` | Ch02 social navigation 기반 패키지 submodule |
| `system_interfaces` | Ch04+ Action interface 패키지 submodule |
| `perception_bringup` | Ch04/Ch05 perception, find/scan/follow, assess/resolve ActionServer submodule |
| `system2_bringup` | Ch05 System2 planner/action dispatcher submodule |
| `agentic_vla` | HuNavSim agent 설정, mission examples, launch/scripts 직접 관리 패키지 |

모든 submodule은 `agentic-vla` 브랜치를 추적합니다.

## Clone

```bash
git clone --branch ros2 --recurse-submodules https://github.com/robby-404canfind/agentic-vla.git
cd agentic-vla
git submodule update --init --recursive
```

이미 clone한 뒤 최신 실습 브랜치로 맞출 때는 다음 명령을 사용합니다.

```bash
bash agentic_vla/scripts/bootstrap_submodules.sh
```

## Build

기존 Ch03/Ch05 `system2_bringup` 패키지를 같은 colcon workspace에서 빌드한 상태라면 먼저 이전 build/install 산출물을 정리합니다.

```bash
rm -rf build/system2_bringup install/system2_bringup
```

그다음 의존성을 설치하고 workspace를 빌드합니다.

```bash
rosdep install --from-paths . --ignore-src -r -y
colcon build --symlink-install --packages-up-to agentic_vla
source install/setup.bash
```

## HuNavSim Agent Config

`agentic_vla/config/`에는 factory와 office smoke test용 HuNavSim agent 설정이 들어 있습니다. HuNavSim Docker workspace의 `hunav_agent_manager/config/` 경로를 알고 있다면 다음 스크립트로 복사할 수 있습니다.

```bash
bash agentic_vla/scripts/copy_hunav_agents.sh /path/to/hunav_agent_manager/config
```

factory, hall semantic location의 실제 좌표는 최종 simulator map에서 RViz로 측정한 뒤 `system2_bringup/config/semantic_locations.yaml`에 반영합니다.

## Run

HuNavSim/Webots와 Nav2를 먼저 실행한 뒤, 이 workspace에서 Agentic VLA 노드를 실행합니다.

```bash
source install/setup.bash
ros2 launch agentic_vla agentic_vla_system.launch.py
```

대표 mission 예시는 `agentic_vla/config/mission_examples.yaml`에 정리되어 있습니다.
