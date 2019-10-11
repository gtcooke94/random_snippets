def tags_equal(tag1, tag2):
    quote_chars = ['"', "'"]
    elements1 = get_elements(tag1, quote_chars)
    elements2 = get_elements(tag2, quote_chars)
    dict1 = elements_to_dict(elements1, quote_chars)
    dict2 = elements_to_dict(elements2, quote_chars)
    return dict1 == dict2


def get_elements(tag, quote_chars):
    tag = tag[1:-1].lower()
    elements = tag.split(" ")
    elements = handle_spaces(elements, quote_chars)
    return elements


def elements_to_dict(elements, quote_chars):
    elements_dict = {}
    for element in elements:
        left = element
        right = None
        if "=" in element:
            left, right = element.split("=")
            for char in quote_chars:
                if char in right:
                    right = handle_string(right, char)
        if left in elements_dict:
            continue
        elements_dict[left] = right
    return elements_dict


def handle_string(val, char):
    val = val[1:-1]
    return val


def handle_spaces(elements, quote_chars):
    i = 0
    fixed_elements = []
    char_replaced = False
    for i, element in enumerate(elements):
        new_element = element
        if char_replaced:
            char_replaced = False
            continue
        for char in quote_chars:
            if char in elements[i]:
                if i + 1 >= len(elements):
                    continue
                if not char in elements[i + 1]:
                    continue
                char_replaced = True
                # We've split on a space
                new_element = element + " " + elements[i + 1]
                new_element = new_element.replace(char, "")
        fixed_elements.append(new_element)
    return fixed_elements
