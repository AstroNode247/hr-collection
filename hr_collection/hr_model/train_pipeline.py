from hr_collection.hr_model.hr_classification import AttritionModel, PromotionModel

if __name__ == "__main__":
    attritionModel = AttritionModel()
    attritionModel.train(.2, 20)
    attritionModel.evaluate()

    print("******************************************\n")
    promotionModel = PromotionModel()
    promotionModel.train(.3, 20)
    promotionModel.evaluate()

