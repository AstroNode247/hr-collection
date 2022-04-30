from hr_collection.config import features


def validate_input_promotion(input_data):
    validated_data = input_data.copy()

    if input_data[features.PROMOTION_NUM_NA_NOT_ALLOWED].isnull().any().any():
        validated_data = validated_data.dropna(subset=features.PROMOTION_NUM_NA_NOT_ALLOWED, axis=0)

    if input_data[features.PROMOTION_CAT_NA_NOT_ALLOWED].isnull().any().any():
        validated_data = validated_data.dropna(subset=features.PROMOTION_CAT_NA_NOT_ALLOWED)

    return validated_data


def validate_input_attrition(input_data):
    validated_data = input_data.copy()
    if input_data[features.ATTRITION_NUM_NA_NOT_ALLOWED].isnull().any().any():
        validated_data = validated_data.dropna(subset=features.ATTRITION_NUM_NA_NOT_ALLOWED, axis=0)
    if input_data[features.ATTRITION_CAT_NA_NOT_ALLOWED].isnull().any().any():
        validated_data = validated_data.dropna(subset=features.ATTRITION_CAT_NA_NOT_ALLOWED, axis=0)

    return validated_data
