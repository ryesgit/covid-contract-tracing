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
    
    user_with_most_headers = user_data[list(user_data.keys())[0]]

    # Iterate through the users and get the user with the most number of headers
    for user in user_data:
        if len(user_data[user]) > len(user_with_most_headers):
            user_with_most_headers = user_data[user]

    list_of_headers = list(user_with_most_headers.keys())
    list_of_records = list(user_data.keys())

    number_of_headers = len(list_of_headers)

    converted_data = []

    headers = []
    for header in range(number_of_headers):
        header_value = list(user_with_most_headers.keys())[header]
        headers.append(header_value)
    converted_data.append(headers)
    for record in list_of_records:
        record_values = []
        for header in list_of_headers:
            record_values.append(user_data.get(record, '').get(header, ''))
        converted_data.append(record_values)

    return converted_data