#!/usr/bin/env python
"""
Stock Research Crew - Main Entry Point

This script orchestrates a comprehensive stock analysis workflow that includes:
1. Stock research and data gathering
2. S&P 500 benchmark analysis
3. Data processing and organization
4. Comparative visualization
5. AI-generated investment suggestions

Usage:
    python main.py [STOCK_SYMBOL]
    
Examples:
    python main.py "AAPL"
    python main.py "GOOGL"
    python main.py "MSFT"

Environment Variables:
    STOCK_SYMBOL: Default stock symbol if not provided via command line
    OPENAI_API_KEY: Required for LLM functionality
    SERPER_API_KEY: Required for web search functionality
"""

import os
import sys
import logging
from pathlib import Path
from dotenv import load_dotenv
import warnings

# Suppress non-critical warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('stock_analysis.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables from .env file (located at root, 3 levels up)
env_path = Path(__file__).parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

from crew import StockResearchCrew


def validate_environment():
    """Validate that all required environment variables are set."""
    required_keys = ['OPENAI_API_KEY', 'SERPER_API_KEY']
    missing_keys = [key for key in required_keys if not os.getenv(key)]
    
    if missing_keys:
        logger.error(f"Missing required environment variables: {', '.join(missing_keys)}")
        logger.error(f"Please set these variables in .env file at: {env_path}")
        return False
    return True


def get_stock_symbol():
    """Get stock symbol from command line or environment variables.
    
    Returns:
        str: Stock symbol to analyze (defaults to 'AAPL')
    """
    stock = None
    
    # Priority 1: Command line argument
    if len(sys.argv) > 1:
        stock = sys.argv[1].upper()
        logger.info(f"Stock symbol from command line: {stock}")
    
    # Priority 2: Environment variable
    if not stock:
        stock = os.getenv('STOCK_SYMBOL', '').upper()
        if stock:
            logger.info(f"Stock symbol from environment: {stock}")
    
    # Priority 3: Default
    if not stock:
        stock = 'AAPL'
        logger.info(f"Using default stock symbol: {stock}")
    
    return stock


def run():
    """Main execution function for stock research crew.
    
    Workflow:
    1. Validate environment setup
    2. Get stock symbol
    3. Initialize and run crew
    4. Generate analysis reports
    """
    try:
        logger.info("=" * 70)
        logger.info("Stock Research & S&P 500 Benchmark Analysis System")
        logger.info("=" * 70)
        
        # Validate environment
        if not validate_environment():
            sys.exit(1)
        
        # Get stock symbol
        stock = get_stock_symbol()
        
        # Display startup information
        print(f"\n{'='*70}")
        print(f"Stock Analysis vs S&P 500 Benchmark")
        print(f"Stock Symbol: {stock}")
        print(f"{'='*70}\n")
        
        logger.info(f"Starting analysis for stock: {stock}")
        
        # Initialize and run crew
        logger.info("Initializing Stock Research Crew...")
        crew_instance = StockResearchCrew()
        
        # Prepare inputs for crew execution
        inputs = {
            'stock': stock
        }
        
        logger.info("Executing crew workflow...")
        print("\n[STARTING ANALYSIS WORKFLOW]")
        print("-" * 70)
        
        # Execute crew with error handling
        try:
            result = crew_instance.crew().kickoff(inputs=inputs)
            
            logger.info("Crew execution completed successfully")
            print("-" * 70)
            print("\n[ANALYSIS COMPLETE]")
            print("\nGenerated Files:")
            print("  1. stock_sp500_data.txt - Structured comparison data")
            print("  2. stock_analysis_summary.txt - Visualization and analysis")
            print("  3. investment_suggestion_report.txt - Investment recommendations")
            print("  4. stock_analysis_logs.txt - Detailed execution logs")
            print("  5. stock_analysis.log - Python logging output")
            print("\n" + "="*70 + "\n")
            
            return result
            
        except Exception as e:
            logger.error(f"Error during crew execution: {str(e)}", exc_info=True)
            print(f"\n[ERROR] Crew execution failed: {str(e)}")
            sys.exit(1)
    
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}", exc_info=True)
        print(f"\n[FATAL ERROR] {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    run()

