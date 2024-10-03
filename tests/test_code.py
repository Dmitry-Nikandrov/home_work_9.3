from src.widget import*
from src.masks import*



def test_get_mask_card_number():
    assert get_mask_card_number('1234567890167890')=='1234 56** **** 7890'
    assert get_mask_card_number('123456789016789a') == 'присутствие нечисловых символов'
    assert get_mask_card_number(None) == '0'
    assert get_mask_card_number('123456789016789012334')=='слишком длинный номер карты'

def test_card_number_mask():
    assert card_number_mask('1234567890167894')=='**7894'
    assert card_number_mask('123456789016') == '**9016'
    assert card_number_mask('123456789016788779012') == 'слишком длинный номер карты'
    assert card_number_mask('12345678901678a') == 'присутствие нечисловых символов'

def test_get_date():
    pass


print(get_date('2024-03-11T02:26:18.671407'))