"""
Core monitoring system components.
This module contains the base classes for the monitoring system.
"""

import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import random

class MetricData:
    """
    Represents a single metric measurement with its metadata.
    This class demonstrates how to create value objects in OOP.
    """
    def __init__(self, name: str, value: float, unit: str, timestamp: Optional[datetime] = None):
        self.name = name
        self.value = value
        self.unit = unit
        self.timestamp = timestamp or datetime.now()

    def to_dict(self) -> Dict:
        """Convert metric data to dictionary format for storage and transmission."""
        return {
            "name": self.name,
            "value": self.value,
            "unit": self.unit,
            "timestamp": self.timestamp.isoformat()
        }

class CloudResource:
    """
    Base class for any cloud resource we want to monitor.
    This follows the OOP principle of abstraction - defining a common interface
    for all cloud resources.
    """
    def __init__(self, resource_id: str, resource_type: str, region: str):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.region = region
        self.metadata: Dict = {}
        self.metrics: Dict = {}
        self.status = "unknown"
        
    def collect_metrics(self) -> Dict:
        """
        Abstract method that should be implemented by child classes.
        Each type of resource will collect different metrics.
        """
        raise NotImplementedError("Each resource type must implement collect_metrics()")

    def get_health_status(self) -> str:
        """Determine if the resource is healthy based on its metrics."""
        return self.status

class Alert:
    """
    Represents a monitoring alert.
    Demonstrates creating data classes for specific purposes.
    """
    def __init__(self, resource_id: str, metric_name: str, threshold: float,
                 current_value: float, severity: str):
        self.resource_id = resource_id
        self.metric_name = metric_name
        self.threshold = threshold
        self.current_value = current_value
        self.severity = severity
        self.timestamp = datetime.now()
        self.resolved = False

    def to_dict(self) -> Dict:
        """Convert alert to dictionary format for storage and transmission."""
        return {
            "resource_id": self.resource_id,
            "metric_name": self.metric_name,
            "threshold": self.threshold,
            "current_value": self.current_value,
            "severity": self.severity,
            "timestamp": self.timestamp.isoformat(),
            "resolved": self.resolved
        }