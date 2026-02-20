from app.data import DATA


class EquipmentNotFound(Exception):
    pass


class InvalidModelYear(Exception):
    pass


class EquipmentValuationService:
    MIN_YEAR = 2006
    MAX_YEAR = 2020

    @staticmethod
    def get_values(classification_id: str, model_year: int):
        if model_year < EquipmentValuationService.MIN_YEAR or model_year > EquipmentValuationService.MAX_YEAR:
            raise InvalidModelYear(
                f"Model Year must be between {EquipmentValuationService.MIN_YEAR} "
                f"and {EquipmentValuationService.MAX_YEAR}."
            )

        if classification_id not in DATA:
            raise EquipmentNotFound("Classification ID not found.")

        equipment = DATA[classification_id]
        cost = equipment["saleDetails"]["cost"]
        schedule = equipment["schedule"]

        year_data = schedule["years"].get(str(model_year))

        if year_data:
            market_ratio = year_data["marketRatio"]
            auction_ratio = year_data["auctionRatio"]
        else:
            market_ratio = schedule["defaultMarketRatio"]
            auction_ratio = schedule["defaultAuctionRatio"]

        market_value = round(cost * market_ratio)
        auction_value = round(cost * auction_ratio)

        return {
            "classificationId": classification_id,
            "modelYear": model_year,
            "marketValue": market_value,
            "auctionValue": auction_value,
        }