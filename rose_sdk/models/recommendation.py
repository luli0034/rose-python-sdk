"""
Recommendation models for the Rose Python SDK.
"""

from typing import List, Dict, Any, Optional, Union
from .base import BaseModel


class Recommendation(BaseModel):
    """Recommendation model."""

    data: List[Dict[str, Any]]


class RecommendationFileInfo(BaseModel):
    """Recommendation file info model."""

    url: str


class RecommendationExportInfo(BaseModel):
    """Recommendation export info model."""

    export: Dict[str, RecommendationFileInfo]


class BulkRequest(BaseModel):
    """Bulk request model."""

    payload: List[Dict[str, Any]]


class RecommendationItem(BaseModel):
    """Individual recommendation item with flexible structure."""
    
    key: List[str]
    key_as_string: str
    doc_count: int
    # Allow any additional fields dynamically
    model_config = {"extra": "allow"}
    
    
    def get_field(self, field_name: str, default: Any = None) -> Any:
        """Get a field value by name, returning default if not found."""
        return getattr(self, field_name, default)
    
    
    def get_metric(self, metric_name: str) -> Optional[float]:
        """Get a metric value, handling nested structure like {'value': 3.0}."""
        metric = getattr(self, metric_name, None)
        if isinstance(metric, dict) and 'value' in metric:
            return metric['value']
        elif isinstance(metric, (int, float)):
            return float(metric)
        return None


class AggregationResults(BaseModel):
    """Aggregation results containing buckets and metadata."""
    
    doc_count_error_upper_bound: int
    sum_other_doc_count: int
    buckets: List[RecommendationItem]


class AggregationRecommendation(BaseModel):
    """Aggregation-based recommendation model."""
    
    results: AggregationResults


