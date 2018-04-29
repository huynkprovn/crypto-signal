"""
Helper functions for the various strategies
"""

class Utils():
    """
    Helper functions for the various strategies
    """
    def get_closing_prices(self, historical_data):
        """
        Returns closing prices within a specified time frame for a coin pair
        """
        closing_prices = []
        for data_point in historical_data:
            closing_prices.append(data_point[4])
        return closing_prices
