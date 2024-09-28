import masks

def mask_account_card(card_info:str)->str:

    """получает информацию о карте или банковском счете и преобразовывает их в маску с помощью ранее написанных функций"""
    card_info = card_info.split()
    number_mask_list =[]
    for i in card_info:
        if (i.isalpha()):
            number_mask_list.extend([i,' '])
        else:
            if number_mask_list[0][0].lower()=='с':
                number_mask_list.append(masks.card_number_mask(i))
            else:
                number_mask_list.append(masks.get_mask_card_number(i))

    return ''.join(number_mask_list)
