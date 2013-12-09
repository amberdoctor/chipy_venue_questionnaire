# coding: utf8
#Needs to be first since creating auth_users creates auth_groups
if db(db.auth_group.id>0).count() == 0:
    db.auth_group.insert(
        role='venue_manager',
        description='Has the ability to view venues.',
    )
