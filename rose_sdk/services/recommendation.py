"""
Recommendation service for the Rose Python SDK.
"""

from typing import List, Dict, Any, Optional, Union
from ..models.recommendation import (
    Recommendation,
    RecommendationExportInfo,
    BulkRequest,
    AggregationRecommendation,
    RecommendationItem,
)


class RecommendationService:
    """Service for recommendation operations."""

    def __init__(self, client):
        self.client = client

    def get(
        self, query_id: str, parameters: Optional[Dict[str, Any]] = None
    ) -> Union[Recommendation, AggregationRecommendation]:
        """
        Get recommendation results from a specific query.
        Automatically detects the response type and returns the appropriate model.

        Args:
            query_id: The query ID
            parameters: Parameters for the query

        Returns:
            Recommendation or AggregationRecommendation object based on response structure
        """

        response = self.client.get(f"/recommendations/{query_id}", params=parameters)
        # Check if the response has aggregation structure
        if "results" in response["data"] and "buckets" in response["data"]["results"]:
            return AggregationRecommendation(**response["data"])
        else:
            return Recommendation(**response["data"])

    def batch_query(self, query_id: str, payload: List[Dict[str, Any]]) -> List[Recommendation]:
        """
        Batch request static (pre-computed) recommendation results.

        Args:
            query_id: The query ID
            payload: A bulk of parameter groups

        Returns:
            List of Recommendation objects
        """
        data = BulkRequest(payload=payload)
        response = self.client.post(f"/recommendations/{query_id}:batchQuery", data=data.model_dump())
        recommendations = []
        for rec_data in response["data"]:
            # Response structure: {"data": {"data": [...], "user_id": "..."}}
            recommendation_items = rec_data["data"]["data"]
            recommendations.append(Recommendation(data=recommendation_items))
        return recommendations

    def get_export_info(self, query_id: str, expiration: Optional[int] = None) -> RecommendationExportInfo:
        """
        Get information about exported recommendation results.

        Args:
            query_id: The query ID
            expiration: The expiration time of the export information in seconds

        Returns:
            RecommendationExportInfo object
        """
        params = {}
        if expiration is not None:
            params["expiration"] = expiration

        response = self.client.get(f"/recommendations/{query_id}:export", params=params)
        return RecommendationExportInfo(**response["data"])
