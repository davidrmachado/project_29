def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    logged_students = 0

    for login, logout in permanence_period:
        if type(login) != int or type(logout) != int:
            return None
        if login <= target_time <= logout:
            logged_students += 1

    return logged_students
