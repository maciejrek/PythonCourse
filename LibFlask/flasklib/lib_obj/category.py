class Category:
    """
    Category of the book, with the following properties:

    Attributes:
        name: A string representing book's category
        id: An integer representing book's id
    """

    def __init__(self, cat_id: int, books_category_name: str, is_active: bool):
        self.uid = cat_id
        self.name = books_category_name
        self.active = is_active

    def __repr__(self):
        return f"[Book category: {self.name}]"