class SearchContactsForm:
    '''
    This module builds a form that searches for
    contacts available inside the repository of contacts
    provided by the application

    Methods
    -------
    search_by_category(category: str) -> List[dict]
        Searches for contacts by category
        and retunts a list of contacts
        that match the category

    rerender_canvas(contacts: List[dict]) -> None
        Rerenders the canvas with the newly searched contacts
    '''
    def __init__(self) -> None:
        pass