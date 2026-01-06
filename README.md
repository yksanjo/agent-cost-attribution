# Agent Cost Attribution Script

![License](https://img.shields.io/github/license/ai-engineer-community/agent-cost-attribution)
![Python](https://img.shields.io/badge/Made%20with-Python-blue)
![Flask](https://img.shields.io/badge/Dashboard-Flask-red)

SDK wrapper + analytics dashboard showing per-agent token costs (input/output breakdown), cost per tool invocation, model cost trends over time, and alerts when costs exceed thresholds.

## Features

- SDK wrapper for tracking agent costs
- Per-agent token costs (input/output breakdown)
- Cost per tool invocation
- Model cost trends over time
- Alerts when costs exceed thresholds
- Analytics dashboard

## Installation

```bash
pip install agent-cost-attribution
```

## Usage

```python
from anthropic import Anthropic
from agent_cost_attribution import CostTracker

client = Anthropic()
cost_tracker = CostTracker()

def track_agent_call(agent_name, model):
    response = client.messages.create(...)
    cost = (response.usage.input_tokens * 0.003 +
            response.usage.output_tokens * 0.015) / 1000
    cost_tracker.record_cost(agent_name, cost, response.usage)
    return response
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

MIT