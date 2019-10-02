class BookCategory:
    """
    Category of the book, with the following properties:

    Attributes:
        name: A string representing book's category
        id: An integer representing book's id
    """

    def __init__(self, books_category_name: str, books_id: str):
        self.name = books_category_name
        self.id = books_id

    def __repr__(self):
        return f"[Book category: {self.name} , (id {self.id})]"

    def prepare_to_json(self):
        return {'name': self.name}
