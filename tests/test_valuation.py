import pytest
from app.service import EquipmentValuationService, InvalidModelYear, EquipmentNotFound


def test_valid_calculation():
    result = EquipmentValuationService.get_values("87390", 2016)

    assert result["marketValue"] == 30008
    assert result["auctionValue"] == 20426


def test_default_ratio_used():
    # 67352 has no data beyond 2012, so 2015 should use default (0.02)
    result = EquipmentValuationService.get_values("67352", 2015)

    assert result["marketValue"] == round(681252 * 0.02)
    assert result["auctionValue"] == round(681252 * 0.02)


def test_invalid_year_low():
    with pytest.raises(InvalidModelYear):
        EquipmentValuationService.get_values("87390", 2005)


def test_invalid_year_high():
    with pytest.raises(InvalidModelYear):
        EquipmentValuationService.get_values("87390", 2021)


def test_invalid_classification():
    with pytest.raises(EquipmentNotFound):
        EquipmentValuationService.get_values("99999", 2016)