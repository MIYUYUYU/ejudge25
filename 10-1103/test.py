# 批量数据验证
def validate_users(users):
    errors = []
    for user in users:
        if not user.get('name'):
            errors.append(ValueError(f"用户 {user.get('id')} 缺少姓名"))
        if not isinstance(user.get('age'), int):
            errors.append(TypeError(f"用户 {user.get('id')} 年龄格式错误"))

    if errors:
        raise ExceptionGroup("用户数据验证失败", errors)


# 分别处理不同类型的错误
try:
    validate_users([
        {'id': 1, 'name': ''},
        {'id': 2, 'age': 'invalid'},
        {'id': 3, 'name': 'Alice', 'age': 25}
    ])
except* ValueError as ve:
    print("姓名相关的错误:", [str(e) for e in ve.exceptions])
except* TypeError as te:
    print("类型相关的错误:", [str(e) for e in te.exceptions])