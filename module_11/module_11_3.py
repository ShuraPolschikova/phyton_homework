def introspection_info(obj):
    obj_type = type(obj)
    obj_attr = dir(obj)
    obj_module = obj.__module__
    obj_methods = [met for met in obj_attr if callable(getattr(obj, met))]
    obj_id = id(obj)


    info = {'type': obj_type, 'attributes': obj_attr, 'methods': obj_methods, 'module': obj_module, 'id' : obj_id, }
    return info


class Examples:
    def first_method(self):
        pass

    def second_method(self):
        pass

    def third_method(self):
        pass


example = Examples()
inform = introspection_info(example)

print(inform)
