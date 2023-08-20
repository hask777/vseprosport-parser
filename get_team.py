def get_team_name(teams_names, prediction):
    for team_name in teams_names:
        if f'«{team_name}»' in prediction\
        \
        or f'{team_name}а' in prediction\
        or f'{team_name[:-1]}а' in prediction\
        \
        or f'{team_name}у' in prediction\
        or f'{team_name[:-1]}у' in prediction\
        \
        or f'{team_name}и' in prediction\
        or f'{team_name[:-1]}и' in prediction\
        \
        or f'{team_name[:-1]}ы' in prediction\
        or f'{team_name}ы' in prediction:
            return team_name