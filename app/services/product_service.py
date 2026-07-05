class ProductService:

    @staticmethod
    def get_products():
        return [
            {
                "id": 1,
                "name": "MacBook Air M4",
                "price": 89999,
                "category": "Laptop",
            },
            {
                "id": 2,
                "name": "Dell Inspiron 15",
                "price": 65999,
                "category": "Laptop",
            },
            {
                "id": 3,
                "name": "iPhone 16",
                "price": 79999,
                "category": "Mobile",
            },
        ]

    @staticmethod
    def search_products(question: str):

        question = question.lower()

        products = ProductService.get_products()

        if "laptop" in question:
            return [
                product
                for product in products
                if product["category"].lower() == "laptop"
            ]

        if "mobile" in question or "phone" in question:
            return [
                product
                for product in products
                if product["category"].lower() == "mobile"
            ]

        return products        