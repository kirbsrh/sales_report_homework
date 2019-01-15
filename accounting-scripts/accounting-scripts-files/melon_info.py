


    # from melons import melon_names, melon_seedlessness, melon_prices


    # def print_melon(name, seedless, price):
    #     """Print each melon with corresponding attribute information."""

    #     have_or_have_not = 'have'
    #     if seedless:
    #         have_or_have_not = 'do not have'

    #     print(f"{name}s {have_or_have_not} seeds and are ${price:.2f}")


    # for i in melon_names:
    #     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])




from melons import melon_data

def print_melon_data(melon_data):

    have_or_have_not = 'have'
    for melon, data in melon_data.items():
        if data["seedless"]:
            have_or_have_not = 'do not have'
        else:
            have_or_have_not = 'have'

        print(f"{melon}s {have_or_have_not} seeds and are ${data['price']:.2f}")

    for melon, data in melon_data.items():
        print(melon)
        for k,v in data.items():
            print(f"      {k}:{v}")



print_melon_data(melon_data)