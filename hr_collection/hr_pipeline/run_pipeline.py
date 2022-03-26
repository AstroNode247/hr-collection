from hr_collection.hr_pipeline.data_pipeline.data_source import PromotionData, AttritionData
from hr_collection.hr_pipeline.pipeline.action import Pipeline

from hr_collection.config import config

if __name__ == "__main__":
    promotion = PromotionData()
    pipeline = Pipeline(promotion)
    pipeline.run()
    pipeline.load_to_db("promotion", config.POSTGRES_CONN)
