import justpy as jp
def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analyis of Course reviews",classes="text-h1 text-center")
    p1 = jp.QDiv(a=wp , text="The graphs represents course review analysis")
    return wp
jp.justpy(app)