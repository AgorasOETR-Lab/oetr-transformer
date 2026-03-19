def rotate_roles(heads, roles, step):
    assignments = {}
    for i, head in enumerate(heads):
        role_index = (i + step) % len(roles)
        assignments[head] = roles[role_index]
    return assignments
