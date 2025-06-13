class Person:
    def __init__(self, name, mom=None, dad=None, born=None, died=None):
        self.name = name
        self.mom = mom
        self.dad = dad
        self.born = born
        self.died = died

    def life_span(self):
        return f"{self.born or '?'}-{self.died or '?'}"

    def __repr__(self):
        """Return a string representation of the person."""
        info = f"{self.name} ({self.life_span()})"
        info += f", Mom: {self.mom.name if self.mom else 'Unknown'}"
        info += f", Dad: {self.dad.name if self.dad else 'Unknown'}"
        return info

    def print_family_tree(self, prefix="", level=0):
        """Print the family tree starting from this person."""
        indent = "    " * level
        print(f"{prefix}{self.name} ({self.life_span()})")
        if self.mom:
            self.mom.print_family_tree(f"{indent}mom: ", level + 1)
        if self.dad:
            self.dad.print_family_tree(f"{indent}dad: ", level + 1)


granbois_7 = Person("Eugénie Granbois", born="1838", died="1907")
baquié_47 = Person("Ferdinand Baquié", born="1837", died="1883")
baquié_46 = Person("Louise Baquié", mom=granbois_7, dad=baquié_47, born="1868", died="1945")
ramos_1459 = Person("Marie Ramos", born="1826", died="1904")
martinez_8709 = Person("Jacques Martinez", born="1822", died="1891")
martinez_8708 = Person("Joseph Martinez", mom=ramos_1459, dad=martinez_8709, born="1864", died="1926")
martinez_9931 = Person("Adele Martinez", mom=ramos_1459, dad=martinez_8709, born="1860", died="Unknown")
martinez_9932 = Person("Gerard Martinez", mom=ramos_1459, dad=martinez_8709, born="Unknown")
martinez_9927 = Person("Mildred Martinez", mom=baquié_46, dad=martinez_8708, born="1911", died="1990")
prevost_1179 = Person("Jeanne Prevost", born="1864", died="Unknown")
fontaine_2773 = Person("Ernest Fontaine", born="1857", died="1919")
fontaine_2776 = Person("Suzanne Fontaine", mom=prevost_1179, dad=fontaine_2773, born="1894", died="1979")
alioto_37 = Person("Maria Alioto" , born="1834", died="aft.1908")
riggitano_1 = Person("Santo Riggitano", born="1824", died="1898")
riggitano_2 = Person("Salvatore Riggitano", mom=alioto_37, dad=riggitano_1, born="1876", died="1960")
prevost_1163 = Person("Louis Prevost", mom=fontaine_2776, dad=riggitano_2, born="1920", died="1997")
prevost_1162 = Person("Robert Prevost", born="1955", mom=martinez_9927, dad=prevost_1163)


prevost_1162.print_family_tree()