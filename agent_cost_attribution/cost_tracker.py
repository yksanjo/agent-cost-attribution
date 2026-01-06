from anthropic import Anthropic
import pandas as pd
import plotly.express as px
from flask import Flask, render_template
import json
from datetime import datetime
from typing import Dict, Any

class CostTracker:
    def __init__(self):
        self.cost_data = []
        self.app = Flask(__name__)
        self.setup_routes()
    
    def record_cost(self, agent_name: str, cost: float, usage: Dict[str, Any]):
        """Record cost for an agent invocation"""
        record = {
            'agent_name': agent_name,
            'cost': cost,
            'usage': usage,
            'timestamp': datetime.now()
        }
        self.cost_data.append(record)
    
    def get_cost_summary(self) -> Dict[str, Any]:
        """Get cost summary by agent"""
        df = pd.DataFrame(self.cost_data)
        if df.empty:
            return {}
        
        summary = df.groupby('agent_name').agg({
            'cost': ['sum', 'mean', 'count'],
        }).round(4)
        
        summary.columns = ['total_cost', 'avg_cost', 'invocation_count']
        return summary.to_dict(orient='index')
    
    def setup_routes(self):
        @self.app.route('/')
        def dashboard():
            return self.generate_dashboard()
    
    def generate_dashboard(self):
        """Generate cost visualization dashboard"""
        if not self.cost_data:
            return "<h1>No cost data available</h1>"
        
        df = pd.DataFrame(self.cost_data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Create cost trend chart
        fig = px.line(df, x='timestamp', y='cost', color='agent_name', 
                      title='Agent Cost Trend Over Time')
        chart_html = fig.to_html(full_html=False)
        
        # Create summary table
        summary = self.get_cost_summary()
        summary_html = f"<h2>Cost Summary</h2><pre>{json.dumps(summary, indent=2)}</pre>"
        
        return f"{summary_html}<br>{chart_html}"
    
    def run_dashboard(self, host='127.0.0.1', port=5000):
        """Run the cost dashboard server"""
        self.app.run(host=host, port=port, debug=False)