def display_time(seconds):
    intervals = (
    ('days', 86400),    # 60 * 60 * 24
    ('hours', 3600),    # 60 * 60
    ('minutes', 60),
    ('seconds', 1),
    )
    result = []

    for _, count in intervals:
        value = seconds // count
        seconds -= value * count
        result.append(value)
    data = {}
    data['days'] = result[0]
    data['hours'] = result[1]
    data['minutes'] = result[2]
    data['seconds'] = result[3]

    return data