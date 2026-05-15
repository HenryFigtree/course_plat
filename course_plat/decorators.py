from functools import wraps
from flask import g, abort, redirect, url_for

def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


def admin_required(view):
    @login_required
    @wraps(view)
    def wrapped_view(**kwargs):
        if not g.user['is_admin']:
            abort(403)

        return view(**kwargs)

    return wrapped_view

