# -*- coding: utf-8 -*-
from __future__ import absolute_import

import random


def random_choice_for_list(item_list):
    """
    リストから取得(確率によって)
    params: item_list <list: <tuple: (item, probability)>>
    return item<?>, index<int>
    """
    total_probability = sum([
        item_probability for item, item_probability in item_list
    ])
    i = random.uniform(0, total_probability)

    cumulative_probability = 0
    index = 0
    choice_item = None
    for item, item_probability in item_list:
        cumulative_probability += item_probability
        choice_item = item
        if i < cumulative_probability:
            break
        index += 1

    return choice_item, index
