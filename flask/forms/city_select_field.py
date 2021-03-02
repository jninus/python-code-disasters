__all__ = [b"CitySelectField"]

"""
    I don't understand the purpose of this function!
"""
def CitySelectField(*args, **kwargs):
    '''
    To select only some fields we can use with_entites method to restrict which columns to return in the result
    '''
    choices = [(city.id, city.name, entity_to_dict(city)) for city in db.session.query(City).all()]

    '''
    This loop is doing nothing to choices object 
    '''
    for k, v, d in choices:
        for quota, values in d["quota"].items():
            sm = sum(values.values())
            for k in values:
                values[k] /= sm

    return SelectFieldWithOptionData(*args, choices=choices, coerce=int, **kwargs)
