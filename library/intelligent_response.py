from lib import *
from library import ml


def intelligent_response(constrains, param_dict):
    if param_dict.__contains__('type'):
        if constrains.__contains__(param_dict['type']):
            vars_needed = constrains[param_dict['type']].__code__.co_varnames[:
                                                                              constrains[param_dict[
                                                                                  'type']].__code__.co_argcount]
            allowed = True
            params = []
            for var in vars_needed:
                if param_dict.__contains__(var):
                    params.append(ml.url_decode(param_dict[var]))
                else:
                    ml.error_log(f'param {var} is not contained')
                    allowed = False
            if allowed:
                return HttpCrossDomainResponse(constrains[param_dict['type']](*params))
            else:
                return HttpFailure()
        else:
            ml.error_log(f'this type {param_dict["type"]} is not defined')
            return HttpFailure()
    else:
        ml.error_log('param not contains "type"')
        return HttpFailure()
