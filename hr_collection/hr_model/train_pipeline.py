from hr_collection.hr_model.hr_classification import AttritionModel, PromotionModel
from hr_collection import __version__ as _version

import logging
_logger = logging.getLogger(__name__)

if __name__ == "__main__":
    attritionModel = AttritionModel()
    attritionModel.train(.2, 20)
    attritionModel.evaluate()

    attritionModel.save_pickle(f"attrition_classifier")

    print("******************************************\n")
    promotionModel = PromotionModel()
    promotionModel.train(.3, 20)
    promotionModel.evaluate()
    promotionModel.save_pickle("promotion_classifier")
