def build_user_profile(user_id: int, **kwargs) -> dict:
    profile = {'user_id': user_id}
    profile.update(kwargs)
    return profile
print(build_user_profile(1, name="Иван", city="Томск"))
print(build_user_profile(2, name="Мария", age=25, job="инженер"))