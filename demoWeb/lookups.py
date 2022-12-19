from dal import autocomplete

class LookupMainDishes(autocomplete.Select2ListView):
    def get_list(self):
        menu = ['BUTTER CHICKEN', 'PALAK PANEER', 'SPICY PORK VINDALOO', 'INDIAN STYLE LENTILS']
        print(self.forwarded)
        return menu


class LookupDessertDishes(autocomplete.Select2ListView):
    def get_list(self):
        menu = ['Mixed berry mousse', 'Mango and coconut soufflé', 'Homemade carrot cake', 'Matcha cake']
        return menu