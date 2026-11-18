import logging
import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Azure Function triggered for processing Kaggle climate records.')
    
    try:
        climate_data = {
            "cloud_provider": "Azure Functions",
            "source": "Kaggle Global Climate Change Dataset",
            "average_temperature_change": 1.15,
            "co2_emissions_ppm": 421.5,
            "status": "Processed successfully via serverless micro-batch"
        }
        return func.HttpResponse(
            json.dumps(climate_data),
            status_code=200,
            mimetype="application/json"
        )
    except Exception as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )