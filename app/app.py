from flask import Blueprint
from app.controllers import UfController

bp = Blueprint('main', __name__)
uf = UfController()


@bp.route('/uf')
def index():
    return uf.index()
