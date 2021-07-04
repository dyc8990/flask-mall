from flask import Blueprint

admin = Blueprint('admin', __name__)  # 定义蓝图对象

import app.admin.views