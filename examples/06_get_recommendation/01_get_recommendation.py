#!/usr/bin/env python3
"""
Basic Get Recommendation Example

This example demonstrates how to get recommendations using the Rose Python SDK.
It shows the most common use case of getting personalized recommendations for a user.
"""

import os
from rose_sdk import RoseClient
from rose_sdk.exceptions import RoseAPIError, RoseNotFoundError
from rose_sdk.models.recommendation import AggregationRecommendation, Recommendation

def main():
    """Main function to demonstrate basic recommendation retrieval."""
    
    # Initialize the Rose client
    # You can set these as environment variables or replace with your actual values
    base_url = os.getenv('ROSE_BASE_URL', 'https://admin-test.rose.blendvision.com')
    access_token = os.getenv('ROSE_ACCESS_TOKEN', 'your_access_token_here')
    
    client = RoseClient(
        base_url=base_url,
        access_token=access_token
    )
    
    print("🌹 Rose Python SDK - Basic Get Recommendation Example")
    print("=" * 60)
    
    # Example 1: Get recommendations for a specific user
    print("\n📋 Example 1: Get recommendations for a user")
    print("-" * 50)
    
    try:
        # Replace with your actual query ID
        query_id = "your_query_id_here"
        
        # Parameters for the recommendation query
        # These parameters will be passed to your recommendation algorithm
        parameters = {
            "gte": "now-3h",
            "size": 10,  # Number of recommendations to return
        }
        
        print(f"Query ID: {query_id}")
        print(f"Parameters: {parameters}")
        
        # Get recommendations
        recommendations = client.recommendations.get(
            query_id=query_id,
            parameters=parameters
        )
        if isinstance(recommendations, AggregationRecommendation):
            print(f"\n✅ Successfully retrieved recommendations!")
            print(f"Number of recommendations: {len(recommendations.results.buckets)}")
            
            # Display the recommendations
            for i, rec in enumerate(recommendations.results.buckets, 1):
                print(f"  {i}. {rec.key_as_string} - {rec.get_metric('item_count')}")
        elif isinstance(recommendations, Recommendation):
            print(f"\n✅ Successfully retrieved recommendations!")
            print(f"Number of recommendations: {len(recommendations.data)}")
            
            # Display the recommendations
            for i, rec in enumerate(recommendations.data, 1):
                print(f"  {i}. {rec}")
    except RoseNotFoundError:
        print("❌ Error: Query not found. Please check your query_id.")
    except RoseAPIError as e:
        print(f"❌ API Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        raise
    
   
    print("\n" + "=" * 60)
    print("🎉 Basic Get Recommendation Example Complete!")
    print("\n💡 Tips:")
    print("- Make sure to replace 'your_query_id_here' with an actual query ID")
    print("- Set ROSE_BASE_URL and ROSE_ACCESS_TOKEN environment variables")
    print("- Adjust parameters based on your recommendation algorithm requirements")
    print("- Handle empty results gracefully in your application")


if __name__ == "__main__":
    main()
