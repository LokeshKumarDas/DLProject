from src.cnnClassifier import logger
from cnnClassifier.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_2_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_3_model_trainer import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_4_model_evaluation import EvaluationPipeline

logger.info(f'Welcome! project starts now.')

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"------- stage {STAGE_NAME} started -------")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"------- stage {STAGE_NAME} completed -------\n\nx")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f"------- stage {STAGE_NAME} started -------")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f"------- stage {STAGE_NAME} completed -------\n\n")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Training"
try:
    logger.info(f"*******************")
    logger.info(f"------- stage {STAGE_NAME} started -------")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f"------- stage {STAGE_NAME} completed -------\n\n")
except Exception as e:
    logger.exception(e)
    raise e
# to activate mlflow uncomment line in {pipeline/stage_4_model_evaluation}
STAGE_NAME = "Evaluation stage"
try:
   logger.info(f"*******************")
   logger.info(f"------- stage {STAGE_NAME} started -------")
   model_evalution = EvaluationPipeline()
   model_evalution.main()
   logger.info(f"------- stage {STAGE_NAME} completed -------\n\n")

except Exception as e:
        logger.exception(e)
        raise e
    
    
# to execute run 
# dvc init
# dvc repro
# dvc dag # to visualize the pipeline