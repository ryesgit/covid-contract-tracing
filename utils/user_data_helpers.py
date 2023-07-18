def convert_data_to_array(user_data: dict) -> list:
    '''
    Converts the user data to an array.
    First level of the array are the headers,
    Following levels are the user data.

    Parameters
    ----------
    user_data : dict
        The user data to convert to an array.

    Returns
    -------
    user_data: list
        The user data in an array.
    '''

    # If given file is empty, return nothing
    if len(user_data) == 0:
        return [[], []]

    if type(user_data) == list:
        return user_data

    number_of_headers = len(user_data[list(user_data.keys())[0]])

    list_of_headers = list(user_data[list(user_data.keys())[0]].keys())
    list_of_records = list(user_data.keys())

    converted_data = []

    headers = []
    for header in range(number_of_headers):
        first_dict_key = list(user_data.keys())[0]
        header_value = list(user_data[first_dict_key].keys())[header]
        headers.append(header_value)
    converted_data.append(headers)
    for record in list_of_records:
        record_values = []
        for header in list_of_headers:
            record_values.append(user_data.get(record, '').get(header, ''))
        converted_data.append(record_values)

    return converted_data