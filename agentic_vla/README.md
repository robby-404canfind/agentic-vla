# agentic_vla

`agentic_vla`는 최종 시나리오 기반 실습에서 직접 수정할 launch, scenario, mission example 자산을 보관하는 얇은 ROS2 패키지입니다. 핵심 기능 패키지는 같은 workspace의 submodule로 관리합니다.

## 포함 파일

- `config/mission_examples.yaml`: hall 기준 자연어 mission 예시와 기대 high-level action 패턴입니다.
- `config/semantic_locations.factory_hall.yaml`: factory 확장 실습용 placeholder입니다. 기본 Ch05 실습에서는 사용하지 않습니다.
- `config/hunav_agents_factory.yaml`: factory 확장 환경의 HuNavSim agent 예시입니다.
- `config/hunav_agents_office_mixed.yaml`: office 확장 smoke test용 HuNavSim agent 예시입니다.
- `launch/agentic_vla_system.launch.py`: perception stack과 System2 planner/action server를 함께 실행합니다.
- `scripts/bootstrap_submodules.sh`: repository root의 submodule을 `agentic-vla` 브랜치 기준으로 동기화합니다.
- `scripts/copy_hunav_agents.sh`: HuNavSim agent 설정 파일을 시뮬레이터 config 디렉터리로 복사합니다.

## 실행 흐름

HuNavSim/Webots와 Nav2는 시뮬레이터 환경에서 먼저 실행합니다. 그다음 이 workspace에서 다음 launch를 실행합니다.

```bash
source install/setup.bash
ros2 launch agentic_vla agentic_vla_system.launch.py
```

LLM backend/model을 임시로 바꾸려면 launch argument를 사용합니다.

```bash
ros2 launch agentic_vla agentic_vla_system.launch.py \
  backend:=openrouter model:=openai/gpt-oss-120b:free
```
