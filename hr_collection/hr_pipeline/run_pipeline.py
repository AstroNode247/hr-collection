from hr_collection.hr_pipeline.data_pipeline.data_source import PromotionData, AttritionData, PromotionTestData
from hr_collection.hr_pipeline.pipeline.action import Pipeline

from hr_collection.config import config


def promotion_pipeline():
    print("***********************  Promotion  *************************")
    promotion = PromotionData()
    pipeline.data = promotion
    pipeline.run()
    pipeline.load_to_db("promotion", config.POSTGRES_CONN)


def attrition_pipeline():
    print("************************ Attrition ***************************")
    attrition = AttritionData()
    pipeline.data = attrition
    pipeline.run()
    pipeline.load_to_db("attrition", config.POSTGRES_CONN)


def promotion_test_pipeline():
    print("************************* Promotion Test *********************")
    promotionTest = PromotionTestData()
    pipeline.data = promotionTest
    pipeline.run()
    pipeline.load_to_db("promotion_test", config.POSTGRES_CONN)


if __name__ == "__main__":
    pipeline = Pipeline()
    promotion_pipeline()
    attrition_pipeline()
