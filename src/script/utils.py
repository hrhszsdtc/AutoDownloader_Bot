import jsbeautifier


def Beautify_Js(input_js):
    options = jsbeautifier.defalt_options()
    formatted_js = jsbeautifier_beautify(input_js, options)
    return formatted_js
