# -*- coding: utf-8 -*-
from flask import redirect
from application import application


@application.errorhandler(403)
def forbidden(error):
    print(error)
    return redirect("https://http.cat/403")


@application.errorhandler(404)
def page_not_found(error):
    print(error)
    return redirect("https://spartacodingclub.kr/404")


@application.errorhandler(410)
def gone(error):
    print(error)
    return redirect("https://http.cat/410")


@application.errorhandler(500)
def internal_server_error(error):
    print(error)
    return redirect("https://http.cat/500")


@application.errorhandler(401)
def no_authentication(error):
    print(error)
    return redirect("https://http.cat/401")